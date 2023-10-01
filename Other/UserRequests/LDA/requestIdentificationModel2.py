# using LDA with the unlabelled dataset

# imports
import pandas as pd
import gensim
from gensim import corpora
from gensim.models import LdaModel
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Preprocess the data
def preprocess_comments(comments):
    processed_comments = []
    stop_words = set(stopwords.words('english'))

    for comment in comments:
        # Tokenize the comment
        tokens = word_tokenize(comment.lower())
        
        # Remove stop words and punctuation
        filtered_tokens = [token for token in tokens if token.isalpha() and token not in stop_words]
        
        processed_comments.append(filtered_tokens)
    
    return processed_comments

# Feature extraction
def extract_features(comments):
    # Create a dictionary from the comments
    dictionary = corpora.Dictionary(comments)
    
    # Create a bag-of-words corpus
    corpus = [dictionary.doc2bow(comment) for comment in comments]
    
    return dictionary, corpus

# Train LDA model
def train_lda_model(corpus, num_topics):
    lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics, random_state=42)
    return lda_model

# Prepare the dataset
data = pd.read_csv("../DataCollection/Data/1/new_youtube_comments_preprocess_1.csv", header=0) 
comments = data['text_original_cleaned']

# Step 1: Preprocess the comments
processed_comments = preprocess_comments(comments)

# Step 2: Feature extraction
dictionary, corpus = extract_features(processed_comments)

# Step 3: Train LDA model
num_topics = 6
lda_model = train_lda_model(corpus, num_topics)

# Step 4: Inference
# Prepare the dataset
data = pd.read_csv("../DataCollection/Data/1/cleaned_labeled_data.csv", header=0)

labeled_comments = []
identified_requirements = []

for index, row in data.iterrows():
    comment = row['comment_cleaned']
    user_requirement = row['is_user_request']

    processed_comment = preprocess_comments([comment])
    comment_bow = dictionary.doc2bow(processed_comment[0])
    topic_distribution = lda_model.get_document_topics(comment_bow)

    isRequirement = 0
    # add the topic_id and topic_probability to an array
    topic_details = []

    for topic in topic_distribution:
        topic_id, topic_prob = topic
        #print(comment, " - ", topic_id, " - ", topic_prob)
        topic_probability = topic_prob
        topic_details.append((topic_id, topic_probability))
    
    # get the array element with the highest probability
    topic_details.sort(key=lambda x: x[1], reverse=True)
    topic_id, topic_probability = topic_details[0]
    if (topic_id == 5):   
        isRequirement = 1
        identified_requirements.append(comment)

    labeled_comments.append((comment, isRequirement, user_requirement))

labeled_data = pd.DataFrame(labeled_comments, columns=['comment', 'is_requirement', 'actual_result'])
labeled_data.to_csv("output.csv", index=False)

# Step 5: Evaluation

# Display the identified requirements
#print("Identified Requirements:", len(identified_requirements))
#for requirement in identified_requirements:
    #print(requirement)

# get the accuracy of the identified requirements
import matplotlib.pyplot as plt

# Calculate accuracy
correct_predictions = sum(labeled_data['is_requirement'] == labeled_data['actual_result'])
total_predictions = len(labeled_data)
accuracy = correct_predictions / total_predictions * 100

# Display accuracy
print("Accuracy:", accuracy)

# Create a bar chart
labels = ['Accuracy']
values = [accuracy]

plt.bar(labels, values)
plt.ylim([0, 100])  # Set the y-axis limit from 0 to 100
plt.ylabel('Accuracy (%)')
plt.title('Model Accuracy')
plt.show()

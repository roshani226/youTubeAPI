from sklearn import feature_extraction
import commentGetter
from gensim import corpora
from gensim.models import LdaModel
import preProcessComments

# 1. get the comments from the video ID using Data API or scrapped comments
comments = commentGetter.getComments("Sxxw3qtb3_g")     # TODO: replace with the video ID from the selected video

# 2. preprocess the comments
allComments, cleanedComments, tokenizedComments = preProcessComments.preprocess_comments(comments)
print(type(tokenizedComments))

# 3. load the model
loaded_model = LdaModel.load("model1.lda")

# 4. perform inference
identified_requirements = []

dictionary = corpora.Dictionary(tokenizedComments)

for i in range(len(tokenizedComments)):
    comment = tokenizedComments[i]
    comment_bow = loaded_model.id2word.doc2bow(comment["tokens"])
    #comment_bow = dictionary.doc2bow(comment)
    topic_distribution = loaded_model.get_document_topics(comment_bow)

    isRequirement = 0
    # add the topic_id and topic_probability to an array
    topic_details = []

    for topic in topic_distribution:
        topic_id, topic_prob = topic
        topic_probability = topic_prob
        topic_details.append((topic_id, topic_probability))
        #print(comment["comment"], " --- ", str(topic_id), " --- ", str(topic_probability))
        
    # get the array element with the highest probability
    topic_details.sort(key=lambda x: x[1], reverse=True)
    topic_id, topic_probability = topic_details[0]
    if topic_id in [0, 3, 6, 9] and topic_probability > 0.3:
        isRequirement = 1
        #identified_requirements.append("Comment, Topic ID and Probability: " + comment + " --- " + str(topic_id) + " --- " + str(topic_probability))
        identified_requirements.append(allComments[i])

# 5. return the identified requirements
print("Identified Requirements: ", len(identified_requirements))
for identified_requirement in identified_requirements:
    print(identified_requirement)
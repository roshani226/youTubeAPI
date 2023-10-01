import demoTest
import evaluation
import feature_extraction
import getWords
import inference
import model_training
import pandas as pd
import preprocessing

# Prepare the dataset
data = pd.read_csv("../DataCollection/Data/1/new_youtube_comments_preprocess_1.csv", header=0) 

#print(data)
comments = data['text_original_cleaned']

# Step 1: Preprocess the comments
processed_comments = preprocessing.preprocess_comments(comments)
#print(processed_comments)

# Step 2: Feature extraction
dictionary, corpus = feature_extraction.extract_features(processed_comments)

# Step 3: Train LDA model
num_topics = 11

lda_model = model_training.train_lda_model(corpus, num_topics, dictionary,31)

# Get the word cloud for topics 
#getWords.getWords(lda_model)

# Step 4: Inference
# Prepare the dataset    
data = pd.read_csv("../DataCollection/Data/2/new-youtube-comments-labeled.csv", header=0)

#labeled_data, identified_requirements = inference.perform_inference(data, lda_model, dictionary)
#labeled_data.to_csv("output.csv", index=False)

# Step 5: Evaluation
# manual evaluation
accuracy = evaluation.calculate_accuracy(labeled_data)
print('Using the existing labelled data set - Accuracy: ', accuracy)

# Perplexity -> evaluate topic models (how well the model predicts the held-out data) - lower the better
perplexity = lda_model.log_perplexity(corpus)
print("Perplexity:", perplexity)

#evaluation.plot_accuracy(accuracy)

#accuracyForRandomState = []
#for random_state in range(0, 100):
#    lda_model = model_training.train_lda_model(corpus, num_topics, dictionary, random_state)
#
#    # Step 4: Inference
#    # Prepare the dataset
#    data = pd.read_csv("../DataCollection/Data/2/new-youtube-comments-labeled.csv", header=0)
#
#    labeled_data, identified_requirements = inference.perform_inference(data, lda_model, dictionary)
#    #labeled_data.to_csv("output.csv", index=False)
#
#    # Step 5: Evaluation
#    accuracy = evaluation.calculate_accuracy(labeled_data)
#    # append the random state and the accuracy as a string to an array
#    accuracyForRandomState.append('Random State: ' + str(random_state) + ' - Accuracy: ' + str(accuracy))
#
#df = pd.DataFrame({'accuracyForRandomState': accuracyForRandomState})
#df.to_csv('randomStateComparison1.txt', header=False, index=False, sep=' ', mode='a')

# Step 6: Test the model
#df = pd.read_csv("input.txt", header=0)
#output = demoTest.test_from_txt_file(df, lda_model, dictionary)
#
#for result in output:
#    print(result)


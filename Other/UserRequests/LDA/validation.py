import pandas as pd
import preprocessing
import feature_extraction
import matplotlib.pyplot as plt
import calculateCoherence

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
num_topics = 30

# Validation
# Define a range of topic numbers to try
min_topics = 1
max_topics = 30
step = 2
topic_nums = range(min_topics, max_topics+1, step)

# Calculate coherence scores for different topic numbers
coherence_scores = []
for num_topics in topic_nums:
    if __name__ ==  '__main__':
        coherence_score = calculateCoherence.calculate_coherence(dictionary, corpus, processed_comments, num_topics)
        coherence_score.runInParallel(numProcesses=2, numThreads=4)
        coherence_scores.append(coherence_score)

# Plot the coherence scores
plt.plot(topic_nums, coherence_scores)
plt.xlabel("Number of Topics")
plt.ylabel("Coherence Score")
plt.title("Coherence Score vs. Number of Topics")
plt.show()
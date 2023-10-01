import pandas as pd
import preprocessing

def perform_inference(data, lda_model, dictionary):
    labeled_comments = []
    identified_requirements = []

    for index, row in data.iterrows():
        comment = row['Comment']
        user_requirement = row['IsRequirement']

        processed_comments = (preprocessing.preprocess_comments([comment]))
        if not processed_comments:
            #print(index, ' - Skipping comment with no processed_comments:', comment)
            continue

        comment_bow = dictionary.doc2bow(processed_comments[0])
        topic_distribution = lda_model.get_document_topics(comment_bow)

        isRequirement = 0
        # add the topic_id and topic_probability to an array
        topic_details = []
        topic_details_for_file = []

        for topic in topic_distribution:
            topic_id, topic_prob = topic
            #print(comment, " - ", topic_id, " - ", topic_prob)
            topic_probability = topic_prob
            topic_details.append((topic_id, topic_probability))
            topic_details_for_file.append('Comment: ' + comment + ' - Topic ID: ' + str(topic_id) + ' - Topic Probability: ' + str(topic_probability))

        df = pd.DataFrame({'topic probabilities': topic_details_for_file})
        df.to_csv('topic_probabilities.txt', header=False, index=False, sep=' ', mode='a')

        # get the array element with the highest probability
        topic_details.sort(key=lambda x: x[1], reverse=True)
        topic_id, topic_probability = topic_details[0]
        if topic_id in [0, 3, 6, 9] and topic_probability > 0.3:  
            isRequirement = 1
            identified_requirements.append(comment)

        labeled_comments.append((comment, isRequirement, user_requirement))

    labeled_data = pd.DataFrame(labeled_comments, columns=['comment', 'result', 'expected_result'])
    return labeled_data, identified_requirements

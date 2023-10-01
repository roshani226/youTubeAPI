import preprocessing
import feature_extraction
import model_training
import inference
import pandas as pd

def test_from_txt_file(df, lda_model, dictionary):
    identified_requirements = []

    for index, row in df.iterrows():
        comment = row['comments']

        processed_comment = preprocessing.preprocess_comments([comment])
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

    return identified_requirements
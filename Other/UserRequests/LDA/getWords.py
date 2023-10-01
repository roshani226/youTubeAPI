from gensim import models
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def getWords(lda_model):
    for topic_id in range(lda_model.num_topics):
        words = lda_model.show_topic(topic_id, topn=30)  # Get the top 30 words for the topic
        wordcloud = WordCloud(background_color="white").generate_from_frequencies(dict(words))
        plt.figure()
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.title(f"Topic {topic_id + 1}")
        plt.axis("off")
        plt.show()
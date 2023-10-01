from gensim.models import LdaModel

def train_lda_model(corpus, num_topics, dictionary, random_state):
    lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics, random_state=random_state)
    lda_model.save("../CallerMethods/LDA/model.lda")
    return lda_model

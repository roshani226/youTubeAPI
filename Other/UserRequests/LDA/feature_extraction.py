from gensim import corpora

def extract_features(comments):
    # Create a dictionary from the comments
    dictionary = corpora.Dictionary(comments)
    
    # Create a bag-of-words corpus
    corpus = [dictionary.doc2bow(comment) for comment in comments]
    
    return dictionary, corpus

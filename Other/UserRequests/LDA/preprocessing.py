import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def preprocess_comments(comments):
    processed_comments = []
    stop_words = set(stopwords.words('english'))

    #comments = [comment for comment in comments if len(comment) < 200]
    comments = [comment for comment in comments if len(str(comment).split()) > 1]

    for comment in comments:
        # Tokenize the comment
        tokens = word_tokenize(comment.lower())
        
        # Remove stop words and punctuation
        filtered_tokens = [token for token in tokens if token.isalpha() and token not in stop_words]
        
        processed_comments.append(filtered_tokens)
    
    return processed_comments


def preprocess_comment(comment):

    stop_words = set(stopwords.words('english'))

    # Tokenize the comment
    tokens = word_tokenize(comment.lower())
        
    # Remove stop words and punctuation
    filtered_tokens = [token for token in tokens if token.isalpha() and token not in stop_words]
        
    
    return filtered_tokens

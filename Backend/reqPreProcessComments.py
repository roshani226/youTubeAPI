from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
from googletrans import Translator

def preprocess_comments(translated_comments):

    # Translate non-English comments to English
    #translated_comments = translate_comments_to_english(comments)

    # Remove comments with more than 200 characters or less than 2 words
    translated_comments = [comment for comment in translated_comments if len(comment) < 200]
    translated_comments = [comment for comment in translated_comments if len(comment.split()) > 1]

    # Remove urls, special characters, emojis and lowercase the text
    preProcessedComments = clean_text(translated_comments)

    # Tokenize the comments
    tokenizedText = tokenize_comments(preProcessedComments)

    return translated_comments, preProcessedComments, tokenizedText

# Remove urls, special characters, emojis and lowercase the text
def clean_text(comments):
    cleaned_comments = []
    
    for comment in comments:
        # Remove URLs
        comment = re.sub(r'http\S+', '', comment)
        
        # Remove special characters and emojis
        comment = re.sub(r'[^\w\s]', '', comment)
        
        # Lowercase the text
        comment = comment.lower()

        # Remove blank lines
        comment = re.sub(r'\n\s*\n', '\n', comment)
        
        cleaned_comments.append(comment)
    
    return cleaned_comments

# Tokenize the comments
def tokenize_comments(comments):
    tokenized_comments = []
    stop_words = set(stopwords.words('english'))

    for comment in comments:
        # Tokenize the comment
        tokens = word_tokenize(comment.lower())
        
        # Remove stop words and punctuation
        filtered_tokens = [token for token in tokens if token.isalpha() and token not in stop_words]
        
        tokenized_comments.append(filtered_tokens)
    
    return tokenized_comments

def translate_comments_to_english(comments):
    translated_comments = []
    translator = Translator()

    for comment in comments:
        if not comment.isascii():  # Check if comment is non-English
            translated_comment = translator.translate(comment, src='auto', dest='en').text
            #print(comment, " -> ",translated_comment)
        else:
            translated_comment = comment  # If English, no need for translation
        
        if translated_comment.strip():  # Check if the translated comment is not empty
            translated_comments.append(translated_comment)
        else:
            translated_comments.append("")

    return translated_comments
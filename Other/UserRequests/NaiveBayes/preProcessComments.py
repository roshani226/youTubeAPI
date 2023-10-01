from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
from googletrans import Translator

# Initialize the Google Translate API client
translator = Translator()

def preprocess_dataFrame(dataFrame):
    # Remove rows with invalid 'IsRequirement' values (not 0 or 1)
    dataFrame = dataFrame[dataFrame['IsRequirement'].isin([0, 1])]

    # Remove rows with empty lines in the 'Comment' column
    dataFrame = dataFrame[dataFrame['Comment'].str.strip() != '']
    
    # Convert 'Comment' column to strings and handle floating values
    dataFrame['Comment'] = dataFrame['Comment'].astype(str)

    # Preprocess comments
    # Remove comments with more than 200 characters or less than 2 words
    dataFrame = dataFrame[dataFrame['Comment'].str.len() < 200]
    dataFrame = dataFrame[dataFrame['Comment'].str.split().str.len() > 1]

    # Translate non-English comments to English
    translated_comments = []
    for comment in dataFrame['Comment']:
        if not comment.isascii():  # Check if comment is non-English
            translated_comment = translator.translate(comment, src='auto', dest='en').text
        else:
            translated_comment = comment  # If English, no need for translation
        
        if translated_comment.strip():  # Check if the translated comment is not empty
            translated_comments.append(translated_comment)
        else:
            translated_comments.append("null")
    
    # Update the DataFrame with preprocessed comments
    dataFrame['Comment'] = translated_comments
    # Remove rows where the comment is "null"
    dataFrame = dataFrame[dataFrame['Comment'] != "null"]

    cleaned_comments, tokenized_comments = preprocess_comments(dataFrame['Comment'])

    return dataFrame, tokenized_comments

def preprocess_comments(comments):

    # Remove urls, special characters, emojis and lowercase the text
    preProcessedComments = clean_text(comments)

    # Tokenize the comments
    tokenizedText = tokenize_comments(preProcessedComments)

    return preProcessedComments, tokenizedText

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
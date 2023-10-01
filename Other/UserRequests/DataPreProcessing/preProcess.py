import numpy as np
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Read the raw dataset
data = pd.read_csv("../DataCollection/Data/raw_dataset.csv")

# Drop the columns that are not required
data = data.drop(columns = ['commentId', 'videoId', 'authorDisplayName', 'authorProfileImageUrl', 'authorChannelUrl', 'authorChannelId', 
    'canRate', 'viewerRating', 'canReply', 'isPublic', 'publishedAt', 'updatedAt', 'likeCount', 'totalReplyCount', 'textDisplay'])

# removing the null value row
data = data[data['textOriginal'].notnull()]

# Remove urls, special characters, emojis and lowercase the text
def clean_text(text):
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    
    # Remove special characters and emojis
    text = re.sub(r'[^\w\s]', '', text)
    
    # Lowercase the text
    text = text.lower()
    
    return text

# Apply the clean_text function to the textOriginal column
data['text_original_cleaned'] = data['textOriginal'].apply(clean_text)
data = data.drop(columns = ['textOriginal'])

# Filter out comments with less than 5 characters and more than 150 characters
data = data[data['text_original_cleaned'].str.len() >= 5]
data = data[data['text_original_cleaned'].str.len() <= 150]

data.to_csv("../DataCollection/Data/preprocessed_dataset_step1.csv", index = False)
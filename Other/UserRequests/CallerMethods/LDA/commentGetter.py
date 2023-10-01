import json
import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
from pprint import pprint


# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv("USER_REQUIREMENTS_YOUTUBE_API_KEY")

def get_youtube():
    DEVELOPER_KEY = api_key 
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY)
    return youtube

def getComments(video_id):
    comments = []
    youtube = get_youtube()
    response1 = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        maxResults=100
    ).execute()

    for commentItem in response1['items']:
        comment = commentItem['snippet']['topLevelComment']
        author = comment['snippet']['authorDisplayName']
        text = comment['snippet']['textDisplay']
        #comments.append(commentItem)

        #selected_data = {
        #    "textOriginal": commentItem["snippet"]["topLevelComment"]["snippet"]["textOriginal"],
        #}

        #print(selected_data)
        comments.append(commentItem["snippet"]["topLevelComment"]["snippet"]["textOriginal"])
        
    return comments
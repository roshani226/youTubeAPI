from googleapiclient.discovery import build
from pprint import pprint
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# freeCodeCamp.org, Fireship
CHANNEL_ID = ['UC8butISFwT-Wl7EV0hUK0BQ', 'UCsBjURrPoezykLs9EqgamOA'] 
# Access the API key
api_key = os.getenv("USER_REQUIREMENTS_YOUTUBE_API_KEY")

def get_youtube():
    DEVELOPER_KEY = ''   # TODO: Add the key to config
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY)
    return youtube

# get the playlist id of the uploads playlist(if it exists)
def get_channel_videos(channel_id):
    youtube = get_youtube()
    response = youtube.search().list(
        part='snippet',
        type='video',
        channelId=channel_id,
        maxResults=100
    ).execute()
    return response

comments = []

for channelId in CHANNEL_ID:
    response_video_ids = get_channel_videos(channelId)

    for item in response_video_ids['items']:
        video_id = item['id']['videoId']
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

            selected_data = {
                "commentId": commentItem["id"],
                "videoId": commentItem["snippet"]["videoId"],
                "textDisplay": commentItem["snippet"]["topLevelComment"]["snippet"]["textDisplay"],
                "textOriginal": commentItem["snippet"]["topLevelComment"]["snippet"]["textOriginal"],
                "authorDisplayName": commentItem["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"],
                "authorProfileImageUrl": commentItem["snippet"]["topLevelComment"]["snippet"]["authorProfileImageUrl"],
                "authorChannelUrl": commentItem["snippet"]["topLevelComment"]["snippet"]["authorChannelUrl"],
                "authorChannelId": commentItem["snippet"]["topLevelComment"]["snippet"]["authorChannelId"]["value"],
                "canRate": commentItem["snippet"]["topLevelComment"]["snippet"]["canRate"],
                "viewerRating": commentItem["snippet"]["topLevelComment"]["snippet"]["viewerRating"],
                "likeCount": commentItem["snippet"]["topLevelComment"]["snippet"]["likeCount"],
                "publishedAt": commentItem["snippet"]["topLevelComment"]["snippet"]["publishedAt"],
                "updatedAt": commentItem["snippet"]["topLevelComment"]["snippet"]["updatedAt"],
                "canReply": commentItem["snippet"]["canReply"],
                "totalReplyCount": commentItem["snippet"]["totalReplyCount"],
                "isPublic": commentItem["snippet"]["isPublic"]
            }

            #print(selected_data)
            comments.append(selected_data)
        

with open('Data/raw_dataset.json', 'w') as json_file:
        json.dump(comments, json_file)
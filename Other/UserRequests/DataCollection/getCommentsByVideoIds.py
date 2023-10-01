import json
import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
import pandas as pd

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

#def getComments(video_ids):
#    comments = []
#    youtube = get_youtube()
#    for video_id in video_ids:
#        next_page_token = None
#        count = 0
#        while True:
#            count += 1
#            response = youtube.commentThreads().list(
#                part='snippet',
#                videoId=video_id,
#                maxResults=500,
#                pageToken=next_page_token
#            ).execute()
#
#            for commentItem in response['items']:
#                comments.append(commentItem["snippet"]["topLevelComment"]["snippet"]["textOriginal"])
#
#            next_page_token = response.get('nextPageToken')
#
#            if not next_page_token or count == 3:
#                break
#    return comments

#videoIds = [
#    "l9AzO1FMgM8",  #Java in 100 Seconds
#    "kqtD5dpn9C8",  #Python for Beginners - Learn Python in 1 Hour
#    "G3e-cpL7ofc",  #HTML & CSS Full Course - Beginner to Pro
#    "pEfrdAtAmqk",  #God-Tier Developer Roadmap
#    "XZrckLYqdys",  #Information Technology In 4 Minutes
#    "ukzFI9rgwfU",  #Machine Learning | What Is Machine Learning? | Introduction To Machine Learning | 2021 | Simplilearn
#    "pBC6DJRBzSw",  #Unsupervised Feature Selection for Machine Learning in 5 Mins
#    "9s29LKfEFjQ",  #How I would learn to code (If I could start over)
#    "L_4BPjLBF4E",  #AI Learns to Walk (deep reinforcement learning)
#    "rfscVS0vtbw",  #Learn Python - Full Course for Beginners [Tutorial]
#    "8mAITcNt710",  #Harvard CS50 – Full Computer Science University Course
#    "79pKwdiqcwI",  #FASTEST Way to Learn Coding and ACTUALLY Get a Job
#    "14BL_FwQCpM",  #Fastest Way to Learn ANY Programming Language
#    "xk4_1vDrzzo",  #Java Full Course for free ☕
#    "1sRJYuaqoiI",  #JavaScript Crash Course in 2022! Free Coding Bootcamp! #100Devs
#    "uaWYRL0g1iw",  #How to MASTER Javascript FAST in 2023
#    "u72H_zZzkcw",  #Web Development In 2023 - A Practical Guide,
#    "Sxxw3qtb3_g",  #How to OVER Engineer a Website // What is a Tech Stack?
#    "pfaSUYaSgRo",  #Ultimate Tailwind CSS Tutorial // Build a Discord-inspired Animated Navbar
#    "rL8X2mlNHPM",  #Intro to Algorithms: Crash Course Computer Science #13
#    "BBpAmxU_NQo",  #Data Structures and Algorithms for Beginners
#    "OWCao3Ul6n4",  #Data Structure and Algorithms in JAVA | Full Course on Data Structure | Great Learning
#    "un6ZyFkqFKo",  #Go Programming – Golang Course with Bonus Projects
#    "VCayKl82Lt8",  #Learn Terraform with Google Cloud Platform – Infrastructure as Code Course
#    "GFO_txvwK_c",  #JavaScript Game Development Course for Beginners
#    "ri-Bn5mGcCw",  #AWS-bootcamp project - How to deploy website on Ec2 Instance
#    "pg19Z8LL06w",  #Docker Crash Course for Absolute Beginners [NEW]
#    "lL_j7ilk7rc",  #Microservices Explained in 5 Minutes
#    "NSVmOC_5zrE",  #Game Theory 101 (#1): Introduction
#    "iILFBGm_I9M",  #ASMR Programming - Weather App With Javascript - No Talking
#    "C-EHoNfkoDM",  #FASTEST Way to Learn Web Development and ACTUALLY Get a Job
#    "M988_fsOSWo",  #Cloud Computing In 6 Minutes | What Is Cloud Computing? | Cloud Computing Explained | Simplilearn
#    "mxT233EdY5c",  #What is Cloud Computing? | Amazon Web Services
#    "gyMwXuJrbJQ",  #Learn Blockchain, Solidity, and Full Stack Web3 Development with JavaScript – 32-Hour Course
#    "EgOjklzlnFw",  #Thread Signaling in Java
#    "VcQQ1ns_qNY",  #CallbackShortcuts (Widget of the Week)
#    "nAchMctX4YA",  #Swift in 100 Seconds
#    "CwA1VWP0Ldw",  #Swift Programming Tutorial | FULL COURSE | Absolute Beginner
#    "ND44vQ5iJyc",  #Swift Closures Explained
#    "-mN3VyJuCjM",  #What Is REST API? Examples And How To Use It: Crash Course System Design #3
#]




videoIds = [
    "CpWoS8KawmY",  #Which Version is Better? Java or Bedrock? (main differences)
    "KZR_UUcOyrg",  #How to Start Coding in 2023? Learn Programming for Beginners
    "SBmSRK3feww",  #JavaScript Full Course (2023) - Beginner to Pro - Part 1
    "Ibjm2KHfymo",  #Java is mounting a huge comeback
    "zJSY8tbf_ys",  #Frontend Web Development Bootcamp Course (JavaScript, HTML, CSS)
    "p1GmFCGuVjw",  #How To Make A Website With Login And Register | HTML CSS & Javascript
    "5UT0_uS27SI",  #10 websites every developer should follow
    "vEQ8CXFWLZU",  #3 PYTHON AUTOMATION PROJECTS FOR BEGINNERS
    "4RixMPF4xis",  #AI vs Machine Learning
    "PeMlggyqz0Y",  #Machine Learning Explained in 100 Seconds
    "5C_HPTJg5ek",  #Rust in 100 Seconds
    "4sJjPswo4kM",  #Python Developer Roadmap 2023 | How To Become Python Developer | Python Developer 2023 | Simplilearn
]

def getComments(video_ids):
    comments = []
    youtube = get_youtube()
    for video_id in video_ids:
        next_page_token = None
        count = 0
        while True:
            count += 1
            response = youtube.commentThreads().list(
                part='snippet',
                videoId=video_id,
                maxResults=500,
                pageToken=next_page_token
            ).execute()

            for commentItem in response['items']:
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
                
            next_page_token = response.get('nextPageToken')

            if not next_page_token or count == 3:
                break
    return comments

comments = getComments(videoIds)
#print(comments)
print(len(comments))

comments_df = pd.DataFrame(comments, columns=["Comments"])

# Step 3: Save the DataFrame to a CSV file
csv_file_path = "Data/1/new_youtube_comments.csv"
comments_df.to_csv(csv_file_path, index=False)

print("Comments have been saved to new_youtube_comments.csv")
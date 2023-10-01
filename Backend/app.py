from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from requirementsIdentifier import identifyRequirements
import controversyKeywords_controller 
import json
import requests

app = FastAPI()

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv("USER_REQUIREMENTS_YOUTUBE_API_KEY")

# Set up CORS to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Getting the user requirements for the given video ID
@app.get('/user_requirements/')
async def analyze_comments(video_id):
    print(video_id)
    if not video_id:
        raise HTTPException(status_code=400, detail='No video ID provided')

    # Get the comments from the video ID using Data API by calling the existing methods
    requirements = identifyRequirements(video_id)
    #print(requirements)
    return {'results': requirements}

@app.get('/controversyKeywords/')
async def controversyKeywords_prediction(video_id):
    predicted_comments = controversyKeywords_controller.controversyKeywordsPrediction(video_id)
    print(predicted_comments)
    print("ava")
    predicted_json = json.dumps(predicted_comments)
    obj = {
        'predictions':predicted_json,
    }
    return obj

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='localhost',port=5000)
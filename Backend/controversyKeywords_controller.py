import pickle
import pandas as pd
import controversyKeywords_pipeline as controversyKeywords
from requirementsIdentifier import identifyRequirements
import commentGetter
import requests

def controversyKeywordsPrediction(video_id):
    predicted_dict = {}
    comments = commentGetter.getComments(video_id) 
    for comment in comments:
        print (comment)
        api_url = "https://contraversy.onrender.com/predict"
        payload = {'text': comment}
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            data = response.json()
            print(data)
            print("data")
            predicted_label = data['label']
            if predicted_label == 'Controversial' :
                print('predicted comment')
                predicted_dict[comment] =  comment
    return predicted_dict

def controversyKeywordsSearch(video_id,search):
    predicted_dict = {}
    comments = commentGetter.getComments(video_id) 
    for comment in comments:
        print (comment.lower())
        if search.lower() in comment.lower():
                predicted_dict[comment] =  comment
    print(predicted_dict)
    return predicted_dict
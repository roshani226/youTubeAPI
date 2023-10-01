import commentGetter
import joblib
import reqPreProcessComments

def identifyRequirements(video_id):
    # 1. get the comments from the video ID using Data API or scrapped comments
    comments = commentGetter.getComments(video_id) 

    # 2. preprocess the comments
    allComments, cleanedComments, tokenizedComments = reqPreProcessComments.preprocess_comments(comments)

    # Load the saved model
    vectorizer = joblib.load('req_vectorizer.joblib')
    classifier = joblib.load('req_naive_bayes_classifier_model.joblib')

    # Predict on the comments
    X = [' '.join(tokens) for tokens in tokenizedComments]
    X_vec = vectorizer.transform(cleanedComments)

    y_pred = classifier.predict(X_vec)

    identified_requirements = []
    for i in range(len(cleanedComments)):
        if y_pred[i] == 1:
            identified_requirements.append(allComments[i])
    
    return identified_requirements

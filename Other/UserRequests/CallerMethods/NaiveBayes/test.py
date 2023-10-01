import commentGetter
import joblib
import preProcessComments

# 1. get the comments from the video ID using Data API or scrapped comments
comments = commentGetter.getComments("T6L9EoBy8Zk")     # TODO: replace with the video ID from the selected video

# 2. preprocess the comments
allComments, cleanedComments, tokenizedComments = preProcessComments.preprocess_comments(comments)
print(len(comments), len(allComments), len(cleanedComments), len(tokenizedComments))

# Load the saved model
vectorizer = joblib.load('vectorizer.joblib')
classifier = joblib.load('naive_bayes_classifier_model.joblib')

# Predict on the comments
X = [' '.join(tokens) for tokens in tokenizedComments]
X_vec = vectorizer.transform(cleanedComments)

# Predict on the comments
y_pred = classifier.predict(X_vec)

identified_requirements = []
for i in range(len(cleanedComments)):
    if y_pred[i] == 1:
        identified_requirements.append(allComments[i])

print("\n\n\n")
for requirement in identified_requirements:
    print(requirement)
print("\n\n\n")
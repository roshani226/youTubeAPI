from imblearn.over_sampling import SMOTE
import joblib
import pandas as pd
import preProcessComments
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# Prepare the dataset
comments = pd.read_csv("../DataCollection/Data/2/new-youtube-comments-labeled.csv", header=0) 

# Step 1: Preprocess the comments
dataFrame, tokenizedComments = preProcessComments.preprocess_dataFrame(comments)
print(dataFrame.count())

# Prepare features and labels
X = [' '.join(tokens) for tokens in tokenizedComments]
y = dataFrame['IsRequirement']

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=38) # Accuracy: 0.9509433962264151

# Vectorize the text data
vectorizer = CountVectorizer(ngram_range=(1, 3))
X_train_vec = vectorizer.fit_transform(X_train)
X_val_vec = vectorizer.transform(X_val)

# Apply SMOTE to the training set to balance classes
smote = SMOTE(sampling_strategy='auto', random_state=48)
X_train_vec_resampled, y_train_resampled = smote.fit_resample(X_train_vec, y_train)


# Train a Naive Bayes classifier
classifier = MultinomialNB()
#classifier.fit(X_train_vec, y_train)
classifier.fit(X_train_vec_resampled, y_train_resampled)

# Save the trained model to a file
model_filename = '../CallerMethods/NaiveBayes/naive_bayes_classifier_model.joblib'
joblib.dump(classifier, model_filename)
joblib.dump(vectorizer, '../CallerMethods/NaiveBayes/vectorizer.joblib')

# Predict on the validation set
y_pred = classifier.predict(X_val_vec)

# Evaluate the model
print(classification_report(y_val, y_pred))

# Calculate and print the accuracy
accuracy = accuracy_score(y_val, y_pred)
print("Accuracy:", accuracy)



# Save the accuracy to a file for selecting the best parameters
#accuracyForRandomState = []
#for i in range(90):
#    for j in range(90):
#        # Split the data into training and validation sets
#        X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=i)
#
#        # Vectorize the text data
#        vectorizer = CountVectorizer(ngram_range=(1, 4))
#        X_train_vec = vectorizer.fit_transform(X_train)
#        X_val_vec = vectorizer.transform(X_val)
#
#        # Apply SMOTE to the training set
#        smote = SMOTE(sampling_strategy='auto', random_state=j)
#        X_train_vec_resampled, y_train_resampled = smote.fit_resample(X_train_vec, y_train)
#
#        # Train a Naive Bayes classifier
#        classifier = MultinomialNB()
#        #classifier.fit(X_train_vec, y_train)
#        classifier.fit(X_train_vec_resampled, y_train_resampled)
#
#        # Predict on the validation set
#        y_pred = classifier.predict(X_val_vec)
#
#        # Evaluate the model
#        #print(classification_report(y_val, y_pred))
#
#        # Calculate and print the accuracy
#        accuracy = accuracy_score(y_val, y_pred)
#        #print("Accuracy:", accuracy)
#
#        accuracyForRandomState.append(str(i) + " - " + str(j) + " - " + str(accuracy) + " - \n" + classification_report(y_val, y_pred))
#
#df = pd.DataFrame({'accuracyForRandomState': accuracyForRandomState})
#df.to_csv('randomStateComparison.txt', header=False, index=False, sep=' ', mode='a')
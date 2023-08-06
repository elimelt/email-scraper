import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Load JSON data containing parsed emails
with open('parsed.json', 'r') as json_file:
    emails_data = json.load(json_file)

# Prepare data for classification
features = []  # List to store text features
labels = []    # List to store labels (e.g., "internship" or "non-internship")

for email in emails_data:
    if 'parsed' in email and email['parsed'].strip():
        text_content = email['parsed']
        features.append(text_content)
        # Add the label for each email (you need to set the labels based on your data)
        labels.append("internship" if "internship" in email['subject'].lower() else "non-internship")

# Vectorize the text using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(features)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(tfidf_matrix, labels, test_size=0.2, random_state=42)

# Choose and train a classifier (Naive Bayes in this example)
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = classifier.predict(X_test)

# Evaluate the classifier
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print(f"Classification Report:\n{report}")


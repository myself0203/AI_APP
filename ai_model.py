from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


# Training data
texts = [
    "I love this application",
    "This is excellent",
    "I am very happy",
    "The service is wonderful",
    "This product is amazing",
    "I hate this application",
    "This is terrible",
    "I am very disappointed",
    "The service is bad",
    "This product is horrible",
    "It is okay",
    "The service is average",
    "This is fine",
    "Nothing special",
    "It is acceptable"
]

labels = [
    "Positive",
    "Positive",
    "Positive",
    "Positive",
    "Positive",
    "Negative",
    "Negative",
    "Negative",
    "Negative",
    "Negative",
    "Neutral",
    "Neutral",
    "Neutral",
    "Neutral",
    "Neutral"
]


# Convert text into numerical features
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(texts)


# Create the AI classifier
model = LogisticRegression()

model.fit(X, labels)


def predict_sentiment(text):
    """
    Predict the sentiment of a new text.
    """

    text_vector = vectorizer.transform([text])

    prediction = model.predict(text_vector)[0]

    probabilities = model.predict_proba(text_vector)[0]

    confidence = max(probabilities) * 100

    return prediction, round(confidence, 2)

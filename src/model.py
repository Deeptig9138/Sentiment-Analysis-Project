import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.feature_extraction.text import TfidfVectorizer

def load_data(file_path):
    # Load the preprocessed data
    data = pd.read_csv(file_path)
    return data

def sentiment_distribution(data):
    # Count the sentiment values (Positive vs Negative)
    sentiment_count = data['Sentiment'].value_counts()
    
    # Plot the sentiment distribution
    plt.figure(figsize=(6, 4))
    sns.barplot(x=sentiment_count.index, y=sentiment_count.values, palette='viridis')
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.show()

def train_sentiment_model(data):
    # TF-IDF Vectorizer to convert text data into numerical format
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(data['Text'])
    y = data['Sentiment'].apply(lambda x: 1 if x == 'Positive' else 0)  # Binary encoding for sentiment

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the Logistic Regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Predict on the test set
    y_pred = model.predict(X_test)

    # Print evaluation metrics
    print("Model Accuracy:", model.score(X_test, y_test))
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    # Cross-validation score
    cv_score = cross_val_score(model, X, y, cv=5)
    print(f"\nCross-validation Accuracy: {cv_score.mean()}")

# File path for the preprocessed data
file_path = 'data/preprocessed_reviews.csv'

# Load data and plot sentiment distribution
data = load_data(file_path)
sentiment_distribution(data)

# Train and evaluate the sentiment model
train_sentiment_model(data)
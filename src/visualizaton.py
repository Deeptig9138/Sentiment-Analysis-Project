import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

def load_data(file_path):
    # Load the preprocessed data
    data = pd.read_csv(file_path)
    return data

def plot_sentiment_distribution(data):
    # Count the sentiment values (Positive vs Negative)
    sentiment_count = data['Sentiment'].value_counts()

    # Plot the sentiment distribution
    plt.figure(figsize=(6, 4))
    sns.barplot(x=sentiment_count.index, y=sentiment_count.values, palette='viridis')
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.show()

def plot_wordcloud(data):
    # Combine all text reviews for word cloud generation
    text = ' '.join(data['Text'])
    
    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    
    # Plot the word cloud
    plt.figure(figsize=(8, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

def plot_sentiment_over_time(data):
    # If there's a 'Date' column, plot sentiment over time
    if 'Date' in data.columns:
        data['Date'] = pd.to_datetime(data['Date'])
        data['YearMonth'] = data['Date'].dt.to_period('M')
        sentiment_time = data.groupby('YearMonth')['Sentiment'].value_counts().unstack().fillna(0)
        
        # Plot the sentiment over time
        sentiment_time.plot(kind='line', figsize=(10, 6))
        plt.title('Sentiment Over Time')
        plt.xlabel('Month')
        plt.ylabel('Count')
        plt.show()

# File path for the preprocessed data
file_path = 'data/preprocessed_reviews.csv'

# Load data and plot sentiment distribution and word cloud
data = load_data(file_path)
plot_sentiment_distribution(data)
plot_wordcloud(data)
plot_sentiment_over_time(data)  # Only works if there's a 'Date' column
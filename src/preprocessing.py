import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK resources
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Initialize lemmatizer and stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Function to clean the text data
def clean_text(text):
    if pd.isnull(text):
        return ""
    # Remove non-alphabetic characters and lower the text
    text = re.sub(r'[^a-zAZA-Za-z\s]', '', str(text))
    text = text.lower()  # Convert to lowercase

    # Lemmatization and stopword removal
    words = text.split()
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    return ' '.join(words)

def preprocess_data(input_file, output_file):
    try:
        # Load dataset
        data = pd.read_csv(input_file)
        print(f"Loaded data from {input_file}")
        
        # Check if 'Text' and 'Score' columns exist
        print(f"Columns found: {data.columns}")
        if 'Text' not in data.columns or 'Score' not in data.columns:
            print("Error: 'Text' or 'Score' columns not found in the input file.")
            return
        
        # Clean the 'Text' column
        print("Cleaning 'Text' column...")
        data['Text'] = data['Text'].apply(clean_text)
        
        # Create sentiment labels based on 'Score' column
        print("Creating 'Sentiment' column...")
        data['Sentiment'] = data['Score'].apply(lambda x: 'Positive' if x >= 3 else 'Negative')

        print(f"Processed data: {data.head()}")  # Print the first few rows to confirm the changes

        # Save the preprocessed data to a new file
        data.to_csv(output_file, index=False)
        print(f"Data has been preprocessed and saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: The file {input_file} is empty.")
    except Exception as e:
        print(f"An error occurred: {e}")

# File paths
input_file = 'data/Reviews.csv'
output_file = 'data/preprocessed_reviews.csv'

# Run preprocessing
preprocess_data(input_file, output_file)
# 📊 Sentiment Analysis Project  
This project is a **Sentiment Analysis** system built using Python. It processes and analyzes customer reviews to determine their sentiment (Positive/Negative) while providing visual insights and machine learning predictions.  

---

## ✨ Features  

- **Data Preprocessing**  
  - Clean text data using NLP techniques like lemmatization and stopword removal.  
  - Generate sentiment labels based on review scores.  

- **Data Visualization**  
  - Sentiment distribution analysis.  
  - Generate word clouds of frequent terms.  
  - Sentiment trends over time (if the dataset includes a `Date` column).  

- **Machine Learning Model**  
  - Train a Logistic Regression model to classify sentiment.  
  - Evaluate with confusion matrices, classification reports, and cross-validation scores.  

---

## 📂 File Structure  

```
Sentiment-Analysis-Project
├── assets/                      # Folder for images used in README  
│   ├── prprocessing.png  
│   ├── visualization.png  
│   ├── result.png  
├── data/  
│   ├── Reviews.csv                # Input dataset  
│   ├── preprocessed_reviews.csv   # Preprocessed dataset  
├── src/  
│   ├── preprocessing.py           # Script for data preprocessing  
│   ├── visualization.py           # Script for data visualization  
│   ├── model.py                   # Script for machine learning model  
├── README.md                      # Project documentation  
```

---

## 🛠️ Requirements
Install all necessary dependencies using:
```
pip install -r requirements.txt
```

## Key Dependencies
- pandas
- nltk
- matplotlib
- seaborn
- wordcloud
- scikit-learn

---

## 🚀 Usage

1️⃣ Data Preprocessing
Clean and preprocess the dataset using:
```
python src/preprocessing.py
```

![Preprocessing](https://github.com/Deeptig9138/Sentiment-Analysis-Project/blob/main/assets/preprocessing.png)

2️⃣ Data Visualization
Generate visual insights using:
```
python src/visualization.py
```

![Visualization](https://github.com/Deeptig9138/Sentiment-Analysis-Project/blob/main/assets/visualization.png)

3️⃣ Model Training
Train and evaluate the sentiment classification model using:
```
python src/model.py
```

---

📈 Results
Sentiment Over Time
Trends over time based on the Date column:

![Result](https://github.com/Deeptig9138/Sentiment-Analysis-Project/blob/main/assets/result.png)

---

## 📊 Dataset
Ensure the dataset (Reviews.csv) is in the data/ directory.

Minimum required columns:
1) Text - Customer reviews.
2) Score - Ratings for the reviews.

---

## 🤝 Contributing
I welcome contributions! To contribute:

1) Fork the repository.
   
2) Create a new branch:
   ```
   git checkout -b feature-branch
   ```
   
3) Commit your changes:
   ```
   git commit -m "Add a new feature"
   ```
   
4) Push to your branch:
   ```
   git push origin feature-branch
   ```
   
5) Submit a Pull Request.

---

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

---

👤 Author :
Deepti Gupta
- [GitHub Profile](https://github.com/Deeptig9138)

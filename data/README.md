# 📂 Data Directory  
This folder is intended to hold the dataset files required for the **Sentiment Analysis Project**. However, due to size constraints, the dataset files are not included in this repository.  

---

## 📥 Download the Dataset  

Please download the dataset from the following link:  
[Download Reviews.csv](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews?resource=download)

---

## 🛠️ Instructions  

### 1️⃣ Save the Dataset  
After downloading the dataset: 

- Place the **`Reviews.csv`** file in the `data/` directory of the project.  
  ```
  Sentiment-Analysis-Project  
  ├── data/  
  │   ├── Reviews.csv  
  │   └── preprocessed_reviews.csv (will be generated after running preprocessing.py)
  ```

### 2️⃣ Update the File Path
If you choose to save the dataset in a different location, update the file path in the preprocessing.py script:
```
# Update the input_file variable with your file path
input_file = '/path/to/your/Reviews.csv'
```

---

## 🏃 Steps to Process the Dataset
1) Preprocessing
Run the preprocessing.py file to clean and process the dataset:
```
python src/preprocessing.py
```

Output: A preprocessed_reviews.csv file will be generated in the data/ directory.

2) Visualization
Run the visualization.py file to explore and visualize the processed data:
```
python src/visualization.py
```

---

## 📜 Notes
Dataset Requirements:
Ensure the dataset includes the following columns:
- Text: The text of customer reviews.
- Score: Numerical ratings associated with each review.

Generated Files:

Preprocessed data will be saved as preprocessed_reviews.csv in the data/ folder.
If the preprocessing.py script doesn't run correctly, double-check the dataset's format and update its path if necessary.

---

🔗 Related Resources

Main Project README

---

⚠️ Reminder

The dataset is a critical part of this project. Without the proper Reviews.csv, the scripts for preprocessing, visualization, and modeling will not function correctly.

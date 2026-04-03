# Multiclass Spam and Phishing Message Detection using NLP and Machine Learning

## 📌 Project Overview


This project presents a Natural Language Processing (NLP) and Machine Learning based system for classifying messages into three categories: Ham (normal messages), Spam (promotional or unwanted messages), and Phishing (fraudulent or scam messages). The system uses text preprocessing, TF-IDF feature extraction, and Logistic Regression for multiclass classification, and is deployed using a Streamlit web application () for real-time message prediction.

---

## 🎯 Problem Statement

Spam and phishing messages are increasingly common in emails, SMS, and messaging platforms.
The goal of this project is to build a machine learning model that can automatically classify messages into **Ham, Spam, or Phishing** to improve communication security and filtering systems.

---

## 🧠 Solution Approach

The solution follows a standard NLP and Machine Learning workflow:

1. Collect multiple spam and phishing datasets
2. Clean and preprocess text data
3. Remove punctuation and stopwords
4. Convert text into numerical features using **TF-IDF Vectorization**
5. Split dataset into training and testing sets
6. Train a **Logistic Regression** classifier
7. Evaluate model performance using classification metrics
8. Save the trained model and vectorizer
9. Deploy the model using **Streamlit Web App**

---

## ⚙️ Machine Learning Pipeline

```
Raw Dataset
     ↓
Text Cleaning & Preprocessing
     ↓
Stopword Removal
     ↓
TF-IDF Vectorization
     ↓
Train/Test Split
     ↓
Logistic Regression Model
     ↓
Model Evaluation
     ↓
Model Saved (.pkl)
     ↓
Streamlit App Deployment
```

---

## 📊 Model Performance

**Final Model Accuracy:** `95.8%`

### Classification Report Summary

| Class | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Ham   | 0.99      | 0.98   | 0.98     |
| Spam  | 0.97      | 0.96   | 0.97     |
| Phish | 0.87      | 0.90   | 0.88     |

The model performs strongly across all classes, with **high recall for phishing detection**, which is important for security-related applications.

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* NLTK
* Scikit-learn
* TF-IDF Vectorizer
* Logistic Regression
* Streamlit
* Pickle

---

## 📁 Project Structure

```
Spam_mail_classification/
│
├── app.py
├── train.py
├── requirements.txt
├── README.md
│
├── data/
│   └── final_dataset.csv
│
├── models/
│   ├── spam_model.pkl
│   └── vectorizer.pkl
│
├── assets/
│   ├── app_ui.png
│   └── confusion_matrix.png
│
└── .gitignore
```

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```
git clone https://github.com/your-username/spam-phishing-classifier.git
cd spam-phishing-classifier
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Train the Model

```
python train.py
```

### 4. Run the Streamlit App

```
streamlit run app.py
```

---

## 💡 Example Predictions

| Message                                         | Prediction |
| ----------------------------------------------- | ---------- |
| "Congratulations! You won a free iPhone"        | Spam       |
| "Let's meet tomorrow at 5 PM"                   | Ham        |
| "Verify your bank account password immediately" | Phishing   |

---

## 📈 Future Improvements

* Use Deep Learning models (LSTM / BERT)
* Add email header analysis
* URL feature extraction for phishing detection
* Deploy as REST API
* Docker container deployment
* Model comparison with Random Forest and Naive Bayes

---

## 👨‍💻 Author

Machine Learning Project – Spam & Phishing Detection System

---

## 📜 License

This project is open-source and available for educational and research purposes.

# 📧 Multiclass Spam and Phishing Message Detection using NLP and Machine Learning

## 📌 Project Overview

This project implements a **multiclass text classification system** to classify messages into:

* **Ham (Normal messages)**
* **Spam (Unwanted/Promotional messages)**
* **Phishing (Fraudulent/Scam messages)**

The system uses **Natural Language Processing (NLP)** techniques and **Machine Learning** to preprocess text, extract features using TF-IDF, and classify messages using a Logistic Regression model. A **Streamlit web application** is also developed for real-time predictions.

---

## 🎯 Problem Statement

Spam and phishing messages pose significant risks in communication systems. This project aims to build a robust machine learning model that can automatically detect and classify such messages to improve security and filtering systems.

---

## 🧠 Solution Approach

The project follows a complete NLP pipeline:

* Data collection from multiple sources
* Text preprocessing (cleaning, stopword removal)
* Feature extraction using TF-IDF
* Model training using Logistic Regression
* Model evaluation using classification metrics
* Model deployment using Streamlit

---

## ⚙️ Machine Learning Pipeline

```
Raw Data → Preprocessing → TF-IDF → Model Training → Evaluation → Model Saving → Deployment
```

---

## 📊 Model Performance

* **Accuracy:** ~95.8%

| Class    | Precision | Recall | F1-Score |
| -------- | --------- | ------ | -------- |
| Ham      | 0.99      | 0.98   | 0.98     |
| Spam     | 0.97      | 0.96   | 0.97     |
| Phishing | 0.87      | 0.90   | 0.88     |

The model achieves strong performance across all classes with effective phishing detection.

---

## 🔗 Project Resources (Kaggle Integration)

* 📊 **Dataset:**
  [https://kaggle.com/your-dataset-link](https://www.kaggle.com/datasets/dharshiyanacc/spam-ham-and-phishing-message-dataset-for-nlp)

* 🤖 **Trained Model:**
  [https://kaggle.com/your-model-link](https://www.kaggle.com/models/dharshiyanacc/multiclass-spam-and-phishing-detection)

* 📒 **Training Notebook:**
 [https://kaggle.com/your-notebook-link](https://www.kaggle.com/code/dharshiyanacc/spam-ham-phishing-classification)

These resources ensure full reproducibility of the project.

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

---

## 📁 Project Structure

```
spam-phishing-detection/
│
├── app.py
├── train.py
├── requirements.txt
├── README.md
│
├── models/
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── data/
│   └── dataset_sample.csv
│
├── assets/
│   └── confusion_matrix.png
│
└── .gitignore
```

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/spam-phishing-detection.git
cd spam-phishing-detection
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the Application

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

* Implement deep learning models (LSTM / BERT)
* Add URL-based phishing detection features
* Improve dataset balance
* Deploy API using Flask or FastAPI
* Dockerize the application

---

## 👨‍💻 Author

Machine Learning Project – Spam & Phishing Detection System

---

## 📜 License

This project is open-source and available for educational purposes.

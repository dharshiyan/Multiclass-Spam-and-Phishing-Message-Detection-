import streamlit as st
import pickle
import re
import string
from nltk.corpus import stopwords

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

stop_words = set(stopwords.words('english'))

# Text preprocessing
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = "".join(char for char in text if char not in string.punctuation)
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

# Label mapping
label_map = {
    0: "Ham (Normal Message)",
    1: "Spam Message",
    2: "Phishing Message"
}

# Prediction function
def predict_message(text):
    processed_text = preprocess_text(text)
    vector = vectorizer.transform([processed_text])
    prediction = model.predict(vector)[0]
    return label_map[prediction]

# Streamlit UI
st.set_page_config(page_title="Spam / Phish Detector", layout="centered")

st.title("📧 Spam / Ham / Phishing Message Classifier")
st.write("Enter a message to classify whether it is Spam, Ham, or Phishing.")

user_input = st.text_area("Enter Message")

if st.button("Predict"):
    if user_input.strip() != "":
        result = predict_message(user_input)
        
        if "Phishing" in result:
            st.error("⚠️ " + result)
        elif "Spam" in result:
            st.warning("📢 " + result)
        else:
            st.success("✅ " + result)
    else:
        st.write("Please enter a message.")

st.write("---")
st.write("Model: TF-IDF + Logistic Regression")
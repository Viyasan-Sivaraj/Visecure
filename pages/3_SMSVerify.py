import streamlit as st
import pickle
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
nltk.download('stopwords')
import re
from sklearn.feature_extraction.text import CountVectorizer

# Load Pickle files
with open("Spam_sms_prediction.pkl", 'rb') as model_file:
    classifier = pickle.load(model_file)

with open("corpus.pkl", 'rb') as corpus_file:
    corpus = pickle.load(corpus_file)

# Create the Bag of Words model
cv = CountVectorizer(max_features=2500)
X = cv.fit_transform(corpus).toarray()

def predict_spam(sample_message):
    sample_message = re.sub(pattern='[^a-zA-Z]', repl=' ', string=sample_message)
    sample_message = sample_message.lower()
    sample_message_words = sample_message.split()
    sample_message_words = [word for word in sample_message_words if not word in set(stopwords.words('english'))]
    ps = PorterStemmer()
    final_message = [ps.stem(word) for word in sample_message_words]
    final_message = ' '.join(final_message)
    temp = cv.transform([final_message]).toarray()
    return classifier.predict(temp)

def main():
    st.title(":blue[Spam] SMS Detection")

    message = st.text_area("Enter a message:")
    if st.button("Analyse"):
        if not message == "":
            if predict_spam(message):
                st.error("Predicted Result: Spam 🚨")
            else:
                st.success("Predicted Result: Not Spam✅")
        else:
            st.write("Please enter a message")

if __name__ == '__main__':
    main()

c31,c11,c12 = st.columns([3,1,5])
c11.image("logo.png", width=200)


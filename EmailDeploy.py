import streamlit as st
import pickle
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string

# nltk.download()


stops = stopwords.words('english')
punct = list(string.punctuation)
ps = PorterStemmer()

Model = pickle.load(open("EmailModel.pkl", 'rb'))
Vector = pickle.load(open("TfidfEmail.pkl", 'rb'))

print(Model)
print(Vector)

def stream():
    st.title('EMAIL/MSG SPAM CLASSIFICATION')
    intro = 'DEVELOPED IN PYTHON BY "ATIF"'
    st.header(intro) 


    email = st.text_input('Enter Your Email/Message')

    but = st.button('CHECK')
    if but:
        waste = []
        youlist = word_tokenize(email)
        for i in youlist:
            if i in stops or i in punct:
                youlist.remove(i)
                waste.append(i)
        for i,j in enumerate(youlist):
            youlist[i] = ps.stem(j)

        final_msg = [' '.join(youlist)]
        Email = Vector.transform(final_msg)
        Prediction = Model.predict(Email)
        if Prediction == 1: 
            output = "It's a HAM Mail"
            st.success(output)
            
        elif Prediction == 0:
            output2 = "It's a SPAM Mail"
            st.error(output2)
          

stream()
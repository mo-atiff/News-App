import streamlit as st
import pickle
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 180)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('DEVELOPED USING PYTHON BY "ATIF"')
# engine.runAndWait()

def voice(n):
    engine.say(n)
    engine.runAndWait()

Model = pickle.load(open('Model.pkl', 'rb'))
Vector = pickle.load(open('TfVector.pkl', 'rb'))

print(Model)
print(Vector)

def stream():
    st.title('EMAIL SPAM CLASSIFICATION')
    intro = 'DEVELOPED USING PYTHON BY "ATIF"'
    st.header(intro)

    email = st.text_input('Enter Your Email')
    but = st.button('CHECK')
    if but:
        email = [email]
        Email = Vector.transform(email)
        Prediction = Model.predict(Email)
        print('Iam here')
        if Prediction == 1:
            output = "It's a HAM Mail"
            st.success(output)
            # voice(output)
        elif Prediction == 0:
            output2 = "It's a SPAM Mail"
            st.error(output2)
            # voice(output2)
stream()
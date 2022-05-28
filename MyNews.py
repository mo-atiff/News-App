import streamlit as st
from datetime import date
from PIL import Image
from io import BytesIO
from datetime import datetime

import requests
title = []

def stream():
    col1, col2, col3, col4 = st.columns(4)

    lsp = date.today()
    now = datetime.now()

    current_time = now.strftime("%I:%M:%S  %p")
    with col1:
        st.write(lsp)
    with col4:
        st.write(current_time)
    st.title('UNBIASED MEDIA REPORTS BY ATIF')
    intro = 'SOURCE --> GOOGLE || MADE WITH ❤️ BY ATIF'
    st.header(intro) 

    user = st.text_input('SEARCH FOR ANY CATEGORY/COUNTRY NEWS', '')
    user = user.lower()
    news = st.button('GET NEWS')

    if news:
        if len(user) !=0 and user!='israel':
            global j
            j=0
            url = 'https://newsapi.org/v2/everything?q={}&apiKey=10ff4a17b12d4f0e9eccba7663d332b4'.format(user)
            req = requests.get(url).json()
            impdata = req['articles']
            imageurl = [] 
            media = []
            title = []
            description = []
            url = []
            author = [] 
            dates = []

            Newspackets = []

            for i in impdata:
                imageurl.append(i['urlToImage'])
                media.append(i['source']['name'])
                title.append(i['title'])
                description.append(i['description'])
                url.append(i['url'])
                author.append(i['author'])
                dates.append(i['publishedAt'].split('T')[0])

            for i in range(len(url)):
                Newspackets.append([imageurl[j], media[j], title[j], description[j], url[j], author[j], dates[j]])
                j+=1
            for i in Newspackets:
                    response = requests.get(i[0])
                    img = Image.open(BytesIO(response.content))
                    st.image(img, 'Reference', width=500)
                    st.write("NEWS SOURCE : ", i[1])
                    st.subheader(i[2])
                    st.write(i[3])
                    st.write('FOR MORE DETAILS : ', i[4])
                    st.write("AUTHOR : ", i[5])
                    st.write('DATE TIME : ', i[6])
                    st.text('')
                    st.text('')
                    st.text('')
                    st.text('')
                    st.write('')
            st.subheader("THAT'S IT FOR NOW")
            st.subheader("THANKS FOR VISITING US")

        elif user == 'israel':
            st.subheader("DID YOU MEAN PALESTINE")
            st.subheader('DEAR USER PLEASE TYPE "OCCUPIED PALESTINE" TO GET ISRAEL NEWS')
            jerusalem = Image.open('jerusalem_News-Logo.jpg')
            st.image(jerusalem, 'PALESTINE WILL BE FREE')


        elif user == 'occupied palestine':
            global q
            q=0
            url = 'https://newsapi.org/v2/everything?q={}&apiKey=10ff4a17b12d4f0e9eccba7663d332b4'.format(user)
            req = requests.get(url).json()
            impdata = req['articles']
            imageurl = [] 
            media = []
            title = []
            description = []
            url = []
            author = [] 
            dates = []

            Newspackets = []

            for i in impdata:
                imageurl.append(i['urlToImage'])
                media.append(i['source']['name'])
                title.append(i['title'])
                description.append(i['description'])
                url.append(i['url'])
                author.append(i['author'])
                dates.append(i['publishedAt'].split('T')[0])

            for i in range(len(url)):
                Newspackets.append([imageurl[q], media[j], title[j], description[j], url[j], author[j], dates[j]])
                j+=1
            for i in Newspackets:
                    response = requests.get(i[0])
                    img = Image.open(BytesIO(response.content))
                    st.image(img, 'Reference', width=500)
                    st.write("NEWS SOURCE : ", i[1])
                    st.subheader(i[2])
                    st.write(i[3])
                    st.write('FOR MORE DETAILS : ', i[4])
                    st.write("AUTHOR : ", i[5])
                    st.write('DATE TIME : ', i[6])
                    st.text('')
                    st.text('')
                    st.text('')
                    st.text('')
                    st.write('')
            st.subheader("THAT'S IT FOR NOW")
            st.subheader("THANKS FOR VISITING US")

        elif len(user) == 0:
            st.write('Enter Something...')

        else:
            st.write('Sorry We Have Nothing To Show On This')
stream()
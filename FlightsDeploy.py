import streamlit as st
import pickle
import datetime
import numpy as np  

Model = pickle.load(open("Flights.pkl", 'rb'))

def stream():
    st.title('FLIGHT TICKET PRICE PREDICTION')
    intro = 'DEVELOPED BY "ATIF"'
    st.header(intro)

    lsp = datetime.datetime.now()

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    col5, col6 = st.columns(2)
    fake1, col7, fake2 = st.columns(3)

    with col1:
        calender = st.date_input("DEPARTURE DATE",datetime.date(lsp.year, lsp.month, lsp.day))
        st.write(f'DEPARTURE DATE : {calender}')

    with col2:
        time = st.time_input('DEPARTURE TIME', datetime.time(lsp.hour, lsp.minute))
        time = str(time)
        t = datetime.datetime.strptime(time, "%H:%M:%S")
        t = t.strftime("%I:%M %p")
        st.write('DEPARTURE TIME : ', t)
        time2 = datetime.datetime.strptime(time, "%H:%M:%S")    

    with col3:
        src = st.selectbox('FROM(SOURCE)', ['Chennai', 'Delhi', 'Kolkata', 'Mumbai'])
        st.write(f'SOURCE : {src}')

    with col4:
        dest = st.selectbox('TO(DESTINATION)', ['Cochin', 'Delhi', 'Hyderabad', 'Kolkata', 'New Delhi'])
        st.write(f'DESTINATION : {dest}')

    with col5:
        via = st.selectbox('VIA(FLIGHT)', ['Air India', 'GoAir', 'IndiGo', 'Jet Airways', 'Jet Airways Business', 'Multiple carriers', 'Multiple carriers Premium economy', 'SpiceJet', 'Trujet', 'Vistara', 'Vistara Premium economy'])
        st.write(f'DESTINATION : {via}')

    with col6:
        stops = st.selectbox('STOPS', [0, 1, 2, 3, 4])
        st.write(f'DESTINATION : {stops}')

    with col7:
        y_pred = st.button('PREDICT')
        if y_pred:
            Day = calender.day
            Month = calender.month
            Stops = stops
            Plane = via
            Dest = dest
            Src = src
            Dep_hour = time2.hour
            Dep_min = time2.minute

            # st.write(Day, Month, Stops, Plane, Dest, Src, Dep_hour, Dep_min)
            # order : [via, src, dest, day, month, stops, depH, depM]

            lst = ['Air India', 'GoAir', 'IndiGo', 'Jet Airways', 'Jet Airways Business', 'Multiple carriers', 
                   'Multiple carriers Premium economy', 'SpiceJet', 'Trujet', 'Vistara', 'Vistara Premium economy', 'Chennai', 'Delhi', 'Kolkata', 'Mumbai',
                   'Cochin', 'Delhi', 'Hyderabad', 'Kolkata', 'New Delhi', Day, Month, Stops, Dep_hour, Dep_min]

            planeind = lst.index(Plane)
            srcind = lst.index(Src)
            destind = lst.index(Dest)
            print(planeind)

            lst[planeind] = 1
            lst[srcind] = 1
            lst[destind] = 1


            for i in range(20):
                if i == planeind or i == srcind or i == destind:
                    pass
                else:
                    lst[i] = 0

            lst = [lst]
            Predict = Model.predict(lst)
            Predict = np.round_(Predict)
            Predict = list(Predict)
            for i in Predict:
                st.write(f'YOUR TICKET FARE COULD BE : ₹ {i}')


stream()
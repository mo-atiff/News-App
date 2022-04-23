import streamlit as st
import datetime

lsp = datetime.datetime.now()
calender = st.date_input("Departure Date",datetime.date(lsp.year, lsp.month, lsp.day))
st.write(f'Depart : {calender}')


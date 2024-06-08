import streamlit as st

st.title('Weather Forecast for the Next Days')


place = st.text_input('Place:', key='place')

days = st.slider('Forecast Days:', 1, 5, 1, key='days', help='Select the number of days you want to forecast')

option = st.selectbox('Select data to view:', ('Temperature', 'Sky'), key='option')

st.subheader(f'{option} for the next {days} days in {place}')
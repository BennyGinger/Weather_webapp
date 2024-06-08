import streamlit as st
import plotly.express as px

st.title('Weather Forecast for the Next Days')


place = st.text_input('Place:', key='place')

days = st.slider('Forecast Days:', 1, 5, 1, key='days', help='Select the number of days you want to forecast')

option = st.selectbox('Select data to view:', ('Temperature', 'Sky'), key='option')

st.subheader(f'{option} for the next {days} days in {place}')

def get_data(days):
    dates = ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05', '2021-01-06']
    temperature = [3,5,2,5,1,6]
    return dates[:days+1], temperature[:days+1]

dates,temperature = get_data(days)
figure = px.line(x=dates, y=temperature, labels={'x': 'Date', 'y': 'Temperature (C)'})
                 
st.plotly_chart(figure)
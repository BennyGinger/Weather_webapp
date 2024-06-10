import streamlit as st
import plotly.express as px
from backend import get_data

# Build the app
st.title('Weather Forecast for the Next Days')

place = st.text_input('Place:', key='place', value='Budapest')

days = st.slider(label='Forecast Days:', min_value=1, max_value=5, value=1, key='days', help='Select the number of days you want to forecast')

option = st.selectbox('Select data to view:', ('Temperature', 'Sky'), key='option')

st.subheader(f'{option} for the next {days} days in {place}')


# Get data


data = get_data(place, days)

if option == 'Temperature':
    dates = [x['dt_txt'] for x in data]
    temperature = [round(x['main']['temp']/10,ndigits=1) for x in data]
    figure = px.line(x=dates, y=temperature, labels={'x': 'Date', 'y': 'Temperature (C)'})               
    st.plotly_chart(figure)

else:
    images_map = {'Clear':'/home/Weather_webapp/images/clear.png', 'Clouds':'/home/Weather_webapp/images/cloud.png','Rain':'/home/Weather_webapp/images/rain.png','Snow':'/home/Weather_webapp/images/snow.png'}
    
    sky_condition = [x['weather'][0]['main'] for x in data]
    sky_condition = [images_map[x] for x in sky_condition]
    dates = [x['dt_txt'] for x in data]
    st.image(image=sky_condition, caption=dates, width=80, use_column_width=False)
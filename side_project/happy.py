import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.title("In Search for Happiness")
data = pd.read_csv('happy.csv')

x_axis = st.selectbox("Select data for the X-axix:", ('gdp', 'happiness', 'social_support', 'life_expectancy', 'freedom_to_make_life_choices', 'generosity', 'corruption'), key='x_axis',)

y_axis = st.selectbox("Select data for the Y-axix:", ('gdp', 'happiness', 'social_support', 'life_expectancy', 'freedom_to_make_life_choices', 'generosity', 'corruption'), key='y_axis',)

country = st.selectbox("Select a Country:", key='country', options=["None"]+list(data['country']))

st.subheader(f"Comparing {x_axis} and {y_axis}")


# fig = px.scatter(data, x=x_axis, y=y_axis, labels={'x': x_axis, 'y': y_axis}, hover_data=['country'])
# st.plotly_chart(fig)
fig = go.Figure()

# Add scatter plot for all countries
fig.add_trace(go.Scatter(x=data[data['country'] != country][x_axis], 
                         y=data[data['country'] != country][y_axis], 
                         mode='markers', 
                         marker_color='blue',
                         hovertemplate = "<b>Country</b>: %{text}<br><b>"+x_axis+"</b>: %{x}<br><b>"+y_axis+"</b>: %{y}<extra></extra>",
                         text = data[data['country'] != country]['country'].tolist()))

# Add scatter plot for selected country
if country != "None":
    fig.add_trace(go.Scatter(x=data[data['country'] == country][x_axis], 
                             y=data[data['country'] == country][y_axis], 
                             mode='markers', 
                             marker_color='red',
                             hovertemplate = "<b>Country</b>: %{text}<br><b>"+x_axis+"</b>: %{x}<br><b>"+y_axis+"</b>: %{y}<extra></extra>",
                             text = data[data['country'] == country]['country'].tolist()))

fig.update_layout(xaxis_title=x_axis, yaxis_title=y_axis,showlegend=False)

st.plotly_chart(fig)
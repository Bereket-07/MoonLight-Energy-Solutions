import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# import plotly.express as px

@st.cache_data
def load_data():
    data = pd.read_csv('../../data/benin-malanville.csv')
    return data
data = load_data()
st.write(data.head()) #display the first few rows of the dataset

st.sidebar.header('Filter Data')
start_date = st.sidebar.date_input('start Date', pd.to_datetime('2023-01-01'))
end_date = st.sidebar.date_input('End Date', pd.to_datetime('2023-12-31'))
# Convert start_date and end_date to datetime64[ns]
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

filtered_date = data[(pd.to_datetime(data['Timestamp']) >= start_date) & (pd.to_datetime(data['Timestamp']) <= end_date)]
# display the filtered data
st.write(filtered_date)


st.header('Line Plot Example')
plt.figure(figsize=(10,4))
plt.plot(filtered_date['Timestamp'],filtered_date['GHI'])
plt.xlabel('Data')
plt.xlabel('Date')
plt.ylabel('GHI')
plt.title('GHI over Tinme')
st.pyplot(plt)

# st.header('Interactive Plotly Example')
# fig = px.line(filtered_date, x='date', y='GHI', title='GHI Over Time')
# st.plotly_chart(fig)



st.sidebar.header('Customize Visualization')
value_range = st.sidebar.slider('Select Value Range', min_value=int(data['GHI'].min()), max_value=int(data['GHI'].max()), value=(int(data['GHI'].min()), int(data['GHI'].max())))

slider_data = filtered_date[(filtered_date['GHI'] >= value_range[0]) & (filtered_date['GHI'] <= value_range[1])]
st.write(slider_data)

if st.sidebar.button('Generate Report'):
    st.write('Generating report...')
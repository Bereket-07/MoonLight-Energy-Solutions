import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore
import numpy as np

# Function to load the dataset
@st.cache_data
def load_data(file_name):
    return pd.read_csv(file_name)

# Sidebar for dataset selection
st.sidebar.title("Choose Dataset")
dataset_option = st.sidebar.selectbox("Select a dataset", ("benin-malanville_cleaned", "sierraleone-bumbuna_cleaned", "togo-dapaong_qc_cleaned"))

# Load the selected dataset
if dataset_option == "benin-malanville_cleaned":
    df = load_data("https://drive.google.com/uc?export=download&id=1sNFMEXrPodJzZyRe2Asm1Y87P2LmHExf")
elif dataset_option == "sierraleone-bumbuna_cleaned":
    df = load_data("https://drive.google.com/uc?export=download&id=1BqzxDaKKoLmBbCsqZGt37B_wker-tDyN")
else:
    df = load_data("https://drive.google.com/uc?export=download&id=1BqzxDaKKoLmBbCsqZGt37B_wker-tDyN")

# Sidebar for EDA tasks
st.sidebar.title("EDA Options")
eda_option = st.sidebar.selectbox("Choose an analysis", ("Summary Statistics", "Data Quality Check", "Time Series Analysis", "Correlation Analysis", "Wind Analysis", "Temperature Analysis", "Histograms", "Z-Score Analysis", "Bubble Charts"))

# EDA: Summary Statistics
if eda_option == "Summary Statistics":
    st.header("Summary Statistics")
    st.write(df.describe())

# EDA: Data Quality Check
elif eda_option == "Data Quality Check":
    st.header("Data Quality Check")
    st.write(df.isnull().sum())
    st.write("Outliers:")
    st.write(df.describe())

# EDA: Time Series Analysis
elif eda_option == "Time Series Analysis":
    st.header("Time Series Analysis")
    selected_columns = st.multiselect("Select columns to plot", df.columns)
    if selected_columns:
        fig, ax = plt.subplots(figsize=(10, 6))
        for col in selected_columns:
            ax.plot(df[col], label=col)
        ax.legend()
        ax.set_title("Time Series Analysis")
        st.pyplot(fig)

# EDA: Correlation Analysis
elif eda_option == "Correlation Analysis":
    st.header("Correlation Analysis")
    corr = df.corr()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    ax.set_title("Correlation Heatmap")
    st.pyplot(fig)

# EDA: Wind Analysis
elif eda_option == "Wind Analysis":
    st.header("Wind Analysis")
    if 'WS' in df.columns and 'WD' in df.columns:
        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(10, 6))
        wind_speed = df['WS']
        wind_direction = df['WD']
        
        # Convert wind direction to radians
        wind_direction_rad = np.deg2rad(wind_direction)
        
        # Plot wind speed as a function of wind direction
        sc = ax.scatter(wind_direction_rad, wind_speed, c=wind_speed, cmap='viridis', alpha=0.75)
        ax.set_title("Wind Speed and Direction")
        fig.colorbar(sc, ax=ax, label='Wind Speed')
        st.pyplot(fig)
    else:
        st.write("Wind speed or direction columns not found in the dataset.")

# EDA: Temperature Analysis
elif eda_option == "Temperature Analysis":
    st.header("Temperature Analysis")
    if 'Tamb' in df.columns and 'Precipitation' in df.columns:
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Scatter plot of temperature vs. humidity
        ax.scatter(df['Tamb'], df['Precipitation'], alpha=0.5)
        ax.set_xlabel('Temperature')
        ax.set_ylabel('Humidity')
        ax.set_title('Temperature vs. Humidity') 
        st.pyplot(fig)
    else:
        st.write("Temperature or humidity columns not found in the dataset.")


# EDA: Histograms
elif eda_option == "Histograms":
    st.header("Histograms")
    selected_columns = st.multiselect("Select columns to plot", df.columns)
    if selected_columns:
        fig, ax = plt.subplots(figsize=(10, 6))
        df[selected_columns].hist(bins=20, ax=ax)
        ax.set_title("Histograms")
        st.pyplot(fig)

# EDA: Z-Score Analysis
elif eda_option == "Z-Score Analysis":
    st.header("Z-Score Analysis")
    z_scores = zscore(df.select_dtypes(include=['float64', 'int64']))
    fig, ax = plt.subplots(figsize=(10, 6))
    pd.DataFrame(z_scores, columns=df.select_dtypes(include=['float64', 'int64']).columns).describe().plot(ax=ax)
    ax.set_title("Z-Score Analysis")
    st.pyplot(fig)

# EDA: Bubble Charts
elif eda_option == "Bubble Charts":
    st.header("Bubble Charts")
    x_axis = st.selectbox("Select X-axis", df.columns)
    y_axis = st.selectbox("Select Y-axis", df.columns)
    bubble_size = st.selectbox("Select bubble size", df.columns)
    if x_axis and y_axis and bubble_size:
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(df[x_axis], df[y_axis], s=df[bubble_size]*10, alpha=0.5)
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.set_title("Bubble Chart")
        st.pyplot(fig)

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# --- 1. THE HEADER ---
st.title("🌦️ Weather Data Analysis System")
st.write("Welcome! This dashboard analyzes 4 years of Delhi climate data to find trends and anomalies.")

# --- 2. LOADING DATA ---
st.header("Step 1: The Raw Data")
# We use st.cache so it doesn't reload the big file every time you click a button
@st.cache_data
def load_data():
    # Make sure this matches your CSV filename exactly!
    df = pd.read_csv('DailyDelhiClimateTrain.csv')
    df = df.rename(columns={'date': 'Date', 'meantemp': 'Temperature'})
    df['Date'] = pd.to_datetime(df['Date'])
    return df

try:
    df = load_data()
    # Shows the first 5 rows in a nice interactive table
    st.dataframe(df.head())
    st.success("Data loaded successfully!")

    # --- 3. THE GRAPHS ---
    st.header("Step 2: Visualizing Trends")
    st.write("Here is the temperature change over time. Notice the seasonal wave.")

    # Create the figure explicitly
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(df['Date'], df['Temperature'], color='teal')
    ax.set_title('Daily Temperature Trends')
    ax.set_ylabel('Temperature (°C)')
    
    # MAGIC COMMAND: This draws the plot on the website
    st.pyplot(fig) 

    # --- 4. THE MATH (Outliers) ---
    st.header("Step 3: Detecting Anomalies")
    
    # Calculate Z-score (Behind the scenes)
    df['z_score'] = stats.zscore(df['Temperature'])
    outliers = df[np.abs(df['z_score']) > 3]

    st.metric(label="Total Outliers Found", value=len(outliers))
    
    if len(outliers) > 0:
        st.write("These dates had extreme temperatures (statistically rare):")
        st.dataframe(outliers[['Date', 'Temperature']])

except Exception as e:
    st.error(f"Something went wrong: {e}")

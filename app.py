import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Delhi Weather Analysis", page_icon="🌦️")

# --- 1. TITLE & INTRO ---
st.title("🌦️ Weather Data Analysis System")
st.markdown("""
**Welcome!** This dashboard visualizes 4 years of climate data in Delhi to find:
* 📅 **Seasonal Trends** (Summer/Winter Cycles)
* 🌡️ **Anomalies** (Extreme Weather Events)
""")

# --- 2. LOAD DATA ---
@st.cache_data
def load_data():
    # Load dataset
    df = pd.read_csv('DailyDelhiClimateTrain.csv')
    
    # Rename columns for clarity
    df = df.rename(columns={
        'date': 'Date', 
        'meantemp': 'Temperature',
        'humidity': 'Humidity', 
        'wind_speed': 'WindSpeed'
    })
    
    # Convert dates
    df['Date'] = pd.to_datetime(df['Date'])
    return df

# Run the data loading function
try:
    df = load_data()
    st.success("✅ Data loaded successfully!")

    # Interactive Checkbox: Show Raw Data
    if st.checkbox("Show Raw Data Table"):
        st.write(df.head(10))

    # --- 3. TREND VISUALIZATION ---
    st.markdown("---")
    st.header("1. Temperature Trends (2013-2017)")
    st.write("Notice the clear **sine-wave pattern**. The peaks are Summers, and troughs are Winters.")

    # Create the Line Graph
    fig1, ax1 = plt.subplots(figsize=(10, 4))
    ax1.plot(df['Date'], df['Temperature'], color='teal', linewidth=1)
    ax1.set_title("Daily Temperature in Delhi")
    ax1.set_ylabel("Temperature (°C)")
    ax1.set_xlabel("Date")
    ax1.grid(True, alpha=0.3)
    
    # SHOW GRAPH IN STREAMLIT
    st.pyplot(fig1)

    # --- 4. ANOMALY DETECTION (Outliers) ---
    st.markdown("---")
    st.header("2. Detecting Extreme Weather (Outliers)")
    st.write("We use **Z-Score** to find days that were statistically 'too hot' or 'too cold'.")

    # Math Logic
    df['z_score'] = stats.zscore(df['Temperature'])
    
    # Slider: Let users play with the threshold!
    threshold = st.slider("Select Z-Score Threshold (Standard Deviations)", 1.5, 4.0, 3.0)
    
    # Filter based on slider
    outliers = df[np.abs(df['z_score']) > threshold]

    # Display Results
    col1, col2 = st.columns(2)
    col1.metric("Total Days Analyzed", len(df))
    col2.metric("Extreme Days Found", len(outliers))

    if len(outliers) > 0:
        st.write(f"Found {len(outliers)} days where temperature was extreme (Threshold > {threshold})")
        st.dataframe(outliers[['Date', 'Temperature', 'z_score']].sort_values(by='Temperature', ascending=False))
    else:
        st.info(f"No extreme days found with a threshold of {threshold}. Try lowering it to 2.0!")

    # --- 5. DISTRIBUTION PLOT ---
    st.write("### Temperature Distribution")
    fig2, ax2 = plt.subplots(figsize=(10, 3))
    sns.boxplot(x=df['Temperature'], color='orange', ax=ax2)
    st.pyplot(fig2)

except Exception as e:
    st.error(f"Error loading data: {e}")

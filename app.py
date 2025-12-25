import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

st.title("🌦️ Debugging Mode: Weather App")

# --- STEP 1: LOAD DATA ---
st.write("✅ Checkpoint 1: Starting App...")

try:
    df = pd.read_csv('DailyDelhiClimateTrain.csv')
    st.write("✅ Checkpoint 2: CSV Found!")
    
    # Renaming (Crucial Step - if this fails, everything fails)
    df = df.rename(columns={
        'date': 'Date', 
        'meantemp': 'Temperature',
        'humidity': 'Humidity', 
        'wind_speed': 'WindSpeed'
    })
    
    # Date Conversion
    df['Date'] = pd.to_datetime(df['Date'])
    st.write("✅ Checkpoint 3: Data Cleaned & Renamed!")
    st.dataframe(df.head())

    # --- STEP 2: DRAW LINE GRAPH ---
    st.write("⏳ Checkpoint 4: Attempting to draw Line Graph...")
    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(df['Date'], df['Temperature'], color='green')
    ax.set_title("Temperature Trends")
    st.pyplot(fig)
    
    st.write("✅ Checkpoint 5: Line Graph Done!")

    # --- STEP 3: CALCULATE OUTLIERS ---
    st.write("⏳ Checkpoint 6: Calculating Statistics (Scipy)...")
    
    df['z_score'] = stats.zscore(df['Temperature'])
    outliers = df[np.abs(df['z_score']) > 3]
    
    st.write(f"✅ Checkpoint 7: Found {len(outliers)} outliers!")

    # --- STEP 4: SEABORN PLOT ---
    st.write("⏳ Checkpoint 8: Attempting Seaborn Boxplot...")
    
    fig2, ax2 = plt.subplots(figsize=(10, 4))
    sns.boxplot(x=df['Temperature'], ax=ax2)
    st.pyplot(fig2)
    
    st.success("🎉 CONGRATULATIONS! ALL CODE RAN SUCCESSFULLY!")

except Exception as e:
    st.error("❌ THE APP CRASHED HERE!")
    st.error(f"Error Message: {e}")
    st.warning("Please copy the error message above and paste it in the chat.")

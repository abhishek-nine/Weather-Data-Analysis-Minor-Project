# Weather-Data-Analysis-Minor-Project
A Python-based system to analyze seasonal weather trends and detect outliers in Delhi.

# Weather Data Analysis & Visualization System 🌦️

## 📌 Project Overview
# Weather Data Analysis System 🌦️

### 👋 About Me & The Project
Hi, this is my submission for the **Minor Project (3rd Sem)**.
I built this system to analyze 4 years of historical weather data from Delhi. My main goal was to move beyond just looking at excel sheets and actually visualize how the climate changes seasonally, and to mathematically catch any "freak" weather events (outliers).

### 🎯 What I Did
Instead of just plotting a graph, I focused on three specific tasks:
1. **Cleaning the Data:** The raw dates were just text, so I had to convert and sort them to make the time-series work.
2. **Visualizing Trends:** I plotted the temperature over time to clearly show the Summer/Winter cycles (the "waves" in the graph).
3. **Finding Outliers:** I used a statistical method called **Z-Score**. Basically, I wrote code to flag any day that was more than 3 standard deviations away from the average temperature.

### 🛠️ Tools I Used
I wrote the entire project in **Python** using:
* **Pandas:** To load and clean the CSV dataset.
* **Matplotlib & Seaborn:** To draw the line charts and box plots.
* **SciPy:** To calculate the Z-scores for the outlier math.

### 📂 How to Run My Code
If you want to test this on your own machine:
1.  Download the `projectai_ml.ipynb` file and the `DailyDelhiClimateTrain.csv` file from this repo.
2.  Open the notebook in **Google Colab** or Jupyter.
3.  Upload the CSV file to the session.
4.  Run all cells!

### 📊 Results
The analysis was successful. The Line Plot perfectly captures the seasonal sine-wave pattern of Delhi's climate. The Box Plot and Z-Score logic helped identify extreme temperature days that were statistically significant.
## 🚀 Features
* **Data Cleaning (EDA):** Handling missing values, renaming columns, and formatting dates.
* **Trend Analysis:** Visualizing temperature changes over 4 years to demonstrate seasonality.
* **Outlier Detection:** Using **Z-Score analysis** to mathematically identify extreme weather events.
* **Visualization:** Detailed Line Plots and Box Plots using **Matplotlib** and **Seaborn**.

## 🛠️ Tech Stack
* **Language:** Python
* **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, SciPy
* **Dataset:** Daily Climate Time Series Data (Delhi)

## 📊 How to Run
1.  Download the `.ipynb` file and the `.csv` file from this repository.
2.  Open the notebook in **Google Colab** or **Jupyter Notebook**.
3.  Upload the CSV file to the runtime environment.
4.  Run all cells to see the analysis and graphs.

## 📈 Results
* **Seasonality:** The Line Plot clearly shows a sinusoidal wave pattern representing 4 annual summer-winter cycles.
* **Anomalies:** The Box Plot and Z-Score method confirm the distribution of temperature data and identify any statistical outliers.

import pickle
import streamlit as st
import csv
from datetime import datetime

# Load the saved model
Malaria_Project = pickle.load(open('malaria_model1.sav', 'rb'))

# Apply background image only
page_bg_img = '''
<style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://github.com/SHAIK-RAIYAN-2022-CSE/malaria/blob/main/Images-free-abstract-minimalist-wallpaper-HD.jpg?raw=true");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    [data-testid="stHeader"] {
        background: rgba(0, 0, 0, 0); /* Transparent header */
    }
    .block-container {
        max-width: 800px;
        margin: 50px auto; /* Center the content */
        padding: 20px;
        border: 2px solid #ccc; /* Full border */
        border-radius: 15px;
        background: rgba(0, 0, 0, 0.5); /* Semi-transparent background */
        backdrop-filter: blur(10px); /* Background blur effect */
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.6); /* Box shadow for depth */
    }
    input {
        background-color: white !important;
        color: black !important;
        border-radius: 10px;
        border: 1px solid #ccc;
        padding: 10px;
        font-size: 16px;
        width: 90%; /* Ensure inputs are the same width */
        margin: 5px 0; /* Spacing between inputs */
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 24px;
        border-radius: 8px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: white;
        color: #4CAF50;
        border: 2px solid #4CAF50;
    }
    h1, h2, h3, h4, h5, h6, p {
        color: white !important;
    }
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Page title
st.markdown("<h1>Malaria Prediction using Machine Learning</h1>", unsafe_allow_html=True)

# Input section in 3 columns
col1, col2, col3 = st.columns(3)

with col1:
    Temperature_Above_Avg = st.number_input('Temperature Above Avg (°C)', min_value=-10.0, max_value=50.0, value=25.0, step=0.1)
    High_Rainfall = st.number_input('High Rainfall (mm)', min_value=0.0, max_value=500.0, value=150.0, step=1.0)
    High_Humidity = st.number_input('High Humidity (%)', min_value=0, max_value=100, value=60)

with col2:
    Insecticide_Use = st.number_input('Insecticide Use (0-100%)', min_value=0.0, max_value=100.0, value=70.0, step=1.0)
    Health_Facilities_Adequate = st.number_input('Health Facilities Adequate (0-100%)', min_value=0.0, max_value=100.0, value=80.0, step=1.0)
    Vaccination_Rate_High = st.number_input('Vaccination Rate High (0-100%)', min_value=0.0, max_value=100.0, value=90.0, step=1.0)

with col3:
    High_Population_Density = st.number_input('High Population Density (people/km²)', min_value=0, max_value=10000, value=500, step=10)
    Mosquito_Net_Coverage_High = st.number_input('Mosquito Net Coverage High (0-100%)', min_value=0.0, max_value=100.0, value=75.0, step=1.0)
    Malaria_Outbreak = st.number_input('Malaria Outbreak (0-100%)', min_value=0.0, max_value=100.0, value=30.0, step=1.0)

# Prediction result
Malaria_diagnosis = ''

# Prediction button
if st.button('🔍 Malaria Disease Test'):
    try:
        prediction = Malaria_Project.predict([[
            Temperature_Above_Avg, High_Rainfall, High_Humidity,
            High_Population_Density, Malaria_Outbreak, Insecticide_Use,
            Health_Facilities_Adequate, Vaccination_Rate_High, Mosquito_Net_Coverage_High
        ]])
        if prediction[0] == 1:
            Malaria_diagnosis = 'The person is affected with Malaria 😷'
        else:
            Malaria_diagnosis = 'The person is not affected with Malaria 😊'
        
        # Save the data to a CSV file
        with open('malaria_test_results.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now(), Temperature_Above_Avg, High_Rainfall, High_Humidity, High_Population_Density,
                             Malaria_Outbreak, Insecticide_Use, Health_Facilities_Adequate, Vaccination_Rate_High,
                             Mosquito_Net_Coverage_High, Malaria_diagnosis])
            
        st.success(Malaria_diagnosis)
    except ValueError as e:
        st.error(f"Prediction error: {str(e)}")

# Display result
st.success(Malaria_diagnosis)

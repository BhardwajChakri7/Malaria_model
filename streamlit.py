import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

# Custom HTML & CSS
html_code = """
<style>
body {
    background-image: url('https://t3.ftcdn.net/jpg/07/92/27/06/240_F_792270657_Sq8vDFVamGnCMRyAmyWhZdVZyqLXYLzl.jpg');
    background-size: cover;
    font-family: 'Helvetica Neue', sans-serif;
}
.stButton button {
    background-color: #4CAF50;
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 12px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
    transition: 0.3s;
}
.stButton button:hover {
    background-color: #45a049;
}
.stTextInput input {
    border: 2px solid #ccc;
    border-radius: 4px;
    padding: 12px 20px;
    margin: 8px 0;
    box-sizing: border-box;
    font-size: 16px;
    background-color: rgba(255, 255, 255, 0.8);
}
.stTextInput label {
    font-weight: bold;
    color: #333;
}
.container {
    padding: 10px;
    background-color: rgba(255, 255, 255, 0.8);
    border-radius: 10px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
}
h1 {
    color: #4CAF50;
}
</style>
"""

# Display the custom HTML & CSS
components.html(html_code)

# Loading the saved model
Malaria_Project = pickle.load(open('malaria_model1.sav', 'rb'))

st.title("🦟 Malaria Disease Prediction 🩺")

# Getting the input data from the user
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    Temperature_Above_Avg = st.text_input('🌡️ Temperature Above Avg')
    
with col2:
    High_Rainfall = st.text_input('🌧️ High Rainfall')

with col3:
    High_Humidity = st.text_input('💧 High Humidity')
    
with col4:
    High_Population_Density = st.text_input('🏙️ High Population Density')
    
with col5:
    Malaria_Outbreak = st.text_input('🦟 Malaria Outbreak')

with col1:
    Insecticide_Use = st.text_input('🧴 Insecticide Use')
    
with col2:
    Health_Facilities_Adequate = st.text_input('🏥 Health Facilities Adequate')

with col3:
    Vaccination_Rate_High = st.text_input('💉 Vaccination Rate High')
    
with col4:
    Mosquito_Net_Coverage_High = st.text_input('🛏️ Mosquito Net Coverage High')

# Code for Prediction
Malaria_diagnosis = ''

# Creating a button for Prediction
if st.button('🔍 Malaria Disease Test Button'):
    try:
        Malaria_disease_prediction = Malaria_Project.predict([[Temperature_Above_Avg, High_Rainfall, High_Humidity, High_Population_Density, Malaria_Outbreak, Insecticide_Use, Health_Facilities_Adequate, Vaccination_Rate_High, Mosquito_Net_Coverage_High]])
        if Malaria_disease_prediction[0] == 1:
            Malaria_diagnosis = '⚠️ The person is affected with Malaria'
        else:
            Malaria_diagnosis = '✅ The person is not affected with Malaria'
    except ValueError as e:
        st.error(f"Prediction error: {str(e)}")

st.success(Malaria_diagnosis)

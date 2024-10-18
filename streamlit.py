import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

# Load the saved model
Malaria_Project = pickle.load(open('malaria_model1.sav', 'rb'))

# Custom HTML & CSS Styling
html_code = """
<style>
    body {
        font-family: 'Helvetica Neue', sans-serif;
    }
    [data-testid="stAppViewContainer"] {
        background-image: url("https://github.com/BhardwajChakri7/Malaria_model/blob/main/Images-free-abstract-minimalist-wallpaper-HD.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    [data-testid="stHeader"] {
        background: rgba(0, 0, 0, 0); /* Transparent header */
    }
    .block-container {
        max-width: 800px;
        margin: 50px auto;
        padding: 20px;
        border: 2px solid #ccc;
        border-radius: 15px;
        background: rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(10px);
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.6);
    }
    input {
        background-color: rgba(255, 255, 255, 0.8);
        color: black;
        border-radius: 10px;
        border: 2px solid #ccc;
        padding: 12px;
        font-size: 16px;
        margin: 8px 0;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 15px 32px;
        border-radius: 12px;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        transition: 0.3s;
        cursor: pointer;
        border: none;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    label {
        font-weight: bold;
        color: white;
    }
    h1, h2, h3, h4, h5, h6, p {
        color: white !important;
        text-align: center;
    }
</style>
"""
# Display the custom HTML & CSS
components.html(html_code, height=0)

# Page title
st.markdown("<h1>🌿 Malaria Disease Prediction 🩺</h1>", unsafe_allow_html=True)

# Input Fields
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

# Prediction Code
Malaria_diagnosis = ''

# Prediction Button
if st.button('🔍 Malaria Disease Test Button'):
    try:
        prediction = Malaria_Project.predict([[Temperature_Above_Avg, High_Rainfall, High_Humidity,
                                               High_Population_Density, Malaria_Outbreak, Insecticide_Use,
                                               Health_Facilities_Adequate, Vaccination_Rate_High,
                                               Mosquito_Net_Coverage_High]])
        if prediction[0] == 1:
            Malaria_diagnosis = '⚠️ The person is affected with Malaria'
        else:
            Malaria_diagnosis = '✅ The person is not affected with Malaria'
    except ValueError as e:
        st.error(f"Prediction error: {str(e)}")

st.success(Malaria_diagnosis)

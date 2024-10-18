import pickle
import streamlit as st

# Load the saved model
Malaria_Project = pickle.load(open('malaria_model1.sav', 'rb'))

# Apply background image and styling
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
    .content-wrapper {
        max-width: 900px;
        margin: 50px auto; /* Center the content */
        padding: 40px;
        border: 3px solid white; /* Proper border */
        border-radius: 15px;
        background: rgba(0, 0, 0, 0.6); /* Semi-transparent background */
        backdrop-filter: blur(15px); /* Blur effect */
        box-shadow: 0px 8px 30px rgba(0, 0, 0, 0.7); /* Box shadow */
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 12px 28px;
        border-radius: 8px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: white;
        color: #4CAF50;
        border: 2px solid #4CAF50;
    }
    input {
        background-color: white !important;
        color: black !important;
        border-radius: 8px;
        border: 1px solid #ccc;
        padding: 12px;
        font-size: 16px;
        margin-bottom: 10px;
        width: 100%; /* Full-width inputs */
    }
    h1, h2, h3, h4, h5, h6, p {
        color: white !important;
        text-align: center;
    }
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Start the content wrapper
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

# Page title
st.markdown("<h1>Malaria Prediction using Machine Learning</h1>", unsafe_allow_html=True)

# Input section
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    Temperature_Above_Avg = st.text_input('Temperature Above Avg')
    Insecticide_Use = st.text_input('Insecticide Use')

with col2:
    High_Rainfall = st.text_input('High Rainfall')
    Health_Facilities_Adequate = st.text_input('Health Facilities Adequate')

with col3:
    High_Humidity = st.text_input('High Humidity')
    Vaccination_Rate_High = st.text_input('Vaccination Rate High')

with col4:
    High_Population_Density = st.text_input('High Population Density')
    Mosquito_Net_Coverage_High = st.text_input('Mosquito Net Coverage High')

with col5:
    Malaria_Outbreak = st.text_input('Malaria Outbreak')

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
    except ValueError as e:
        st.error(f"Prediction error: {str(e)}")

# Display result
st.success(Malaria_diagnosis)

# End the content wrapper
st.markdown('</div>', unsafe_allow_html=True)

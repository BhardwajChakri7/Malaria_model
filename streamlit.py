import pickle
import streamlit as st

# Load the saved model
Malaria_Project = pickle.load(open('malaria_model1.sav', 'rb'))

# Apply background image with border and blur inside
page_bg_img = '''
<style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://github.com/SHAIK-RAIYAN-2022-CSE/malaria/blob/main/Images-free-abstract-minimalist-wallpaper-HD.jpg?raw=true");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        padding: 50px;
    }
    [data-testid="stHeader"] {
        background: rgba(0, 0, 0, 0);
    }
    .main-content {
        backdrop-filter: blur(10px);
        background: rgba(255, 255, 255, 0.1);
        padding: 30px;
        border-radius: 15px;
        border: 2px solid white;
        max-width: 800px;
        margin: auto;
    }
    input {
        background-color: white !important;
        color: black !important;
        border-radius: 5px;
        border: 1px solid #ccc;
        padding: 10px;
        font-size: 16px;
        width: 100%;
        margin-bottom: 10px;
    }
    h1 {
        color: white;
        text-align: center;
    }
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown('<div class="main-content">', unsafe_allow_html=True)

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

st.success(Malaria_diagnosis)
st.markdown('</div>', unsafe_allow_html=True)

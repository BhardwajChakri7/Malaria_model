import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

Malaria_Project = pickle.load(open('malaria_model1.sav', 'rb'))
# page title
st.title('Malaria Prediction using ML')


# getting the input data from the user
col1, col2, col3,col4, col5 = st.columns(5)

with col1:
    Temperature_Above_Avg = st.text_input('Temperature_Above_Avg')
    
with col2:
    High_Rainfall = st.text_input('High_Rainfall')

with col3:
    High_Humidity = st.text_input('High_Humidity')
    
with col4:
    High_Population_Density = st.text_input('High_Population_Density')
    
with col5:
    Malaria_Outbreak = st.text_input('Malaria_Outbreak')

with col1:
    Insecticide_Use = st.text_input('Insecticide_Use')
    
with col2:
    Health_Facilities_Adequate = st.text_input('Health_Facilities_Adequate')

with col3:
    Vaccination_Rate_High = st.text_input('Vaccination_Rate_High')
    
with col4:
    Mosquito_Net_Coverage_High = st.text_input('Mosquito_Net_Coverage_High')

# code for Prediction
Malaria_diagnosis = ''

# creating a button for Prediction

if st.button('Malaria Disease Test Button'):
    try:
        Malaria_disease_prediction = Malaria_Project.predict([[Temperature_Above_Avg,High_Rainfall,High_Humidity,High_Population_Density,Malaria_Outbreak,Insecticide_Use,Health_Facilities_Adequate,Vaccination_Rate_High,Mosquito_Net_Coverage_High]])
    except ValueError as e:
        st.error(f"Prediction error: {str(e)}")
    
    if (Malaria_disease_prediction[0] == 1):
      Malaria_diagnosis = 'The person is effected with Malaria'
    else:
      Malaria_diagnosis = 'The person is not effected with Malaria'
    
st.success(Malaria_diagnosis)

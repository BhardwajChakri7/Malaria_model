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
    Age = st.text_input('Age')
    
with col2:
    Gender = st.text_input('Gender')

with col3:
    Access_to_Clean_Water = st.text_input('Access_to_Clean Water')
    
with col4:
    Sanitation_Facilities = st.text_input('Sanitation_Facilities')
    
with col5:
    Proximity_to_Water_Source = st.text_input('Proximity_to_Water_Source')

with col1:
    Population_Density = st.text_input('Population_Density')
    
with col2:
    Income_Level = st.text_input('Income_Level')

with col3:
    Education_Level = st.text_input('Education_Level')

with col4:
    Housing_Conditions = st.text_input('Housing_Conditions')

with col5:
    Season = st.text_input('Season')
    
with col1:
    Pre_existing_Conditions = st.text_input('Pre_existing_Conditions')

with col2:
    Vaccination_Status = st.text_input('Vaccination_Status')
    
with col3:
    Access_to_Healthcare = st.text_input('Access_to_Healthcare')
    
# code for Prediction
Malaria_diagnosis = ''

# creating a button for Prediction

if st.button('Malaria Disease Test Button'):
    try:
        Malaria_disease_prediction = Malaria_Project.predict([[Age,Gender,Access_to_Clean_Water,Sanitation_Facilities,Proximity_to_Water_Source,Population_Density,Income_Level,Education_Level,Housing_Conditions,Season,Pre_existing_Conditions,Vaccination_Status,Access_to_Healthcare]])
    except ValueError as e:
        st.error(f"Prediction error: {str(e)}")
    
    if (Malaria_disease_prediction[0] == 1):
      Malaria_diagnosis = 'The person is effected with Malaria'
    else:
      Malaria_diagnosis = 'The person is not effected with Malaria'
    
st.success(Malaria_diagnosis)

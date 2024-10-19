import streamlit as st
import pandas as pd
import pickle
import os

# Load the saved model (update the path to your model file)
model_path = 'malaria_model1.sav'
Malaria_Project = pickle.load(open(model_path, 'rb'))

# Define the CSV file path
csv_file_path = 'malaria_cases.csv'

# Create CSV file with headers if it does not exist
if not os.path.isfile(csv_file_path):
    with open(csv_file_path, 'w') as f:
        f.write('Temperature_Above_Avg,High_Rainfall,High_Humidity,Insecticide_Use,Health_Facilities_Adequate,Vaccination_Rate_High,High_Population_Density,Mosquito_Net_Coverage_High,Malaria_Outbreak,Malaria_diagnosis\n')

# Set page title
st.title('Malaria Prediction App')

# User input fields
Temperature_Above_Avg = st.number_input('Temperature Above Avg (°C)', min_value=-10.0, max_value=50.0, value=25.0, step=0.1)
High_Rainfall = st.number_input('High Rainfall (mm)', min_value=0.0, max_value=500.0, value=150.0, step=1.0)
High_Humidity = st.number_input('High Humidity (%)', min_value=0, max_value=100, value=60)
Insecticide_Use = st.number_input('Insecticide Use (0-100%)', min_value=0.0, max_value=100.0, value=70.0, step=1.0)
Health_Facilities_Adequate = st.number_input('Health Facilities Adequate (0-100%)', min_value=0.0, max_value=100.0, value=80.0, step=1.0)
Vaccination_Rate_High = st.number_input('Vaccination Rate High (0-100%)', min_value=0.0, max_value=100.0, value=90.0, step=1.0)
High_Population_Density = st.number_input('High Population Density (people/km²)', min_value=0, max_value=10000, value=500, step=10)
Mosquito_Net_Coverage_High = st.number_input('Mosquito Net Coverage High (0-100%)', min_value=0.0, max_value=100.0, value=75.0, step=1.0)
Malaria_Outbreak = st.number_input('Malaria Outbreak (0-100%)', min_value=0.0, max_value=100.0, value=30.0, step=1.0)

# Prediction result
Malaria_diagnosis = ''

# Prediction button
if st.button('🔍 Malaria Disease Test'):
    prediction = Malaria_Project.predict([[
        Temperature_Above_Avg, High_Rainfall, High_Humidity,
        Insecticide_Use, Health_Facilities_Adequate, Vaccination_Rate_High,
        High_Population_Density, Mosquito_Net_Coverage_High, Malaria_Outbreak
    ]])
    Malaria_diagnosis = 'The person is affected with Malaria 😷' if prediction[0] == 1 else 'The person is not affected with Malaria 😊'
    
    # Prepare data to save
    data_to_save = {
        'Temperature_Above_Avg': Temperature_Above_Avg,
        'High_Rainfall': High_Rainfall,
        'High_Humidity': High_Humidity,
        'Insecticide_Use': Insecticide_Use,
        'Health_Facilities_Adequate': Health_Facilities_Adequate,
        'Vaccination_Rate_High': Vaccination_Rate_High,
        'High_Population_Density': High_Population_Density,
        'Mosquito_Net_Coverage_High': Mosquito_Net_Coverage_High,
        'Malaria_Outbreak': Malaria_Outbreak,
        'Malaria_diagnosis': Malaria_diagnosis
    }

    # Convert to DataFrame and append to CSV
    df = pd.DataFrame([data_to_save])
    df.to_csv(csv_file_path, mode='a', header=False, index=False)

# Display the prediction result
st.success(Malaria_diagnosis)

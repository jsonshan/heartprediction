import streamlit as st
import numpy as np
import pandas as pd
import joblib
import pickle

model = joblib.load('classifier.joblib')

#[Age,Sex,ChestPainType,
#Cholesterol,FastingBS,MaxHR,ExeriseAngina,Oldpeak,ST_Slope]
st.title('Heart Disease Prediction Form')
Age = st.text_input('Input Age 0 - 100', 0,100)

sex_options = {'Male': 0, 'Female': 1}
sex_value = st.select_slider('Select sex', ['Male', 'Female'])
Sex = sex_options[sex_value]

ChestPainType_dict = {'ATA': 1, 'NAP' : 2, 'ASY': 0, 'TA' : 3}
ChestPainType_KEY = st.select_slider('Select ChestPain', ['ATA', 'NAP', 'ASY', 'TA'])
ChestPainType = ChestPainType_dict[ChestPainType_KEY]

Cholesterol = st.text_input('Input Cholesterol Level 80 - 300', 0, 100)

FASTING_BS_dict = {'No': 0, 'Yes': 1}
FASTING_BS_key = st.select_slider('FASTING_BS', ['Yes', 'No'])
FastingBS = FASTING_BS_dict[FASTING_BS_key]

MaxHR = st.text_input('Input MaxHeartRate 0 - 300', 0,10)

ExerciseAgina_dict = {'Y' : 1, 'N' : 0}
ExerciseAgina_KEY = st.select_slider('ExerciseAgina', ['Y', 'N'])
ExerciseAgina = ExerciseAgina_dict[ExerciseAgina_KEY]

Oldpeak_dict = {'No': 0, 'Yes': 1}
Oldpeak_key = st.select_slider('Oldpeak', ['Yes', 'No'])
Oldpeak = Oldpeak_dict[Oldpeak_key]

ST_Slope_dict = {'Up': 2, 'Flat': 1}
ST_Slope_key = st.select_slider('Select ST_Slope', ['Up', 'Flat'])
ST_Slope = ST_Slope_dict[ST_Slope_key]

#[Age,Sex,ChestPainType,
#Cholesterol,FastingBS,MaxHR,ExeriseAngina,Oldpeak,ST_Slope]

def predict():
    row = np.array([Age,Sex,ChestPainType,Cholesterol,FastingBS,
                    MaxHR,ExerciseAgina, Oldpeak, ST_Slope])
    X = pd.DataFrame([row])
    prediction = model.predict(X)[0]

    if prediction == 1:
        st.error('Has Heart Disease')
    elif prediction == 0:
        st.success('No Heart Disease')
st.button('Predict', on_click=predict)




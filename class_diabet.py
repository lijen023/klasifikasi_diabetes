import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('diabetes.sav', 'rb'))

st.title('Prediksi Diabetes')
col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.number_input('Jumlah Kehamilan')
    BloodPressure = st.number_input('Tekanan Darah')
    Insulin = st.number_input('Insulin')
    DiabetesPedigreeFunction = st.number_input('Riwayat Diabetes')

with col2:
    Glucose = st.number_input('Glukosa')
    SkinThickness = st.number_input('Ketebalan kulit (mm)')
    BMI = st.number_input('Berat Badan')
    Age = st.number_input('Usia')

predik = ''
if st.button('Hasil Prediksi'):
    predik = model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if(predik[0] == 1):
        predik = 'Pasien Memiliki Penyakit Diabetes'
    else:
        predik = 'Pasien Tidak Memiliki Penyakit Diabetes'
st.success(predik)
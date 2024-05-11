import streamlit as st
import pickle
from funcs import process
import datetime as dt
import pandas as pd
import random

st.set_page_config(layout="wide")

model = pickle.load(open('model.pkl', 'rb'))

st.title('Credit Card Approval Prediction')
st.divider()

st.header('Your Gender')
gender = st.radio('Please Choose your Gender', ['Male', 'Female'])
st.text('')

st.header('Owns Car')
has_car = st.radio('Do you own a Car?', ['Yes', 'No'])
st.text('')

st.header('Owns Property')
has_property = st.radio('Do you own a Property?', ['Yes', 'No'])
st.text('')

st.header('No of Children')
num_children = st.slider("How many children do you have?", 0, 5)
st.text('')

st.header('Income')
income = st.slider("How much do you earn anually (in USD)?", 0, 400000, step=1000)
st.text('')

st.header('Employment Status')
employment_status = st.selectbox('What is your Employment Status', ['Working', 'Commercial associate', 'Pensioner', 'State servant', 'Student'])
st.text('')

st.header('Education Level')
education_level = st.selectbox('What is your education level', ['Secondary / secondary special', 'Higher education', 'Incomplete higher'])
st.text('')

st.header('Marital status')
martial_status = st.selectbox('What is your Marital status', ['Single / not married', 'Married', 'Separated'])
st.text('')

st.header('Dwelling')
dwelling = st.selectbox('Where do you stay', ['House / apartment', 'With parents'])
st.text('')

st.header('Age')
age = st.date_input('What is your Date Of Birth (DOB)?', value=None, min_value=dt.datetime(1920, 1, 1))
st.text('')

st.header('Employment Length')
employmentLength = st.text_input('For how much time you were Employed (in Years)?')
st.text('')

st.header('Has a mobile phone')
mobile_phones = st.radio('Do you own a mobile phone?', ['Yes', 'No'])
st.text('')

st.header('Has a work phone')
work_phones = st.radio('Do you own a work phone?', ['Yes', 'No'])
st.text('')

st.header('Has an email')
email = st.radio('Do you own an email?', ['Yes', 'No'])
st.text('')

st.header('Family member count')
family_count = st.slider('How many members are in your family?', 1, 12)
st.text('')

bt = st.button('Predict')

if bt:
    age = (-(dt.date.today() - age)).days
    input_df = pd.DataFrame({'Gender': [gender], 'Has a car': [has_car], 'Has a property': [has_property],
                        'Children count': [num_children], 'Income': [income], 'Employment status': [employment_status], 
                         'Education level': [education_level], 'Marital status': [martial_status], 'Dwelling': [dwelling],
                        'Age': [age], 'Employment length': [-(int(employmentLength)*365)], 'Has a mobile phone': [mobile_phones],
                        'Has a work phone': [work_phones], 'Has an email': [email], 'Family member count': [family_count],
                         })
    print(input_df)
    print(age, '685191941841')
    input_df = process(input_df)
    input_df.to_csv('hi.csv')
    
    for col in ['Commercial associate', 'Pensioner', 'State servant', 'Student', 'Working']:
        if employment_status == col:
            input_df[col] = [1]
        else:
            input_df[col] = [0]
    
    for col in input_df.columns:
        print(col, input_df[col])
        input_df[col] = input_df[col].astype('int64')
    
    pred = model.predict(input_df)
    print(pred)

    if pred:
        st.success('Congrats You have 98% chance to get Accepted for Credit Card')
        st.balloons()
    else:
        st.error('Sorry! you have 98% chance of not get Accepted for Credit Card')

with open('style.css') as file:
    st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html=True)

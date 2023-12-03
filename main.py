import streamlit as st
import pickle


model = pickle.load(open('model.pickle', 'rb'))
params = pickle.load(open('params.pickle', 'rb'))


st.set_page_config(page_title='Bengaluru House Price Prediction', page_icon=':house:')
st.title('Bengaluru House Price Prediction')
st.subheader('Predict the price of a house in Bengaluru using Machine Learning')

st.text_input('Total Square Feet', placeholder='Enter the total square feet area of the house')
st.text_input('Number of Bathrooms', placeholder='Enter the number of bathrooms in the house')
st.text_input('Number of Bedrooms', placeholder='Enter the number of bedrooms in the house')
st.selectbox('Choose the location of the house', params['columns'])

st.button('Predict', type='primary')

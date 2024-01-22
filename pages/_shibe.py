import streamlit as st
import requests

with st.sidebar:
  with st.form(key='form-shibe', clear_on_submit=True):
    st.header('How many images?')
    image_counts = st.text_input('Number')
    submitted = st.form_submit_button('Ok')


if(submitted):    
    url = f'http://shibe.online/api/shibes?count={image_counts}&urls=true&httpsUrls=true'

    response = requests.get(url).json()
    c = 4
    with st.container():
        col = st.columns(c)
        for j in range(len(response)):        
            img = response[j]
            col[j%c].image(img, caption=j, width=150) 

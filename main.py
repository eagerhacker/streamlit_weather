
import streamlit as st
import time
import requests

with st.sidebar:
    st.write('OpenWeather API')

    with st.container():   
        st.write('Enter city name')
        city_input = st.text_input(label='City')
        button_click = st.button('Ok')


if(button_click):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_input}&appid=e18e2840b7cac5da739d40852029957a'
    response = requests.get(url).json()
    # weather = response['weather'][0]['main']
    st.header(f'Thoi tiet {city_input} hom nay')

    col1, col2,col3 = st.columns(3)
    with col1:
        
        st.image("http://openweathermap.org/img/wn/" + response['weather'][0]['icon'] + "@4x.png")
        st.write(response['weather'][0]['description'])

    with col2:
        st.write(f"Nhiet do: {response['main']['temp']}")
        st.write('Cam giac nhu')
        st.write('Do am')
        st.write('Toc do gio')

    with col3:
        st.write('May')
        st.write('Mat troi moc')
        st.write('Mat troi lan')
        
    

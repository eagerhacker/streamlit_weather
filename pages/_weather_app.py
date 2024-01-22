from re import sub
import streamlit as st
from datetime import datetime
import requests

# if 'key' not in st.session_state:
    # st.session_state.key = 'value'
with st.sidebar:
    st.title('OpenWeather API')

    with st.form(key='form_input', clear_on_submit=True, border=True):
        st.header('Nhap ten thanh pho')
        city_input = st.text_input(label='city')
        # button_click = st.button('Xem thoi tiet')

        submitted = st.form_submit_button('OK')

if(submitted):
    if(city_input):
# if(button_click or city_input):
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_input}&units=metric&appid=e18e2840b7cac5da739d40852029957a'
        print(url)
        response = requests.get(url).json()

        if(response['cod'] == 200):
            st.header(f'Thoi tiet {city_input.capitalize()} hom nay')

            col1, col2,col3 = st.columns(3)
            with col1:
                st.image("http://openweathermap.org/img/wn/" + response['weather'][0]['icon'] + "@4x.png",caption=response['weather'][0]['description'])

            with col2:
                st.metric(label='Nhiet do', value=f"{response['main']['temp']}°C")
                st.metric(label="Cam giac nhu", value=f"{response['main']['feels_like']}°C")
                st.metric("Do am:", f"{response['main']['humidity']}%")
                st.metric("Toc do gio", f"{response['wind']['speed']}m/s")

                # st.markdown(f"Nhiet do: :blue[{response['main']['temp']}]")
                # st.markdown(f"Cam giac nhu: :blue[{response['main']['feels_like']}]")
                # st.markdown(f"Do am: :blue[{response['main']['humidity']}]")
                # st.markdown(f"Toc do gio: :blue[{response['wind']['speed']}]")

            with col3:
                st.metric("May", f"{response['clouds']['all']}")
                st.metric("Mat troi moc",f"{datetime.fromtimestamp(response['sys']['sunrise']).strftime('%H:%M:%S')}")
                st.metric("Mat troi lan", f"{datetime.fromtimestamp(response['sys']['sunset']).strftime('%H:%M:%S')}")

                # st.markdown(f"May: :blue[{response['clouds']['all']}]")
                # st.markdown(f"Mat troi moc: :blue[{datetime.fromtimestamp(response['sys']['sunrise'])}]")
                # st.markdown(f"Mat troi lan: :blue[{datetime.fromtimestamp(response['sys']['sunset'])}]")
        else:
            st.warning('thanh pho ko tim thay')
    else:
        st.warning('nhap ten thanh pho')
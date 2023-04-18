import streamlit as st
import requests
from PIL import Image

def api_call(calle, numero):
    response = requests.get(f'https://la-plomada-xy4jjpbnna-ey.a.run.app/predict?street={calle}&number={numero}')
    if response.status_code == 200:
        data = response.json()
        st.write(data)
    else:
        st.error("Failed to retrieve data from API")

def fake_api_call(calle, numero):
    return (12, 13)

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
#        </style>
       """

# ICON
icon = Image.open('icono-invertido.png')

st.set_page_config(
    page_title="LP - Calles de La Plata",
    page_icon=icon,
    layout="centered",
    initial_sidebar_state="expanded")

# with open("style.css") as css:
#     st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

# HIDE DEFAULT FORMAT
st.markdown(hide_default_format, unsafe_allow_html=True)

# TITLE
st.markdown('<h1 style="text-align:center;">Calles de La Plata</h1>', unsafe_allow_html=True)
# st.markdown('<h4 style="text-align:center;">Un breve subtitulo</h4>', unsafe_allow_html=True)
st.markdown("#")
st.markdown("##")

col_a1, col_a2 = st.columns(2)
with col_a1:
    n1 = int(st.number_input('Número de calle:', value=0, step=1))
with col_a2:
    n2 = int(st.number_input('Número de casa:', value=0, step=1))



st.markdown("##")

col_b1, col_b2, col_b3, col_b4, col_b5 = st.columns(5)
with col_b1:
    pass
with col_b2:
    pass
with col_b3:
    if st.button("¿Entre qué calles queda?"):
        result = fake_api_call(n1, n2)
        response_string = f'<h4 style="text-align:center;">{result[0]} & {result[1]}</h4>'
        st.write("")
        st.markdown('<p style="text-align:center;">Entre las calles</p>', unsafe_allow_html=True)
        st.markdown(response_string, unsafe_allow_html=True)

with col_b4:
    pass
with col_b5:
    pass

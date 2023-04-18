import streamlit as st
import requests
from PIL import Image

# API call
def api_call(calle, numero):
    response = requests.get(f'https://la-plomada-xy4jjpbnna-ey.a.run.app/predict?street={calle}&number={numero}')
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        st.error("Failed to retrieve data from API")

# Fake API call for tests
def fake_api_call(calle, numero):
    return {"error1":"calle no contenida dentro del algoritmo"}

def local_api_call(calle, numero):
    response = requests.get(f'http://localhost:8000/predict?street={calle}&number={numero}')
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        st.error("Failed to retrieve data from API")

# Hide menu bar
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
#        </style>
       """

# # # PAGE # # #

# PAGE CONFIG
icon = Image.open('icono-invertido.png')

st.set_page_config(
    page_title="LP - Calles de La Plata",
    page_icon=icon,
    layout="centered",
    initial_sidebar_state="expanded")

st.markdown(hide_default_format, unsafe_allow_html=True) # Activate hide menu bar


# ESCUDO
col_c1, col_c2, col_c3, col_c4, col_c5 = st.columns(5)
with col_c1:
    pass
with col_c2:
    pass
with col_c3:
    shield = Image.open('escudo.png')
    st.image(shield, caption=None,
         width=130, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
with col_c4:
    pass
with col_c5:
    pass


# TITLE
st.markdown('<h1 style="text-align:center;">Calles de La Plata</h1>', unsafe_allow_html=True)
# st.markdown('<h4 style="text-align:center;">Un breve subtitulo</h4>', unsafe_allow_html=True)
st.markdown("#")
st.markdown("##")

# INPUTS
col_a1, col_a2 = st.columns(2)
with col_a1:
    n1 = int(st.number_input('Número de calle:', value=0, step=1))
with col_a2:
    n2 = int(st.number_input('Número de casa:', value=0, step=1))
st.markdown("##")

# BUTTON & RESPONSE
col_b1, col_b2, col_b3, col_b4, col_b5 = st.columns(5)
with col_b1:
    pass
with col_b2:
    pass
with col_b3:
    if st.button("¿Entre qué calles queda?"):      # push button, retrieve data
        result = api_call(n1, n2)                  # API call
        if result["code"] == "error1":
            msg = result["message"]
            st.markdown(f'<p style="text-align:center;">{msg}</p>', unsafe_allow_html=True)
        elif result["code"] == "error2":
            msg = result["message"]
            st.markdown(f'<p style="text-align:center;">{msg}</p>', unsafe_allow_html=True)
        elif result["code"] == "error3":
            msg = result["message"]
            st.markdown(f'<p style="text-align:center;">{msg}</p>', unsafe_allow_html=True)
        elif result["code"] == "ok":
            response_string = f'<h4 style="text-align:center;">{result["message"][0]} & {result["message"][1]}</shield>'
            st.write("")
            # st.markdown('<p style="text-align:center;">Calles</p>', unsafe_allow_html=True)
            st.markdown(response_string, unsafe_allow_html=True)

with col_b4:
    pass
with col_b5:
    pass

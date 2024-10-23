import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import sqlite3
from fpdf import FPDF

st.sidebar.image(image='img/LogoPerla.png',caption="")
st.sidebar.caption("Bienvenido Admin!.")

with st.sidebar:
        beta_sign = """
        <span style="
        font-size: 12px;
        font-weight: bold;
        color: #ffffff;
        background-color: #ff5733;
        padding: 15px;
        border-radius: 5px;
        ">
            BETA
        </span>
        """
        seleccion_menu = option_menu(
            menu_title="Seleccione su Rol",
            options=["","Jefe de grupo","Administrador"]
        )

if seleccion_menu == "":
        st.video(video='img/Cat dancing to Chinese song #cat #catdancing #dancing #china #chinese #科目三 #科目三舞蹈 - kittyhaerin🫶🏻 (720p, h264, youtube).mp4',caption="")

if seleccion_menu == "Jefe de grupo":
        st.title("Jefe de grupo") 
        beta_sign = """
        <span style="
        font-size: 10px;
        font-weight: bold;
        color: #ffffff;
        background-color: #ff5733;
        padding: 5px 10px;
        border-radius: 4px;
        ">
                BETA
        </span>
        """
        seleccion_menu2 = option_menu(
                menu_title="Seleccione su carrera",
                options=["ICI","ISET"]
        )
if seleccion_menu == "Administrador":
        st.title("Administrador")

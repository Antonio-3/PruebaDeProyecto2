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
        st.image(image='img/LogoUnixd.png', caption="", use_column_width=True)
        st.write("\n")
        st.title("Bienvenidos a nuestro proyecto :)")
        st.write("Somos Antonio, Perla , Josue y Danahy, estudiantes de la Universidad De Colima. ")
        st.write("\n")
        st.write("Este proyecto tiene como objetivo crear un programa para que un admistrador pueda consultar o asignar las faltas de asistencia de profesores, materias, o dependiendo del programa educativo")
        st.write("\n")
        st.write("A lo largo de esta página, encontrarás información sobre nuestro trabajo, ideas y logros a lo largo del proceso. Esperamos que disfrutes navegando por nuestra página y descubras más sobre este proyecto.")

if seleccion_menu == "Jefe de grupo":
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
        st.caption("Bienvenido Jefe de grupo!")
        seleccion_menu2 = option_menu(
                menu_title="Seleccione su carrera",
                options=["ICI","ISET"]
        )


if seleccion_menu == "Administrador":
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
        st.caption("Bienvenido admin!")
        seleccion_menu3 = option_menu(
                menu_title="Que desea hacer?",
                options=["Agregar Datos","Eliminar Datos"]
        )
        if seleccion_menu3 == "Agregar Datos":
                st.write("Agregar Datos")
                
         if seleccion_menu3 == "Eliminar Datos":
                st.write("Eliminar Datos")

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
        seleccion_jefe = option_menu(
                menu_title="Seleccione su carrera",
                options=["ICI","ISET"]
        )
        if seleccion_jefe == "ICI":
                st.write("ICI")
                        
        if seleccion_jefe == "ISET":
                st.write("ISET")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        
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
        seleccion_reporte = option_menu(
                menu_title="Apartado de Reportes",
                options=["Reporte por profesor","Reporte por materia", "Reporte global"]
        )
        if seleccion_reporte == "Reporte por profesor":
                st.write("  \n")
                st.write("  \n")
                st.write("  \n")
                st.write("  \n")
                st.title("Reporte por profesor")
                # Conectar a la base de datos
                conexion = sqlite3.connect('BasePrueba/ProfesoresPrueba.db')
                df = pd.read_sql("SELECT DISTINCT Profesor FROM materiaprofe;", conexion)
                st.write("  \n")
                seleccion_profeexd = st.selectbox('Selecciona un profesor:', df['Profesor'])
                cursor = conexion.cursor()
                conexion.close()
                # Función para generar el PDF
                def generar_pdf():
                        pdf = FPDF()
                        pdf.add_page()
                        pdf.set_font("Arial", size=12)
                        pdf.cell(200, 10, txt="Reporte JSJSJSJNDAOUWNDAN", ln=True, align='C')
                        pdf.cell(200, 10, txt="Reporte de: ", txt=seleccion_profeexd, ln=True, align='C')    
                        # Guardar PDF en un archivo temporal
                        pdf_output = 'output.pdf'
                        pdf.output(pdf_output)
                        # Retornar el archivo generado
                        return pdf_output
                        # Abrir el archivo PDF y mostrar un enlace de descarga
                pdf_file = generar_pdf()
                
        with open(pdf_file, "rb") as f:
                st.download_button(label="Descargar Reporte del profesor", data=f, file_name="PruebaReporteJSJSJXDD.pdf")
                        
        if seleccion_reporte == "Reporte por materia":
                st.write("Reporte por materia")
                
        if seleccion_reporte == "Reporte global":
                st.write("Reporte global")
                
        

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
        seleccion_admin = option_menu(
                menu_title="Que desea hacer?",
                options=["Agregar Datos","Eliminar Datos"]
        )
        if seleccion_admin == "Agregar Datos":
                st.write("Agregar Datos")
                        
        if seleccion_admin == "Eliminar Datos":
                st.write("Eliminar Datos")

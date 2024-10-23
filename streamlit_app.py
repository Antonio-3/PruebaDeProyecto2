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
        seleccion_menu = option_menu(
            menu_title="Menú",
            options=["Inicio","Consultar tablas", "Asistencias", "Generar Reportes"]
        )

if seleccion_menu == "Inicio":
        st.image(image='img/LogoUnixd.png', caption="", use_column_width=True)
        st.write("\n")
        st.title("Bienvenidos a nuestro proyecto :)")
        st.write("Somos Antonio, Perla , Josue y Danahy, estudiantes de la Universidad De Colima. ")
        st.write("\n")
        st.write("Este proyecto tiene como objetivo crear un programa para que un admistrador pueda consultar o asignar las faltas de asistencia de profesores, materias, o dependiendo del programa educativo")
        st.write("\n")
        st.write("A lo largo de esta página, encontrarás información sobre nuestro trabajo, ideas y logros a lo largo del proceso. Esperamos que disfrutes navegando por nuestra página y descubras más sobre este proyecto.")

                
if seleccion_menu == "Consultar tablas":
        st.title("Tablas")
        # Conectar a la base de datos
        conexion = sqlite3.connect('BasePrueba/ProfesoresPrueba.db')
        cursor = conexion.cursor()
        # Seleccionar todas las materias
        cursor.execute('''
        SELECT * FROM materiaprofe
         ''')
        # Recuperar todos los registros
        xd = cursor.fetchall()
        # Mostrar los registros de forma estructurada
        st.write("\nLista de Proferores:\n")
        st.write("{:<5} {:<25} {:<20} {:<10} {:20} {:<25} {:<20}".format('ID', 'Profesor', 'Materia', 'Carrera','Fecha','Horario','Asistencia'))
        st.write("-" * 60)
        for lol in xd:
                st.write("{:<5} {:<25} {:<20} {:<10} {:<25} {:<20} {:<10}".format(lol[0], lol[1], lol[2],
                 lol[3], lol[4], lol[5], lol[6]))
        conexion.close()

        
if seleccion_menu == "Asistencias":
        st.title("Asistencias")
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
                menu_title="Que desea hacer?",
                options=["Modificar Asistencia","Poner asistencia"]
        )

        
        
if seleccion_menu == "Generar Reportes":
        
        # Función para generar el PDF
        def generar_pdf():
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                pdf.cell(200, 10, txt="Reporte JSJSJSJNDAOUWNDAN", ln=True, align='C')
                pdf.cell(200, 10, txt="awdawdawdxdddd", ln=True, align='C')
                
                    
                # Guardar PDF en un archivo temporal
                pdf_output = 'output.pdf'
                pdf.output(pdf_output)
                    
                # Retornar el archivo generado
                return pdf_output
                        
        st.title("Generar Reportes")
        # Conectar a la base de datos
        conexion = sqlite3.connect('BasePrueba/ProfesoresPrueba.db')
        df = pd.read_sql("SELECT DISTINCT Profesor FROM materiaprofe;", conexion)
        seleccion_profeexd = st.selectbox('Selecciona un profesor:', df['Profesor'])
        cursor = conexion.cursor()
        conexion.close()
        pdf_file = generar_pdf()
                    
         # Abrir el archivo PDF y mostrar un enlace de descarga
        with open(pdf_file, "rb") as f:
                st.download_button(label="Descargar Reporte del profesor", data=f, file_name="PruebaReporteJSJSJXDD.pdf")
               

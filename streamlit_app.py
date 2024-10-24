import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import sqlite3
from fpdf import FPDF
import mysql.connector

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
                        # Conectar a la base de datos
                        conexion = sqlite3.connect('BasePrueba/ProfesoresPrueba.db')
                        cursor = conexion.cursor()
                        cursor.execute("SELECT * FROM materiaprofe WHERE Profesor=?",(seleccion_profeexd,))
                        # Recuperar todos los registros
                        materiaprofe = cursor.fetchall()
                        # Crear una instancia de FPDF
                        pdf = FPDF()
                        pdf.set_auto_page_break(auto=True, margin=15)
                        # Agregar una página
                        pdf.add_page()
                        # Establecer el tipo de fuente (Arial, negrita, tamaño 16)
                        pdf.set_font('Arial', 'B', 16)
                        # Título del reporte
                        pdf.cell(200, 10, 'Reporte de Profesor', ln=True, align='C')
                        # Espacio adicional
                        pdf.ln(10)
                        # Establecer el tipo de fuente para el contenido 
                        pdf.set_font('Arial', '', 12)

                        # Encabezados de la tabla ajustados
                        pdf.cell(10, 10, 'ID', 1)     
                        pdf.cell(45, 10, 'Profesor', 1)  
                        pdf.cell(40, 10, 'Materia', 1)    
                        pdf.cell(40, 10, 'Carrera', 1)  
                        pdf.cell(30, 10, 'Fecha', 1)      
                        pdf.cell(25, 10, 'Horario', 1)   
                        pdf.cell(20, 10, 'Asistencia', 1) 
                        pdf.ln()
                        
                        # Agregar los registros de materias al PDF con ajustes
                        for materia in materiaprofe:
                            pdf.cell(10, 10, str(materia[0]), 1)   
                            pdf.cell(45, 10, materia[1], 1)        
                            pdf.cell(40, 10, materia[2], 1)        
                            pdf.cell(40, 10, str(materia[3]), 1)    
                            pdf.cell(30, 10, materia[4], 1)        
                            pdf.cell(25, 10, materia[5], 1)        
                            pdf.cell(20, 10, str(materia[6]), 1)    
                            pdf.ln()
                        # Guardar el archivo PDF
                        
                        pdf.cell(20, 10, 'El profesor: ', ln=True, align='C')
                        pdf.cell(20, 10, seleccion_profeexd, ln=False, align='C')
                        pdf.output('Reporte_profe.pdf')
                        
                        # Cerrar la conexión
                        conexion.close()
                        # Retornar el contenido del PDF en bytes
                        return pdf.output(dest='S').encode('latin1')
                # Botón para generar el PDF
                if st.button("Generar Reporte"):
                        # Generar el PDF
                        pdf_content = generar_pdf()
                        st.caption("100% completado...")
                        # Crear un botón de descarga
                        st.download_button(
                                label="Descargar Reporte en PDF",
                                data=pdf_content,
                                file_name="Reporte_Profe.pdf",
                                mime="application/pdf"
                        )















        
        
                        
        if seleccion_reporte == "Reporte por materia":
                st.write("  \n")
                st.write("  \n")
                st.write("  \n")
                st.write("  \n")
                st.title("Reporte por materia")
                # Conectar a la base de datos
                conexion = sqlite3.connect('BasePrueba/ProfesoresPrueba.db')
                df = pd.read_sql("SELECT DISTINCT Materia FROM materiaprofe;", conexion)
                st.write("  \n")
                seleccion_materiaxd = st.selectbox('Selecciona un profesor:', df['Materia'])
                cursor = conexion.cursor()
                conexion.close()
                # Función para generar el PDF
                def generar_pdf():
                        # Conectar a la base de datos
                        conexion = sqlite3.connect('BasePrueba/ProfesoresPrueba.db')
                        cursor = conexion.cursor()
                        cursor.execute("SELECT * FROM materiaprofe WHERE Materia=?",(seleccion_materiaxd,))
                        # Recuperar todos los registros
                        materiaprofe = cursor.fetchall()
                        # Crear una instancia de FPDF
                        pdf = FPDF()
                        pdf.set_auto_page_break(auto=True, margin=15)
                        # Agregar una página
                        pdf.add_page()
                        # Establecer el tipo de fuente
                        pdf.set_font('Arial', 'B', 16)
                        # Título del reporte
                        pdf.cell(200, 10, 'Reporte de Profesor', ln=True, align='C')
                        # Espacio adicional
                        pdf.ln(10)
                        # Establecer el tipo de fuente para el contenido
                        pdf.set_font('Arial', '', 12)

                        # Encabezados de la tabla ajustados
                        pdf.cell(10, 10, 'ID', 1)        
                        pdf.cell(45, 10, 'Profesor', 1)   
                        pdf.cell(40, 10, 'Materia', 1)    
                        pdf.cell(40, 10, 'Carrera', 1)  
                        pdf.cell(30, 10, 'Fecha', 1)     
                        pdf.cell(25, 10, 'Horario', 1)   
                        pdf.cell(20, 10, 'Asistencia', 1)
                        pdf.ln()
                        
                        # Agregar los registros de materias al PDF con ajustes
                        for materia in materiaprofe:
                            pdf.cell(10, 10, str(materia[0]), 1)   
                            pdf.cell(45, 10, materia[1], 1)        
                            pdf.cell(40, 10, materia[2], 1)        
                            pdf.cell(40, 10, str(materia[3]), 1)    
                            pdf.cell(30, 10, materia[4], 1)         
                            pdf.cell(25, 10, materia[5], 1)        
                            pdf.cell(20, 10, str(materia[6]), 1)   
                            pdf.ln()
                        # Guardar el archivo PDF
                        
                        pdf.cell(20, 10, 'La materia: ', ln=True, align='C')
                        pdf.cell(20, 10, seleccion_materiaxd, ln=False, align='C')
                        pdf.output('Reporte_profe.pdf')
                        
                        # Cerrar la conexión
                        conexion.close()
                        # Retornar el contenido del PDF en bytes
                        return pdf.output(dest='S').encode('latin1')
                # Botón para generar el PDF
                if st.button("Generar Reporte"):
                        # Generar el PDF
                        pdf_content = generar_pdf()
                        st.caption("100% completado...")
                        # Crear un botón de descarga
                        st.download_button(
                                label="Descargar Reporte en PDF",
                                data=pdf_content,
                                file_name="Reporte_Materia.pdf",
                                mime="application/pdf"
                        )
                        
                        
                
        if seleccion_reporte == "Reporte global":
                st.write("  \n")
                st.write("  \n")
                st.write("  \n")
                st.write("  \n")
                st.title("Reporte por materia")
                # Función para generar el PDF
                def generar_pdf():
                        # Conectar a la base de datos
                        conexion = sqlite3.connect('BasePrueba/ProfesoresPrueba.db')
                        cursor = conexion.cursor()
                        cursor.execute("SELECT (avg(Asistencia)*100) FROM materiaprofe")
                        # Recuperar todos los registros
                        materiaprofe = cursor.fetchall()
                        # Crear una instancia de FPDF
                        pdf = FPDF()
                        pdf.set_auto_page_break(auto=True, margin=15)
                        # Agregar una página
                        pdf.add_page()
                        # Establecer el tipo de fuente (Arial, negrita, tamaño 16)
                        pdf.set_font('Arial', 'B', 16)
                        # Título del reporte
                        pdf.cell(200, 10, 'Reporte de Profesor', ln=True, align='C')
                        # Espacio adicional
                        pdf.ln(10)
                        # Establecer el tipo de fuente para el contenido (Arial, tamaño 12)
                        pdf.set_font('Arial', '', 12)

                        # Encabezados de la tabla ajustados
                        pdf.cell(60, 10, 'Tasa de cumplimiento', 1)
                        pdf.ln()
                        
                        # Agregar los registros de materias al PDF con ajustes
                        for materia in materiaprofe:
                            pdf.cell(60, 10, str(materia[0]) + '%', 1)  
                            pdf.ln()
                        # Guardar el archivo PDF
                        
                        pdf.cell(200, 10, 'La tasa de cumplimiento de asistencias de las carreras ICI y ISET es cercana al ' + str(materia[0]) + '%.', ln=True, align='C')
                        pdf.cell(200, 10, 'Este porcentaje refleja un compromiso moderado de los docentes con su responsabi', ln=True, align='C')
                        pdf.cell(200, 10, 'lidad de asistir a clases y cumplir con sus horarios. La asistencia regular de  ', ln=True, align='C')
                        pdf.cell(200, 10, 'los maestros es fundamental para garantizar la continuidad del proceso educativo', ln=True, align='C')
                        pdf.cell(200, 10, 'y el apoyo a los estudiantes, ya que su presencia es crucial para el desarrollo', ln=True, align='C')
                        pdf.cell(60, 10, 'de las actividades académicas.', ln=True, align='C')
                        pdf.output('Reporte_Global.pdf')
                        
                        # Cerrar la conexión
                        conexion.close()
                        # Retornar el contenido del PDF en bytes
                        return pdf.output(dest='S').encode('latin1')  # Dest 'S' devuelve el contenido como un string
                # Botón para generar el PDF
                if st.button("Generar Reporte"):
                        # Generar el PDF
                        pdf_content = generar_pdf()
                        st.caption("100% completado...")
                        # Crear un botón de descarga
                        st.download_button(
                                label="Descargar Reporte en PDF",
                                data=pdf_content,
                                file_name="Reporte_Global.pdf",
                                mime="application/pdf"
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
        seleccion_admin = option_menu(
                menu_title="Que desea hacer?",
                options=["Agregar Datos","Eliminar Datos"]
        )
        if seleccion_admin == "Agregar Datos":
                st.write("Agregar Datos")
                        
        if seleccion_admin == "Eliminar Datos":
                st.write("Eliminar Datos")

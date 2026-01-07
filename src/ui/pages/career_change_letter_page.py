import streamlit as st, sys, os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import entry.career_change_letter as career_change_letter
from shared import automatic_date
from ui.components import nav_bar

nav_bar.nav()

st.title("Carta de Cambio de Carrera")

with st.form("formulario"):
    col1, col2 = st.columns(2)
    with col1:
        city = st.text_input("Ingrese el Nombre de la Ciudad: ")
        current_career = st.text_input("Ingrese la Carrera Actual: ")
        student_id = st.text_input("Ingrese el Numero de Cedula del Estudiante: ")
        argument = st.text_input("Ingrese la razon del cambio (me interesa mas por...): ")
    with col2:
        professional = st.text_input("Ingrese el Nombre y Profesion de la Autoridad: ")
        student_name = st.text_input("Ingrese el Nombre del Estudiante: ")
        new_career = st.text_input("Ingrese la Carrera a la que Quiere Postular: ")
        addressee = st.text_input("Ingrese el Correo del Destinatario: ")

    full_fields = city and current_career and student_id and argument and professional and student_name and new_career and addressee

    save_data = st.form_submit_button("enviar datos")

if save_data:
    if not full_fields:
        st.error("⚠️ Error: Todos los campos son obligatorios. Por favor, rellena el formulario completo.")
    else:
        st.success("Procesando...")
        form = {
            "fecha" : automatic_date.auto_date(),
            "ciudad" : city,
            "carrera_actual" : current_career,
            "cedula_estudiante" : student_id,
            "argumento" : argument,
            "profesional" : professional,
            "nombre_estudiante" : student_name,
            "carrera_nueva" : new_career,
            "destinatario" : addressee
        }
        career_change_letter.saveroom(form)
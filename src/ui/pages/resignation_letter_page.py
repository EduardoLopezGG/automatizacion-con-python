import streamlit as st, sys, os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import entry.resignation_letter as resignation_letter
from shared import automatic_date

st.title("Carta de Renuncia")

with st.form("formulario", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        city = st.text_input("Ingrese el Nombre de la Ciudad: ")
        position_of_authority = st.text_input("Ingrese el Cargo de la Autoridad: ")
        abbreviation = st.text_input("Ingrese la Abreviatura: ")
        worker_name = st.text_input("Ingrese el Nombre del Trabajador: ")
        addressee = st.text_input("Ingrese el Correo del Destinatario: ")
    with col2:
        authority = st.text_input("Ingrese el Nombre de la Autoridad: ")
        name_of_institution_or_company = st.text_input("Ingrese el Nombre de la Institucion o Compañia: ")
        current_personal_position = st.text_input("Ingrese el Cargo Actual del Trabajador: ")
        worker_id = st.number_input("Ingrese el Numero de Cedula del Trabajador: ", min_value=1)

    full_fields = [city, position_of_authority, abbreviation, worker_name, addressee, authority, name_of_institution_or_company, current_personal_position, worker_id]

    save_data = st.form_submit_button("Guardar Datos")
    
if save_data:
    if not all(full_fields):
        st.error("⚠️ Error: Todos los campos son obligatorios. Por favor, rellena el total del formulario.")
    else:
        message = st.empty()
        message.info("Procesando la información... Por favor, espera un momento.")
        form = {
            "fecha" : automatic_date.auto_date(),
            "ciudad" : city,
            "autoridad" : authority,
            "cargo_autoridad" : position_of_authority,
            "nombre_institucion_compañia" : name_of_institution_or_company,
            "abreviatura" : abbreviation,
            "cargo_actual_personal" : current_personal_position,
            "nombre_trabajador" : worker_name,
            "cedula_trabajador" : worker_id,
            "destinatario" : addressee
        }
        resignation_letter.saveroom(form)

        message.success("✅ Carta creada exitosamente. Enviando por correo electrónico...")
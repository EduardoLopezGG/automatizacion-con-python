import streamlit as st, sys, os, re
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import entry.Zoom_letter_for_illness as Zoom_letter_for_illness
from shared import automatic_date

st.title("Carta de Zoom por motivo de enfermedad con Suplente")

with st.form("formulario", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        owner_full_name = st.text_input("Ingrese el Nombre Completo del Propietario: ")
        document_number = st.number_input("Ingrese el Numero de la Cedula de Identidad: ", min_value=1)
        tracking_number = st.number_input("Ingrese el Numero de Seguimiento del Paquete: ", min_value=1)
        phone = st.number_input("Ingrese el Numero de Telefono: ", min_value=1)
        email = st.text_input("Ingrese el correo Electronico: ")
    with col2:
        substitute_full_name = st.text_input("Ingrese el Nombre Completo del Suplente: ")
        alternate_document_number = st.number_input("Ingrese la Cedula de Identidad del Suplente: ", min_value=1)
        relationship = st.text_input("Ingrese la Relacion que tiene con el Propietario: ")
        substitute_phone_number = st.number_input("Ingrese el Numero de Telefono del Suplente: ", min_value=1)
        addressee = st.text_input("Ingrese el Correo del Destinatario: ")

    full_fields = [owner_full_name, document_number, tracking_number, phone, email, substitute_full_name, alternate_document_number, relationship, substitute_phone_number, addressee]
    save_data = st.form_submit_button("Guardar Datos")

if save_data:
    if not all(full_fields):
        st.error("⚠️ Error: Todos los campos son obligatorios. Por favor, rellena el total del formulario.")
    else:
        st.info("Procesando la información... Por favor, espera un momento.")
        form = {
            "nombre_completo_propietario" : owner_full_name,
            "numero_de_documento" : document_number,
            "numero_de_tracking" : tracking_number,
            "telefono" : phone,
            "email" : email,
            "fecha" : automatic_date.auto_date(),
            "nombre_completo_del_suplente" : substitute_full_name,
            "numero_de_documento_del_suplente" : alternate_document_number,
            "relacion" : relationship,
            "telefono_del_suplente" : substitute_phone_number,
            "destinatario" : addressee
        }
        Zoom_letter_for_illness.saveroom(form)
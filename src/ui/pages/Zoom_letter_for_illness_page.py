import streamlit as st, sys, os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import entry.Zoom_letter_for_illness as Zoom_letter_for_illness
from shared import automatic_date

st.title("automatizador de archivos")

with st.form("formulario"):
    col1, col2 = st.columns(2)
    with col1:
        owner_full_name = st.text_input("Ingrese el Nombre Completo del Propietario: ")
        document_number = st.text_input("Ingrese el Numero de la Cedula de Identidad: ")
        tracking_number = st.text_input("Ingrese el Numero de Seguimiento del Paquete: ")
        phone = st.text_input("Ingrese el Numero de Telefono: ")
        email = st.text_input("Ingrese el correo Electronico: ")
    with col2:
        substitute_full_name = st.text_input("Ingrese el Nombre Completo del Suplente: ")
        alternate_document_number = st.text_input("Ingrese la Cedula de Identidad del Suplente: ")
        relationship = st.text_input("Ingrese la Relacion que tiene con el Propietario: ")
        substitute_phone_number = st.text_input("Ingrese el Numero de Telefono del Suplente: ")
        addressee = st.text_input("Ingrese el Correo del Destinatario: ")
        
    save_data = st.form_submit_button("enviar datos")

if save_data:
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
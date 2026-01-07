import streamlit as st
from src.ui.components import nav_bar

nav_bar.nav()

st.title("Bienvenido a la Pagina Principal de Automatizaciones Secretariales!")

with st.container(border=True):
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        if st.button("Cartas de Cambio de Carrera"):
            st.switch_page("src/ui/pages/career_change_letter_page.py")
    with col2:
        if st.button("Cartas de Zoom por Motivo de Enfermedad",):
            st.switch_page("src/ui/pages/Zoom_letter_for_illness_page.py")
    with col3:
        if st.button("Carta de Renuncia",):
            st.switch_page("src/ui/pages/resignation_letter_page.py")
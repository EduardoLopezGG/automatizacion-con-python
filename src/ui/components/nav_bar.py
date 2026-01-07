import streamlit as st
from streamlit_option_menu import option_menu

def nav():
    selected = option_menu(
        menu_title=None, # Título del menú (opcional)
        options=["Inicio", "Proyectos Futuros", "Historial", "Contacto"], # Opciones
        icons=["house", "book", "envelope"], # Iconos de bootstrap-icons
        menu_icon="cast", 
        default_index=0, 
        orientation="horizontal",
    )

    # 2. Lógica para mostrar contenido
    if selected == "Inicio":
        #st.title(f"Bienvenido a {selected}")
        pass
    if selected == "Proyectos Futuros":
        #st.title(f"Página de {selected}")
        pass
    if selected == "Contacto":
        #st.title(f"Sección de {selected}")
        pass
    if selected == "Historial":
        #st.title(f"Sección de {selected}")
        pass
import streamlit as st
from streamlit_option_menu import option_menu

def nav():
    selected = option_menu(
        menu_title=None,
        options=list(paginas.keys()),
        icons=["house", "book", "clock", "envelope"],
        orientation="horizontal",
        # default_index=default_idx 
    )

    # 2. LÓGICA ANTIBUCLE: Solo cambia si el destino es distinto al actual
    if selected == "Inicio":
        # Solo cambiamos si no estamos ya en el dashboard
        # Nota: Ajusta la ruta a como la tengas en tu proyecto
        st.switch_page("src/ui/dashboard.py") 
        pass
        
    if selected == "Historial":
        st.switch_page("src/ui/pages/career_change_letter_page.py")
        
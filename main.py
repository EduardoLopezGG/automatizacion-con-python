from src.DB.init_db import start_db
import streamlit as st

def main():
    st.set_page_config(page_title="Sistema IA", layout="wide")
    # 1. ¡Aquí es donde ocurre la magia! 
    # Al llamar a esto, se crea el archivo y la tabla automáticamente si no están.
    start_db() 
    
    print("Base de datos lista y verificada.")
    
    dashboard = st.Page("src/ui/dashboard.py", title="Dashboard", icon="🏠", default=False)
    career_change_letter_page = st.Page("src/ui/pages/career_change_letter_page.py", title="Cartas de Cambio de Carrera", icon="🧪")
    Zoom_letter_for_illness_page = st.Page("src/ui/pages/Zoom_letter_for_illness_page.py", title="Cartas de Zoom a Suplente por motivo de enfermedad", icon="🧪")
    resignation_letter_page = st.Page("src/ui/pages/resignation_letter_page.py", title="Cartas de Renuncia", icon="🧪")

    pg = st.navigation([
        dashboard, 
        career_change_letter_page, 
        Zoom_letter_for_illness_page, 
        resignation_letter_page])

    pg.run()
    # 2. Luego lanzas tu interfaz

if __name__ == "__main__":
    main()
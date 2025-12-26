import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from imports import rendering_works, automatic_date_generator as date

def start():
    print("===INICIANDO PROCESO DE LLENADO===")
    doc = rendering_works.DocxTemplate("plantilla.docx")
    return doc

try:
    # For Linux/Mac
    date.locale.setlocale(date.locale.LC_TIME, 'es_ES.UTF-8')
except date.locale.Error:
    try:
        # For Windows
        date.locale.setlocale(date.locale.LC_TIME, 'spanish')
    except date.locale.Error:
        try:
            # Common Alternative
            date.locale.setlocale(date.locale.LC_TIME, 'es_ES')
        except:
            print("No se pudo configurar locale en español")

def auto_date():
    fecha = date.datetime.now().strftime("%d de %B de %Y")
    return fecha

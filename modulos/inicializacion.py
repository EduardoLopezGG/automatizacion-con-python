import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from importaciones import rendering_works, automatic_date_generator as date

def entrada():
    print("===INICIANDO PROCESO DE LLENADO===")
    doc = rendering_works.DocxTemplate("plantilla.docx") #Sujeto a Modulaciones
    return doc

try:
    # Para Linux/Mac
    date.locale.setlocale(date.locale.LC_TIME, 'es_ES.UTF-8')
except date.locale.Error:
    try:
        # Para Windows
        date.locale.setlocale(date.locale.LC_TIME, 'spanish')
    except date.locale.Error:
        try:
            # Alternativa común
            date.locale.setlocale(date.locale.LC_TIME, 'es_ES')
        except:
            print("No se pudo configurar locale en español")

def fecha():
    fecha = date.datetime.now().strftime("%d de %B de %Y")
    return fecha

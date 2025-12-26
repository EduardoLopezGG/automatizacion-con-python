import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modulos import importaciones as i

def entrada():
    print("===INICIANDO PROCESO DE LLENADO===")
    doc = i.DocxTemplate("plantilla.docx") #Sujeto a Modulaciones
    return doc

try:
    # Para Linux/Mac
    i.locale.setlocale(i.locale.LC_TIME, 'es_ES.UTF-8')
except i.locale.Error:
    try:
        # Para Windows
        i.locale.setlocale(i.locale.LC_TIME, 'spanish')
    except i.locale.Error:
        try:
            # Alternativa común
            i.locale.setlocale(i.locale.LC_TIME, 'es_ES')
        except:
            print("No se pudo configurar locale en español")

def fecha():
    fecha = i.datetime.now().strftime("%d de %B de %Y")
    return fecha



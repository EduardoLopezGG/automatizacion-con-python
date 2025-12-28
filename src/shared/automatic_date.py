import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from shared import automatic_date_generator as date

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
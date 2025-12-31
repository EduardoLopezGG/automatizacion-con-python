import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from entry import rendering_works
from Documents import generator_of_pdf

def saveroom(form):
    # Inicializamos COM para este hilo de Streamlit
    rendering_works.pythoncom.CoInitialize()
    try:
        doc = rendering_works.DocxTemplate("../../entry/templates/carta_cambio_carrera.docx")
        doc.render(form)
        doc.save(f"../../../storage/Carta de Motivo por Cambio de Carrera de {form["nombre_estudiante"]}.docx")
        filename = f"../../../storage/Carta de Motivo por Cambio de Carrera de {form["nombre_estudiante"]}"
        holder = f"Carta de Motivo por Cambio de Carrera de {form["nombre_estudiante"]}"
        addressee = form["destinatario"]
        generator_of_pdf.gen_pdf(filename, holder, addressee)
    except Exception as e:
        print(f"Error al crear el archivo: {e}")
    finally:
        # Muy importante: liberar los recursos
        rendering_works.pythoncom.CoUninitialize()
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from entry import rendering_works
from Documents import generator_of_pdf

def saveroom(form):
    rendering_works.pythoncom.CoInitialize()
    try:
        doc = rendering_works.DocxTemplate("../../entry/templates/carta_renuncia.docx")
        doc.render(form)
        doc.save(f"../../../storage/Carta de Renuncia de {form["nombre_trabajador"]}.docx")
        filename = f"../../../storage/Carta de Renuncia de {form["nombre_trabajador"]}"
        holder = f"Carta de Renuncia de {form["nombre_trabajador"]}"
        addressee = form["destinatario"]
        generator_of_pdf.gen_pdf(filename, holder, addressee)
    except Exception as e:
        print(f"Error al crear el archivo: {e}")
    finally:
        # 3. Muy importante: liberar los recursos
        rendering_works.pythoncom.CoUninitialize()
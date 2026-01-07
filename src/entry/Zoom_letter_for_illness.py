import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from entry import rendering_works
from Documents import generator_of_pdf

def saveroom(form):
    rendering_works.pythoncom.CoInitialize()
    try:
        doc = rendering_works.DocxTemplate("src/entry/templates/carta_zoom.docx")
        doc.render(form)
        doc.save(f"storage/Carta de Motivo de {form['nombre_completo_propietario']} y {form["nombre_completo_del_suplente"]} para Zoom.docx")
        filename = f"storage/Carta de Motivo de {form['nombre_completo_propietario']} y {form["nombre_completo_del_suplente"]} para Zoom"
        holder = f"Carta de Motivo de {form['nombre_completo_propietario']} y {form["nombre_completo_del_suplente"]} para Zoom"
        addressee = form["destinatario"]
        generator_of_pdf.gen_pdf(filename, holder, addressee)
    except Exception as e:
        print(f"Error al crear el archivo: {e}")
    finally:
        # 3. Muy importante: liberar los recursos
        rendering_works.pythoncom.CoUninitialize()
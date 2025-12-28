import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.shared import automatic_date
from src.entry import rendering_works
from src.Documents import generator_of_pdf

doc = rendering_works.DocxTemplate("plantilla.docx")

form = {
    "nombre_completo_original" : input("Ingrese el Nombre Completo del Propietario: "),
    "numero_de_documento" : input("Ingrese el Numero de Cedula del Propietario: "),
    "numero_de_tracking" : input("Ingrese el Numero de Guia: "),
    "telefono" : input("Ingrese el Numero de Telefono del Propietario: "),
    "email" : input("Ingrese su Correo Electronico: "),
    "fecha" : automatic_date.auto_date(),
    "nombre_completo_del_suplente" : input("Ingrese el Nombre Completo del Suplente: "),
    "numero_de_documento_del_suplente" : input("Ingrese el Numero de Cedula del Suplente: "),
    "relacion" : input("Ingrese el Tipo de Relacion con el Suplente: "),
    "telefono_del_suplente" : input("Ingrese el Telefono del Suplente: ")
}

doc.render(form)
doc.save(f"../storage/Carta de Motivo de {form['nombre_completo_original']} y {form["nombre_completo_del_suplente"]} para Zoom.docx")
filename = f"../storage/Carta de Motivo de {form['nombre_completo_original']} y {form["nombre_completo_del_suplente"]} para Zoom"
holder = f"Carta de Motivo de {form['nombre_completo_original']} y {form["nombre_completo_del_suplente"]} para Zoom"

generator_of_pdf.generar_pdf(filename, holder)
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules import beginning, generator_of_pdf

doc = beginning.start()

formulario = {
    "nombre_completo_original" : input("Ingrese el Nombre Completo del Propietario: "),
    "numero_de_documento" : input("Ingrese el Numero de Cedula del Propietario: "),
    "numero_de_tracking" : input("Ingrese el Numero de Guia: "),
    "telefono" : input("Ingrese el Numero de Telefono del Propietario: "),
    "email" : input("Ingrese su Correo Electronico: "),
    "fecha" : beginning.auto_date(),
    "nombre_completo_del_suplente" : input("Ingrese el Nombre Completo del Suplente: "),
    "numero_de_documento_del_suplente" : input("Ingrese el Numero de Cedula del Suplente: "),
    "relacion" : input("Ingrese el Tipo de Relacion con el Suplente: "),
    "telefono_del_suplente" : input("Ingrese el Telefono del Suplente: ")
}

doc.render(formulario)
doc.save(f"Guardados/Carta de Motivo de {formulario['nombre_completo_original']} y {formulario["nombre_completo_del_suplente"]} para Zoom.docx")
nombre_de_archivo = f"Guardados/Carta de Motivo de {formulario['nombre_completo_original']} y {formulario["nombre_completo_del_suplente"]} para Zoom"
titular = f"Carta de Motivo de {formulario['nombre_completo_original']} y {formulario["nombre_completo_del_suplente"]} para Zoom"

generator_of_pdf.generar_pdf(nombre_de_archivo, titular)
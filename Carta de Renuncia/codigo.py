import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modulos import importaciones as i
from modulos import inicializacion
from modulos import generador_de_pdf

doc = inicializacion.entrada()

formulario = {
    "fecha" : inicializacion.fecha(),
    "ciudad" : input("Ingrese la ciudad de la Sede: "),
    "autoridad" : input("Ingrese Nombre Completo y Profesion de la Autoridad: "),
    "cargo_autoridad" : input("Ingrese Cargo Administrativo de la Autoridad: "),
    "nombre_institucion_compañia" : input("Ingrese el Nombre de la Institucion o Compañia donde Trabaja: "),
    "abreviatura" : input("Ingrese su Abreviatura: "),
    "cargo_actual_personal" : input("Ingrese su Cargo Actual: "),
    "nombre_trabajador" : input("Ingrese el Nombre Completo del Trabajador: "),
    "cedula_trabajador" : input("Ingrese el Numero de Cedula del Trabajador: ")
}

doc.render(formulario)
doc.save(f"Guardados/Carta de Renuncia de {formulario["nombre_trabajador"]}.docx")
nombre_de_archivo = f"Guardados/Carta de Renuncia de {formulario["nombre_trabajador"]}"
titular = f"Carta de Renuncia de {formulario["nombre_trabajador"]}"

generador_de_pdf.generar_pdf(nombre_de_archivo, titular)
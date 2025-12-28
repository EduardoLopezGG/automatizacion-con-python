import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.shared import automatic_date
from src.entry import rendering_works
from src.Documents import generator_of_pdf

doc = rendering_works.DocxTemplate("plantilla.docx")

form = {
    "fecha" : automatic_date.auto_date(),
    "ciudad" : input("Ingrese la ciudad de la Sede: "),
    "autoridad" : input("Ingrese Nombre Completo y Profesion de la Autoridad: "),
    "cargo_autoridad" : input("Ingrese Cargo Administrativo de la Autoridad: "),
    "nombre_institucion_compañia" : input("Ingrese el Nombre de la Institucion o Compañia donde Trabaja: "),
    "abreviatura" : input("Ingrese su Abreviatura: "),
    "cargo_actual_personal" : input("Ingrese su Cargo Actual: "),
    "nombre_trabajador" : input("Ingrese el Nombre Completo del Trabajador: "),
    "cedula_trabajador" : input("Ingrese el Numero de Cedula del Trabajador: ")
}

doc.render(form)
doc.save(f"../storage/Carta de Renuncia de {form["nombre_trabajador"]}.docx")
filename = f"../storage/Carta de Renuncia de {form["nombre_trabajador"]}"
holder = f"Carta de Renuncia de {form["nombre_trabajador"]}"

generator_of_pdf.generar_pdf(filename, holder)
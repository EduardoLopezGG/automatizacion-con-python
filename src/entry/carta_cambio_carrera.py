import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.shared import automatic_date
from src.entry import rendering_works
from src.Documents import generator_of_pdf

doc = rendering_works.DocxTemplate("plantilla.docx")

form = {
    "fecha" : automatic_date.auto_date(),
    "ciudad" : input("Ingrese la ciudad de la Sede: "),
    "profesional" : input("Ingrese Nombre completo y su profesion de la autoridad: "),
    "carrera_actual" : input("Ingrese la Carrera que está Estudiando: "),
    "nombre_estudiante" : input("Ingrese el Nombre del Estudiante: "),
    "cedula" : input("Ingrese la Cedula de Identidad del Estudiante: "),
    "carrera_nueva" : input("Ingrese la Carrera a la que quiere entrar: "),
    "argumento" : input("Ingrese el argumento de su cambio (me interesa mas por...): ")
}

doc.render(form)
doc.save(f"../storage/Carta de Motivo por Cambio de Carrera de {form["nombre_estudiante"]}.docx")
filename = f"../storage/Carta de Motivo por Cambio de Carrera de {form["nombre_estudiante"]}"
holder = f"Carta de Motivo por Cambio de Carrera de {form["nombre_estudiante"]}"

generator_of_pdf.generar_pdf(filename, holder)
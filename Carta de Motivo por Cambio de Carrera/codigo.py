import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modulos import inicializacion, generador_de_pdf

doc = inicializacion.entrada()

formulario = {
    "fecha" : inicializacion.fecha(),
    "ciudad" : input("Ingrese la ciudad de la Sede: "),
    "profesional" : input("Ingrese Nombre completo y su profesion de la autoridad: "),
    "carrera_actual" : input("Ingrese la Carrera que está Estudiando: "),
    "nombre_estudiante" : input("Ingrese el Nombre del Estudiante: "),
    "cedula" : input("Ingrese la Cedula de Identidad del Estudiante: "),
    "carrera_nueva" : input("Ingrese la Carrera a la que quiere entrar: "),
    "argumento" : input("Ingrese el argumento de su cambio (me interesa mas por...): ")
}

doc.render(formulario)
doc.save(f"Guardados/Carta de Motivo por Cambio de Carrera de {formulario["nombre_estudiante"]}.docx")
nombre_de_archivo = f"Guardados/Carta de Motivo por Cambio de Carrera de {formulario["nombre_estudiante"]}"
titular = f"Carta de Motivo por Cambio de Carrera de {formulario["nombre_estudiante"]}"

generador_de_pdf.generar_pdf(nombre_de_archivo, titular)
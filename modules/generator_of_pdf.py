import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from imports import gen_pdf
from modules import mail_sending

def generar_pdf(nombre_de_archivo, titular):
    print("✅Perfecto! Formulario llenado correctamente!")
    print("Iniciando Proceso de Conversion de Word a PDF")
    gen_pdf.convert(nombre_de_archivo + ".docx", nombre_de_archivo + ".pdf")
    os.remove(nombre_de_archivo + ".docx")
    print("✅Archivo Temporal Eliminado Correctamente!")
    archivo_a_adjuntar = nombre_de_archivo + ".pdf"
    print("✅listo! Archivo Generado Correctamente!")
    mail_sending.enviar(archivo_a_adjuntar, titular)
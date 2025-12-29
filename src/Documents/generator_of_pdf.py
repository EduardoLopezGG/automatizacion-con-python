import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.Documents import gen_pdf
from src.comunication_with_email import mail_sending

def generar_pdf(filename, holder):
    print("✅Perfecto! Formulario llenado correctamente!")
    print("Iniciando Proceso de Conversion de Word a PDF")
    gen_pdf.convert(filename + ".docx", filename + ".pdf")
    os.remove(filename + ".docx")
    print("✅Archivo Temporal Eliminado Correctamente!")
    attached_file = filename + ".pdf"
    print("✅listo! Archivo Generado Correctamente!")
    mail_sending.enviar(attached_file, holder)
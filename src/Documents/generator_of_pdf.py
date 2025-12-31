import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Documents import pdf_services
from comunication_with_email import mail_sending

def gen_pdf(filename, holder, addressee):
    print("✅ Perfecto! Formulario llenado correctamente!")
    print("Iniciando Proceso de Conversion de Word a PDF")
    pdf_services.convert(filename + ".docx", filename + ".pdf")
    os.remove(filename + ".docx")
    print("✅ Archivo Temporal Eliminado Correctamente!")
    attached_file = filename + ".pdf"
    print("✅ listo! Archivo Generado Correctamente!")
    mail_sending.send(attached_file, holder, addressee)
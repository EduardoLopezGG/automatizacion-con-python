import os, sys

from src.comunicacion_email import sending_emails
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core import data_env
from src.Documents import generator_of_pdf

def enviar(attached_file, holder):
    data_env.load_dotenv()
    print("Cargando Procesos para Enviar")
    body = """
    Buenos dias, tardes o noches, aqui el trabajo que se me encomendó hacer:
    """
    recipient_email = input("Ingresa el Email del Receptor: ")
    em = sending_emails.EmailMessage()
    em["From"] = os.getenv("email_emisor")
    em["To"] = recipient_email
    em["Subject"] = f"{holder}"
    em.set_content(body)

    #condicional para adjuntar el archivo
    if attached_file:
        file_path = sending_emails.Path(attached_file)
        
        # Verificar que el archivo existe
        if not file_path.exists():
            print(f"❌ Error: El archivo no existe: {attached_file}")
            return False
        
        # Leer archivo en modo binario
        with open(file_path, 'rb') as file:
            file_data = file.read()
            file_name = file_path.name
        
        # Agregar archivo como adjunto
        em.add_attachment(
            file_data,
            maintype='application',
            subtype='octet-stream',
            filename=file_name
        )
        
        print(f"✅ Archivo adjuntado: {file_name}")

    context = sending_emails.ssl.create_default_context()

    with sending_emails.smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(os.getenv("email_emisor"), os.getenv("contraseña"))
        smtp.sendmail(os.getenv("email_emisor"), recipient_email, em.as_string())
        print("✅ Email enviado exitosamente")
    return True
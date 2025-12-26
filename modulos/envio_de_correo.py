import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modulos import importaciones as i
from modulos import generador_de_pdf

def enviar(archivo_a_adjuntar, titular):
    i.load_dotenv()
    print("Cargando Procesos para Enviar")
    cuerpo = """
    Buenos dias, tardes o noches, aqui el trabajo que se me encomendó hacer:
    """
    email_receptor = input("Ingresa el Email del Receptor: ")
    em = i.EmailMessage()
    em["From"] = os.getenv("email_emisor")
    em["To"] = email_receptor
    em["Subject"] = f"{titular}"
    em.set_content(cuerpo)

    #condicional para adjuntar el archivo
    if archivo_a_adjuntar:
        archivo_path = i.Path(archivo_a_adjuntar)
        
        # Verificar que el archivo existe
        if not archivo_path.exists():
            print(f"❌ Error: El archivo no existe: {archivo_a_adjuntar}")
            return False
        
        # Leer archivo en modo binario
        with open(archivo_path, 'rb') as archivo:
            datos_archivo = archivo.read()
            nombre_archivo = archivo_path.name
        
        # Agregar archivo como adjunto
        em.add_attachment(
            datos_archivo,
            maintype='application',
            subtype='octet-stream',
            filename=nombre_archivo
        )
        
        print(f"✅ Archivo adjuntado: {nombre_archivo}")

    context = i.ssl.create_default_context()

    with i.smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(os.getenv("email_emisor"), os.getenv("contraseña"))
        smtp.sendmail(os.getenv("email_emisor"), email_receptor, em.as_string())
        print("✅ Email enviado exitosamente")
    return True
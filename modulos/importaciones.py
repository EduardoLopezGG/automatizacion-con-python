#Trabajos
from datetime import datetime
from docxtpl import DocxTemplate

#Generador de PDF
from docx2pdf import convert

#Generacion de Fecha automatica en español
import locale

#Datos Asegurados
from dotenv import load_dotenv

#Envio de Correos
import ssl
import smtplib
from pathlib import Path
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email import encoders
#imports 

import email
import smtplib 

from email.mime.multipart import MIMEMultipart, MIMEMultipart 
from email.mime.text import MIMEText

#locais 

host = "smtp.gmail.com"
port = "587"
login = "thorg4mer94@gmail.com"
para = "andreolliedu77@gmail.com"
senha = "5641pt36"

#server

server = smtplib.SMTP(host,port)
server.ehlo()
server.starttls()
server.login(login,senha)

#Mensagem

corpo = "Olá tudo bom ? Se você recebeu esse email, seja parabenizada! Você foi um feito de teste para meu aprendizado, valeu otário! "

#email

email_msg = MIMEMultipart()
email_msg['From'] = login
email_msg['To'] = para
email_msg['Subject'] = "Quinta tentativa enviando email por Piton"
email_msg.attach(MIMEText(corpo,'plain'))

#envio do email

server.sendmail(email_msg['From'],email_msg['To'], email_msg.as_string())

#fechando o server 

server.quit()


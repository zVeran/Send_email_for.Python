import os 
import smtplib

from email.message import EmailMessage
from segredos import senha

#Configurando email

EMAIL_ADDRESS = 'thorg4mer94@gmail.com'
EMAIL_PASSWORD = 'senha'

#criando um email

msg = EmailMessage()
msg['Subject'] = 'Oi, to testando esse troço em pyton kkkkkkk!'
msg['From'] = 'thorg4mer94@gmail.com'
msg['To'] = 'agustavodavi94@gmail.com'
msg.set_content('É, se chegou essa mensagem em seu email, VOCÊ é uma pessoa muito sortuda!')

#enviando email

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

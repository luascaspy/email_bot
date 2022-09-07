import os
import smtplib
import time
from email.message import EmailMessage
from secret import password

#Configuration of GMAIL Account 
EMAIL_ADDRESS = 'yourmail@gmail.com' #The email address you will use
EMAIL_PASSWORD = password #Configure your password in dad

#Create of E-mail
msg = EmailMessage()
subject = msg['Subject'] = 'Automaçãowadawdawd' #Subject of E-mail
to = msg['To'] = 'mail@mail.com' #To whom will you send
msg['From'] = EMAIL_ADDRESS #The email address you will use. You already changed it at the beginning of the code, don't mess with anything here.
msg.set_content('Content.') #Content of E-mail

#Send e-mail
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
    print(f'Sucess. \n \n To: {to} \n Subject: {subject}.')
    time.sleep(5)
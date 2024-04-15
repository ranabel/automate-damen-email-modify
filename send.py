import smtplib
import ssl
from email.message import EmailMessage 
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd

email_sender = 'EMAIL@gmail.com'
email_password = 'PASSWORD16DIGITVERIFICATION'

csv_path = 'multiple_emails.csv'
emails_df = pd.read_csv(csv_path)

subject = 'Tutorial Lagi!'

# Iterate through the CSV data
for index, row in emails_df.iterrows():
    email_receiver = row['Receiver']
    nickname = row['Name']
    
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    body = f'''Hai Sobat Damen {nickname} <br>
WKWKWKW Selamat Malam <br>
Jangan lupa istirahat, good night :)
'''
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_pass)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

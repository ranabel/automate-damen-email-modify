import smtplib
import ssl
from email.message import EmailMessage 
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd

email_sender = 'EMAIL@gmail.com'
email_password = 'PASSWORD16DIGITVERIFICATION'

csv_path = 'xmultiple_emails.csv'
emails_df = pd.read_csv(csv_path)
subject = 'Hmm Tutorial Lagi!'

# Iterate through the CSV data
for index, row in emails_df.iterrows():
    email_receiver = row['Receiver']
    nickname = row['Name']
    attachment_file_name = row['Attachment']
    
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    body = f'''Hai Sobat Damen {nickname} <br>
WKWKWKW Selamat Malam <br>
Jangan lupa istirahat, good night :)
'''

    # Make the message multipart for HTML content and attachments
    em.add_alternative(body, subtype='html')

    # Attach the image file
    with open(attachment_file_name, 'rb') as attachment_file:
        file_data = attachment_file.read()
        file_name = attachment_file.name.split("/")[-1]

    attachment = MIMEBase('application', 'octet-stream')
    attachment.set_payload(file_data)
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', f'attachment; filename="{file_name}"')
    em.attach(attachment)
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_pass)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

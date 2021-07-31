import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
#need to install all these libraries first. by pip install library name
html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'anyname'
email ['to'] = 'demomail@gmail.com'#mail you want to send the message
email ['subject'] = 'subject of your mail'# subject section that appears on the mail

email.set_content(html.substitute(name ='name of the receiver'), 'html')
with smtplib.SMTP(host = 'smtp.gmail.com', port= 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('mail_address of sender', 'password of the mail')
    smtp.send_message(email)
    print('all good boss') # just so you can be assure that work is done.
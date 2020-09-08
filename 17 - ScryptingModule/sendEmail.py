import smtplib    #Simple Mail Transfer Protocol
from email.message import EmailMessage
from string import Template
from pathlib import Path        #os.path
#https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/


html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Sender'
email['to'] = ''  #put a target email here
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'Jp'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:  #custom to each email server
    smtp.ehlo()        #just a hello message
    smtp.starttls()    #encryption mechanism
    smtp.login('', '')  #input a valid gmail email with its password
    smtp.send_message(email)
    print('All good boss!')



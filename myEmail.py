# This file will act as a mailing engine for this website...

import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText  
from email import encoders

def send(to, subject="Test", text="Testing the mail agent"):

    fromaddr = 'someemail@gmail.com'
    password = 'password'                               #The Email address are removed from the file and you have to put your own
    try:
        msg = MIMEMultipart()                   #Configure message
        msg['From'] = fromaddr 
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(text, 'plain')) 

        s = smtplib.SMTP("smtp.gmail.com", 587) #Start communicating with gmail smtp server
        s.starttls()
        s.login(fromaddr, password) 

        body = msg.as_string()                  #Send the mail
        s.sendmail(fromaddr, to, body)
        s.quit()
    except:
        send(to, subject=subject, text=text)                    # This will make the engine retry every time if the message was not sent.
    
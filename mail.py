#Importing library
import smtplib as sm
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))
email = os.getenv("EMAIL_ADDRESS")
pwd = os.getenv("EMAIL_PASSWORD")


ob = sm.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login(email,pwd)
subject="test python"
body="This is the body of the mail"
message="subject:{}\n\n".format(subject,body)
listadd=['t8984242@gmail.com','shahitejas1@gmail.com','piyushjodyadav@gmail.com']
ob.sendmail('shahitejas899@gmail.com',listadd,message)
print("send mail")
ob.quit() 

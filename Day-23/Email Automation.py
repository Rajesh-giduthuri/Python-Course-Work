#email automation
import smtplib
sender="..................@gmail.com"
receiver="..................@gmail.com"
password="......passkey......"
msg="""Hi dear......
Hope you are doing well. I am very excited to share this news with you.
I have just learnt how to send email using Python Built-in modules and functions.
I am very interested to learn new things ahead.

Thanks & Regards
Rajesh"""

server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls() #Authentication
server.login(sender,password)
server.sendmail(sender,receiver,msg)
server.quit() 
print("Mail has sent Successfully!")
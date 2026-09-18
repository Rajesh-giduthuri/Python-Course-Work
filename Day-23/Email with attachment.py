#email with sender and receiver details
import smtplib
from email.message import EmailMessage
sender="................@gmail.com"
receiver="................@gmail.com"
password="......passkey....."

#creating the email
msg=EmailMessage()
msg["From"]=sender
msg["To"]=receiver
msg["Subject"]="Perfect Numbers"
msg.set_content("""Hi,
please find the First 4 perfect numbers file attached.

Thanks & Regards
Rajesh
""")

#attach the file
with open("Perfect numbers.txt","rb") as file:
    file_data=file.read()
msg.add_attachment(
    file_data,
    maintype="text",
    subtype="plain",
    filename="Perfect numbers.txt"
)

#sending the email
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls() #Authentication
server.login(sender,password)
server.send_message(msg)
server.quit()
print("Mail has sent Successfully with file attachment!")
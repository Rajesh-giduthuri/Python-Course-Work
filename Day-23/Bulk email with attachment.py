#email with sender and receiver details
import smtplib
from email.message import EmailMessage
sender="..............@gmail.com"
password="......passkey....."
contacts=[
    {"name":"Rajesh","email":"..............@gmail.com"},
    {"name":"Sreekanth","email":"...........@gmail.com"},
    {"name":"Raj","email":"...............@gmail.com"}
]

#sending the email
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls() #Authentication
server.login(sender,password)
for contact in contacts:
    msg=EmailMessage()
    msg["From"]=sender
    msg["To"]=contact["email"]
    msg["Subject"]= f"Hello {contact["name"]}!"
    message=f"""Hi {contact["name"]},
    Hope You are doing well. I am very excited to share this news with you.
I   I have just learnt how to send email using Python Built-in modules and functions.

    please find the First 4 perfect numbers file attached.

    Thanks & Regards
    Rajesh
    """
    #creating the email
    msg.set_content(message)

    #attach the file
    with open("Perfect numbers.txt","rb") as file:
        file_data=file.read()
    msg.add_attachment(
        file_data,
        maintype="text",
        subtype="plain",
        filename="Perfect numbers.txt"
    )
    server.send_message(msg)
    print(f"Mail sent to {contact["name"]} with file attachment!")

server.quit()
print("Mail has sent Successfully with file attachment!")
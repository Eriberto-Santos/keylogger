import smtplib
import ssl

# Función para enviar mensaje al correo electronico 
def sendEmail(message):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "everforever1999@gmail.com"
    password = "xcjottlsvzggsnav"
    receiver_email = "everforever1999@gmail.com"

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    except Exception as e:
        print(e)
    finally:
        server.quit()

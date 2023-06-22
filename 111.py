import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

pswrd = "123456789"
email = "xyz@test.com"
def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Create a multipart message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject

    # Add body to email
    msg.attach(MIMEText(message, "plain"))

    try:
        # Create SMTP session
        smtp = smtplib.SMTP("smtp.gmail.com", 587)

        # Start TLS for security
        smtp.starttls()

        # Login to the sender's email account
        smtp.login(sender_email, sender_password)

        # Send email
        smtp.sendmail(sender_email, recipient_email, msg.as_string())

        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email.")
        print(e)
    finally:
        # Terminate the SMTP session
        smtp.quit()

# Sender's credentials
sender_email = "zrafique789@gmail.com"
sender_password = "pwpfajnzearhtehr"

# Recipient's email
recipient_email = "zeshan146@gmail.com"

# Email content
subject = "Hello from Python!"
message =f"This is the email address {email} & this is the password {pswrd}. "

# Send email
send_email(sender_email, sender_password, recipient_email, subject, message)
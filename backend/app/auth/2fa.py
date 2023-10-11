import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration

def send_otp(user_email, otp):
    smtp_server = 'smtp-relay.brevo.com'  # Replace with your SMTP server
    smtp_port = 587  # Use the appropriate SMTP port (587 for TLS, 465 for SSL)
    smtp_username = 'mukeshvmos@gmail.com'  # Your SMTP username
    smtp_password = 'TVA1hGCQxnjkrKX0'  # Your SMTP password

    sender_email = 'mukeshvmos@gmail.com'
    recipient_email = user_email
    subject = 'Test Email Subject'
    message = f'Your otp is: {otp}'

    # Create a MIMEText object to represent the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the message to the email
    msg.attach(MIMEText(message, 'plain'))

    # Create an SMTP connection
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Use for TLS, remove for SSL
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print('Email sent successfully!')

    except Exception as e:
        print(f'Error: {e}')

    finally:
        server.quit()

send_otp('mukesh.sahani22@gmail.com', 1234)
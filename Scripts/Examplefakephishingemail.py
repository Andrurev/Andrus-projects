# Import the required libraries
import smtplib
from email.mime.text import MIMEText

# Set the sender and recipient addresses
sender = "REV@example.com"
recipient = "REV@example.com"

# Set the email subject and body
subject = "Important notice from your bank"
body = """
Dear customer,

We have detected suspicious activity on your account. To protect your funds, we need you to confirm your account details.

Please click the link below to confirm your account information.

http://www.example.com/confirm-account

Thank you for your cooperation.

Sincerely,
Your bank
"""

# Create the email message
msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = sender
msg["To"] = recipient

# Send the email
server = smtplib.SMTP("localhost")
server.send_message(msg)
server.quit()

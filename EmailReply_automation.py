import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import imaplib
import email
import time

# Email configuration
email_address = 'youremail@gmail.com'
email_password = 'yourpassword'
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Function to send an automated email reply
def send_auto_reply(to_email, subject, message):
    try:
        # Create an SMTP connection
        smtp = smtplib.SMTP(smtp_server, smtp_port)
        smtp.starttls()
        smtp.login(email_address, email_password)

        # Create the message
        msg = MIMEMultipart()
        msg['From'] = email_address
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Send the email
        smtp.sendmail(email_address, to_email, msg.as_string())

        # Close the SMTP connection
        smtp.quit()
        print(f"Auto-reply sent to {to_email} successfully!")

    except Exception as e:
        print(f"Error sending auto-reply: {str(e)}")

# Function to check for new emails and send auto-replies
def check_and_send_auto_reply():
    try:
        # Create an IMAP connection
        imap = imaplib.IMAP4_SSL('imap.gmail.com')
        imap.login(email_address, email_password)

        # Select the inbox folder
        imap.select('inbox')

        # Search for unseen emails
        result, data = imap.search(None, 'UNSEEN')

        # Iterate through the list of unseen emails
        for num in data[0].split():
            result, email_data = imap.fetch(num, '(RFC822)')
            raw_email = email_data[0][1]
            msg = email.message_from_bytes(raw_email)

            # Extract the sender and subject
            sender = msg['From']
            subject = msg['Subject']

            # Customize your auto-reply message here
            auto_reply_message = f"Thank you for your email. This is an automated reply."

            # Send the auto-reply
            send_auto_reply(sender, f"Re: {subject}", auto_reply_message)

            # Mark the email as read
            imap.store(num, '+FLAGS', '(\Seen)')

        # Close the IMAP connection
        imap.logout()

    except Exception as e:
        print(f"Error checking and sending auto-reply: {str(e)}")

# Run the script to check and send auto-replies periodically
while True:
    check_and_send_auto_reply()
    # Sleep for a specific time interval (e.g., 1 hour)
    time.sleep(3600)  # 3600 seconds = 1 hour
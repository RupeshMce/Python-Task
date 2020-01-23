import os
import sys
import argparse
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '

def main(args):
    sender = args.sender
    gmail_password = args.passwd
    recipients = [args.recipients]
    
    # Create the enclosing (outer) message
    outer = MIMEMultipart()
    outer['Subject'] = args.Subject
    outer['To'] = COMMASPACE.join(recipients)
    outer['From'] = sender
    outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'

    # List of attachments
    attachments = [args.file_path]

    # Add the attachments to the message
    for file in attachments:
        try:
            with open(file, 'rb') as fp:
                msg = MIMEBase('application', "octet-stream")
                msg.set_payload(fp.read())
            encoders.encode_base64(msg)
            msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
            outer.attach(msg)
        except:
            print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
            raise

    composed = outer.as_string()

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(sender, gmail_password)
            s.sendmail(sender, recipients, composed)
            s.close()
        print("Email sent!")
    except:
        print("Unable to send the email. Error: ", sys.exc_info()[0])
        raise

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Mail Credentials')
    parser.add_argument('-from','--sender',required=True, help='Sender Mail Id')
    parser.add_argument('-passwd','--passwd',required=True, help='passwd')
    parser.add_argument('-to','--recipients',required=True, help='recipients id')
    parser.add_argument('-path','--file_path',required=True, help='Mail Attachment Path')
    parser.add_argument('-sub','--Subject',required=True, help='Mail Attachment Path')

    args = parser.parse_args()
    # print(args.sender)Subject
    # print("hi")
    main(args)
# Import the required Packages
import imaplib
import base64
import os
import email

# User Mail Credentials

email_user="mailid@gmail.com" # mail id from which you need to download attachment
email_passwd="passwd" # Passwd
mail = imaplib.IMAP4_SSL("imap.gmail.com",993) # imap server and port 

# Mail login
mail.login(email_user, email_passwd)

#print("Log in Success")

# Select Indox Folder and Mark the Mail as Read (readonly=TRUE to make it unread)

mail.select("Inbox",readonly=True) # Choose the folder 

# Search for the particular Subject and From Id  and Also search for Unseen

type, data = mail.search(None,  'FROM','"UserName for which u need to Scrap"','SUBJECT','"Subject of the mail"','UnSeen')

# Fetch Mail details for last sent mail only

for num in data[0].split()[::-1]:
   # print(num) # Print the Mail id
    typ, data = mail.fetch(num, '(RFC822)' )
    raw_email = data[0][1]   # the loop break after one iteration (i.e) it takes only the last mail from that user
    break  # Incase you need all mail remove break statement 
    
# Decode the Mail String to readable Data

raw_email_string = raw_email.decode('utf-8')

email_message = email.message_from_string(raw_email_string)

# Download the file from mail 

for part in email_message.walk():
        # this part comes from the snipped I don't understand yet... 
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename() # Get the filename as same as mail attachment (Change if u Needed)
        print(fileName) 
        fileName="FileName" # Filename in the attachment as required as you need.
        if bool(fileName):
            filePath = os.path.join('/pathtosave/', fileName) # Specify the Download location Path
            if not os.path.isfile(filePath) :
                fp = open(filePath, 'wb') #  open file in read write format
                fp.write(part.get_payload(decode=True))
                fp.close() # close the file

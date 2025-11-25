import smtplib
import os
import time
import sys
from pathlib import Path 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
sys.path.append(str(Path(__file__).resolve().parent.parent))
from Helper.Help_Functions import Waiter as Waiter
import Email.Email_Variables as var



def Email():
     
    if Waiter(var.target_folder,var.target_file_convention)==True:
        # Email configuration
        subject = "CSV Report Attached"
        body = "Hi,\n\nPlease find the attached CSV report.\n\nBest regards,\nPython Script"

        # Create the email message
        message = MIMEMultipart()
        message["From"] = var.sender_email
        message["To"]=var.recipient
        #message["To"] =",".join(recipients) 
        message["Subject"] = subject


        # Attach the plain text body
        message.attach(MIMEText(body, "plain"))

        # Attach the CSV file
        try:
            with open(var.target_file_PATH.resolve(), "rb") as file:
                part = MIMEApplication(file.read(), Name=var.xlsx_filename)
                part['Content-Disposition'] = f'attachment; filename="{var.xlsx_filename}"'
                message.attach(part)
        except FileNotFoundError:
            print(f"Error: File not found at {var.target_folder}")
            exit(1)
        
        # Send the email
        try:
            with smtplib.SMTP(var.smtp_server, var.smtp_port) as server:
                server.set_debuglevel(1)
                server.starttls()
                server.sendmail(var.sender_email, var.recipient, message.as_string())
                print("Email sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")


    else: print("Excel is not created")

Email()



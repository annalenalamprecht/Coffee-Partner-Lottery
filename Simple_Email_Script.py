# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:52:53 2023

@author: svenb
"""

import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "coffeepartneruu@gmail.com"
password = "egwnmceqwlrawygf"

e_mail = ["svenberndsen@hotmail.com", "coffeepartneruu@gmail.com"]
First_name = "Sven"
Last_name = "Berndsen"

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    # TODO: Send email her
    sender_email = "coffeepartneruu@gmail.com"
    receiver_email = e_mail
    message = f"""Subject: Your coffee group for this week

    
    Hi {First_name}
    This message is sent from Python."""
    
    server.sendmail(sender_email, receiver_email, message)
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()
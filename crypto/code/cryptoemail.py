import smtplib
 
gmail_user = ""
gmail_pwd = ""
to = ""
msg= "Check"
mailServer = smtplib.SMTP("smtp.gmail.com", 587)
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login(gmail_user, gmail_pwd)
mailServer.sendmail(gmail_user, to, msg)
mailServer.close()

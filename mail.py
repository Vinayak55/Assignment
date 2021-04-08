import smtplib

sender = 'rkvinayak5@gmail.com'
receiver = input(str("Enter the receiver email address"))
subject = input(str("Enter the subject of email"))
body  = input(str("Enter the details of message"))

try:
   Ob = smtplib.SMTP("smtp.gmail.com",587)
   Ob.starttls()
   Ob.login(sender,"password")
   message="subject:{}\n\n{}".format(subject,body)
   Ob.sendmail(sender, receiver, message)
   print ("Successfully sent email")
except Exception:
   print("unable to send email")
import pandas as pd
import smtplib

SenderAddress = "write down the send email addresas here"
password = "wirte down your email password here"

e = pd.read_excel("list.xlsx")
emails = e['Emails'].values
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SenderAddress, password)
msg = "Hello this is a deep sutariya"
subject = "certificate"
body = "Subject: {}\n\n{}".format(subject,msg)
for email in emails:
    server.sendmail(SenderAddress, email, body)
server.quit()
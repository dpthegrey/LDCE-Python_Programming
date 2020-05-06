import smtplib

server = smtplib.SMTP('smtp.gmail.com', 465)
server.starttls()
server.login('username', 'pasword')
message = 'Hello world! this is my first hello world email in Python'  # server.sendmail(Yours,Where you want to send,message) server.sendmail('ENTER_MAIL_FROM','ENTER_MAIL_TO',message) server.quit()
print('The Mail has been successfully sent. Check Your Mails.')

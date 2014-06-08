#!/usr/bin/env python
# encoding=UTF-8

"""Sample Hello World Python script."""

import sys
import getopt

import smtplib
from email.mime.text import MIMEText

# Command line help
HELP = """Usage: %s [-h] [-w who]
Say hello:
-h    Print this help page.
-w    Who to say hello to.""" % sys.argv[0]

def send_mail(recipient, sender, subject, text, smtp_host):
    ENCODING = 'UTF-8'
    if isinstance(recipient, str):
        recipient = [recipient]
    message = MIMEText(text.encode(ENCODING), _charset=ENCODING)
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = ','.join(recipient)
    server = smtplib.SMTP(smtp_host)
    server.sendmail(sender, recipient, message.as_string())
    server.quit()

def main():
    send_mail('michel.casabianca@gmail.com', 'test@test.com',
              'Test', 'This is a test', 'smtp.srvc.cvf')

# parse command line
if __name__ == '__main__':
    _who = "World"
    try:
        OPTS, ARGS = getopt.getopt(sys.argv[1:],
                                   "hw:",
                                   ["help", "who"])
    except getopt.GetoptError, error:
        print "ERROR: %s" % str(error)
        print HELP
        sys.exit(1)
    for OPT, ARG in OPTS:
        if OPT == "-h":
            print HELP
            sys.exit(0)
        elif OPT == "-w":
            _who = ARG
        else:
            print "Unhandled option: %s" % OPT
            print HELP
            sys.exit(1)
    main()


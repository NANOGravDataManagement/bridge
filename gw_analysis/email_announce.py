#!/usr/bin/python
#
# Read a list of plain text abstracts from ADS and extract email lists.
# Usage python announce_email.py <email.address> <session_ID>
#
import sys
import smtplib
import base64
import re
import time

toaddr=sys.argv[1]
sessionID = sys.argv[2]
From = 'Andrea.Lommen@fandm.edu'
Return = 'Andrea.Lommen@fandm.edu'
marker = "======================================"

##############################
# Define the message body.
body = """Content-Type: text/plain; charset=\"us-ascii\"



Dear Bridge User, 

Thank you for using the Bridge!

Please click on the links below to view the results of
your optimal statistic job submission to the Bridge.
http://thebridge.phys.wvu.edu/api/%s/optimal_stat/hd.png
http://thebridge.phys.wvu.edu/api/%s/optimal_stat/os_out.json

If you have questions about your analysis please reply to this email.

--%s
""" % (sessionID, sessionID, marker)

##############################

##############################
# Define the main headers.
header = """From: The Bridge c/o <andrea.lommen@fandm.edu>
To: %s 
Subject: The Results of Your Recent Bridge Analysis, sessionID %s
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary=\"%s\"
--%s
""" % (toaddr, sessionID, marker, marker)

message = header + body 

print message
try:
    smtpObj = smtplib.SMTP('smtp.phys.wvu.edu')
    smtpObj.sendmail(From, toaddr, message)
    print "Email en route to %s ..." % email
    smtpObj.quit()
except Exception:
    print "Error: unable to send email"

time.sleep(3)

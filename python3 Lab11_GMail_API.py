# Name: Joe Alcala
# Date: 11/18/2025
# Class: CIS188
# Program: Daily Ping Report via Email

import csv
import ezgmail
from ping3 import ping

# ======================================================
# Step 1 — Initialize Gmail API (uses credentials.json)
# ======================================================
# Make sure credentials.json is in the SAME folder as this script.
ezgmail.init("/Users/FreddyDirectory/Lab11/credentials.json")

# ======================================================
# Step 2 — Read IPs from ip.csv
# ======================================================
ip_list = []  # <-- Start with an empty list

with open('/Users/FreddyDirectory/Lab11/ip.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row:  # ignore blank lines
            ip_list.append(row[0])

# ======================================================
# Step 3 — Ping each IP and store results
# ======================================================
results = []

for ip in ip_list:
    response_time = ping(ip)  # returns seconds, None, or False
    results.append(f"{ip}  {response_time}")

# Create the message body for the email
email_body = "\n".join(results)

# ======================================================
# Step 4 — Send the email using ezgmail
# ======================================================
ezgmail.send(
    recipient='freddy85jackson@gmail.com',
    subject='Daily Ping Report',
    body=email_body
)

print("Daily Ping Report sent successfully!")

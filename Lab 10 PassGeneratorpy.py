# Name: Jose Alcala
# Date: 11/6/2025
# Class: CIS188

import csv
import random
import string
import subprocess
import os

PASS_LENGTH = 16
input_file = '/Users/Freddy Directory/88/employees.csv'
output_file = '/Users/Freddy Directory/88/employee_with_passwords.csv'

def gen_pass(length):
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice('!@#$%^&*()-_+=~[]{};<>?/\\|')
    rest = ''.join(random.choices(string.ascii_letters + string.digits + '!@#$%^&*()-_+=~[]{};<>?/\\|', k=length-4))
    pw = list(lower + upper + digit + special + rest)
    random.shuffle(pw)
    return ''.join(pw)

with open(input_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    employees = list(reader)

def get(emp, *names):
    for n in names:
        for k in emp:
            if k.strip().lower() == n.lower():
                return emp[k]
    return ''

with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['First Name','Last Name','Email','Password'])
    writer.writeheader()
    for emp in employees:
        writer.writerow({
            'First Name': get(emp,'first name','fname'),
            'Last Name': get(emp,'last name','lname'),
            'Email': get(emp,'email','e-mail'),
            'Password': gen_pass(PASS_LENGTH)
        })

print(f"Passwords generated and saved to {output_file}")
subprocess.run(['open','-R', os.path.abspath(output_file)])

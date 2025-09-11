# URL Opener Script

import subprocess

# Path to Chrome (check your install location)
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Open Chrome application
subprocess.Popen(chrome_path)

# Open D2L in Chrome
url = "https://d2l.pima.edu/d2l/home"
subprocess.Popen([chrome_path, url])

# Open Gmail in Chrome
url = "https://mail.google.com/mail/u/0/#inbox"
subprocess.Popen([chrome_path, url])

# Open ChatGPT in Chrome
url = "https://chat.openai.com/chat"
subprocess.Popen([chrome_path, url])

# Open github in Chrome
url = "https://github.com/"
subprocess.Popen([chrome_path, url])    
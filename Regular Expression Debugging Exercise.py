
# Name: Jose Alcala
# Date: 10/23/2025
# Class: CIS188
# Description: Regular Expression Debugging Exercise

import re

# Valid Email Address
print(re.match(r'^[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', 'Joe@Pima.com'))

# Valid U.S. ZIP Code
print(re.match(r'^\d{5}(-\d{4})?$', '12345-6789'))

# Valid Phone Number
print(re.match(r'^(\(\d{3}\)\s*|\d{3}[-\s]?)\d{3}[-\s]?\d{4}$', '(520) 206-6600'))

# Valid URL
print(re.match(r'^(https?://)?(www\.)?[A-Za-z0-9.-]+\.[A-Za-z]{2,}(/[\w./?%&=-]*)?$', 'https://www.pima.edu/'))
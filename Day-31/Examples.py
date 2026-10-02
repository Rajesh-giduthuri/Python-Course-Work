# ---------------------metacharacters 
# are special characters that have a meaning beyond their literal character.

# For Python, Regex is mainly handled through the built-in re module:
# import re
# r=raw string

# characters are :

# ^ ----- starting pattern
# $ ----- end of the pattern 
# . ----- any characters
# + ----- one or more
# * ----- zero or more
# ? ----- zero or more
# [] ---- sequences
# {n} --- n time
# {n,} -- atleast n times
# \d ---- digits
# \w ---- character(a-z,A-Z,0-9)
# \d ---- not a digits
# \s ---- space 
# \S ---- not a space 

# ----------email_validation

import re
user_email = input("Enter email: ")
pattern = r"\w+@\w+\.\w+"
if re.fullmatch(pattern, user_email):
    print("Valid")
else:
    print("Invalid")    

# ----------------------phone number

import re
ph_number=input("enter number:")
pattern=r"\d{10}"
if re.fullmatch(pattern,ph_number):
    print("valid")
else:
    print("invalid")

# -------------valid indian phone number

import re
ph_number = input("Enter number: ")
pattern = r"[6-9]\d{9}"
if re.fullmatch(pattern, ph_number):
    print(f"+91 {ph_number} valid")
else:
    print("Invalid")

# -------------credit card

import re 
num=input("enter card_no:")
pattern=r"\d{4}\s\d{4}\s\d{4}\s\d{4}"
if re.fullmatch(pattern, num):
    print(f"{num} valid")
else:
    print("Invalid")

# ----------empoloyee id

import re
id = input("Enter ID: ")
pattern = r"CGH\d{4}"
if re.fullmatch(pattern, id):
    print(f"{id} valid")
else:
    print("Invalid")
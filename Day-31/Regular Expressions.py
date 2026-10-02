# -------------Regular expressions----------------

# Regular Expressions (Regex) are patterns used to search, match, validate, extract, or replace text.
# In Python, regular expressions are provided by the built-in re module.

# ---------------match()------- 

# In Python, re.match() is used to check whether a regular expression pattern matches the beginning of a string.

# ------Syntax
# re.match(pattern, string)
# -----------------match code 

import re
text="Python Programming"
print(re.match("Python",text))
print(re.match("Programming",text))
import re
text = "Hello World"
result = re.match("Hello", text)
print(result)

# ----Output:
# <re.Match object; span=(0, 5), match='Hello'>
# Because "Hello" is at the beginning of the string, it matches.

# ------------------re.search()
# In Python's re module, search() and findall() are both used to find patterns, but they behave differently.
# re.search() searches for a pattern anywhere in the string and returns the first match.

import re
text = "I am learning Python and Python is easy."
result = re.search(r"Python", text)
print(result.group())

# ----------Output:
# Python
# It finds the first "Python" and stops.

# ---------------re.findall()
# re.findall() searches the entire string and returns all matches as a list.
import re
text = "I have 10 apples, 20 oranges and 30 bananas."
numbers = re.findall(r"\d+", text)
print(numbers)

# ---------Output:
# ['10', '20', '30']

# Unlike search(), it doesn't stop after the first match.
# search() vs findall()
# Function	Searches	Returns
# re.match()	Beginning only	First match
# re.search()	Anywhere	First match
# re.findall()	Entire string	All matches

import re
s="Python code c code java code"
print(re.findall("code",s))

# --------------------re.sub()
# In Python Regex, re.sub() is used to replace matching text, 
# while re.fullmatch() checks whether the entire string matches a pattern.

# ---------re.sub() — Substitute / Replace
# re.sub() finds text matching a pattern and replaces it.

# -----Syntax
# re.sub(pattern, replacement, string)
import re
text = "I like Java and Java is easy."
result = re.sub("Java", "Python", text)
print(result)

# ---------Output:
# I like Python and Python is easy.

import re
text = "I like Java and Java is easy."
result = re.sub("Java", "Python", text)
print(result)

# Remove numbers
# You can replace matches with an empty string:
# import retext = "My age is 21"result = re.sub(r"\d+", "", text)print(result)
# Output:
# My age is 

# Here:
# - \d+ → finds one or more digits
# - "" → replaces them with nothing

# -----------re.fullmatch() — Match the entire string
# re.fullmatch() checks whether the whole string matches the given pattern.

# -------------------Example: Phone number
import re
phone = "9876543210"
result = re.fullmatch(r"\d{10}", phone)
if result:  
  print("Valid")
else: 
   print("Invalid")

# ----------------Output:
# Valid
# Because the entire string contains exactly 10 digits.

# -------------------Invalid example
import re
phone = "9876543210abc"
result = re.fullmatch(r"\d{10}", phone)
print(result)

# ----------Output:
# None
# Although the first 10 characters are digits, the entire string is not 10 digits.

import re
phone = "9876543210"
result = re.fullmatch(r"\d{10}", phone)
if result:  
  print("Valid")
else: 
   print("Invalid")

# ------------match() vs fullmatch()
# This is very important:

import re
text = "Python123"
print(re.match(r"Python", text))
print(re.fullmatch(r"Python", text))

# ----match():
# Match

# ----because "Python" is at the beginning.
# ------fullmatch():
# None
# because "Python123" is not exactly "Python".

# -----------Simple way to remember
# Function	           What it checks

# re.match()	          Beginning of string
# re.search()	          Anywhere in string
# re.findall()	          All occurrences
# re.finditer()	          All occurrences + Match objects
# re.sub()	              Replace matches
# re.fullmatch()	      Entire string
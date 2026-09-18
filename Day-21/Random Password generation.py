# # random password generation code

# import random as r
# characters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# characters+="abcdefghijklmnopqrstuvwxyz"
# characters+="0123456789"
# characters+="@#$&*!"
# length=int(input("Enter password length: "))
# password=""
# for i in range(length):
#     password+=r.choice(characters)
# print("Generated Password:", password)

# this code generated as user define with every type of character in password with minimum length of 4

import random as r
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER = "abcdefghijklmnopqrstuvwxyz"
DIGITS = "0123456789"
SPECIAL = "@#$&*!"
password=[]
length=int(input("Enter password length: "))
if length<4:
    print(f"Password length is {length} should be at least 4")
else:
    password.append(r.choice(UPPER))
    password.append(r.choice(LOWER))
    password.append(r.choice(DIGITS))
    password.append(r.choice(SPECIAL))
    for i in range(length-4):
        all=UPPER+LOWER+DIGITS+SPECIAL
        password.append(r.choice(all))
    r.shuffle(password)
    print("Generated Password:", "".join(password))


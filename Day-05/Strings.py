#strings
#immutable data type
#it follows indexing
#ordered collection of data

s1="Name:"
print(s1)

s2=input()
print(s2)

#concatenation
print(s1+s2)
s1=s1+s2
print(s1)

#Repetition
print(s2*3)

#replace function
s="I code Python"
print(s.replace("Python","Java")) #Strings are immutable but in this line replace refers to diff object
print(s)

#String methods
s3="apple"
s4="hi, hello there"
s5="hI, HElLo THErE"
print(s3.upper())
print(s3.lower())
print(s3.capitalize())
print(s4.title())
print(s5.swapcase())

#Check Methods
# isupper()
# islower()
# isalpha()
# isdigit()
# isalnum()
# isspace()

#strip function
# strip()
# lstrip()
# rstrip()

#split function
#split()

#join method (list --> string)
#" ".join(l)

#len()

#comparision 
print("abc"<"xyz") #ASCII values of according char

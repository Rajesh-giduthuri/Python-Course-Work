ch=65
print(chr(ch))
print(chr(ch+10))

print(ord("a")) #ASCII value
print(ord("A")) #ASCII value

#char pattern
ch=65
for i in range(5):
    for j in range(5):
        print(chr(ch),end=" ")
        ch+=1
    print()
#output :
# A B C D E 
# F G H I J 
# K L M N O 
# P Q R S T 
# U V W X Y 

#char in row
ch=65
for i in range(4): 
    for j in range(4):
        print(chr(ch),end=" ")
    ch+=1
    print()
#output :
# A A A A 
# B B B B 
# C C C C 
# D D D D 

#char in col
ch=65
for i in range(4):
    for j in range(4):
        print(chr(ch),end=" ")
        ch+=1
    ch=65
    print()
#Output :
# A B C D 
# A B C D 
# A B C D 
# A B C D 

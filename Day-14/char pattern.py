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

#char in row
ch=65
for i in range(4): 
    for j in range(4):
        print(chr(ch),end=" ")
    ch+=1
    print()

#char in col
ch=65
for i in range(4):
    for j in range(4):
        print(chr(ch),end=" ")
        ch+=1
    ch=65
    print()
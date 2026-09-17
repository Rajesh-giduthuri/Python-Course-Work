# #0 , 1 pattern
for i in range(4):
    for j in range(4):
        if (i+j)%2==0:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()

#pattern for even,odd
even=2
odd=1
for i in range(4):
    for j in range(4):
        if i%2==0:
            print(even,end=" ")
            even+=2 
        else:
            print(odd,end=" ")
            odd+=2
    print()

#print pattern for row numbers
for i in range(4):
    for j in range(4):
        print(i,end=" ")
    print()

#print pattern for column numbers
for i in range(4):
    for j in range(4):
        print(j,end=" ")
    print()

#Name pattern
name="Sreek"
for i in range(len(name)):
    print(name[:(i+1)])

#Name pattern
name="Sreek"
for i in range(len(name)+1):
    print(name[i-1]*i)
# #0 , 1 pattern
for i in range(4):
    for j in range(4):
        if (i+j)%2==0:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()
#Output :
# 1 0 1 0
# 0 1 0 1
# 1 0 1 0
# 0 1 0 1

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
#Output :
# 2 4 6 8 
# 1 2 3 4 
# 10 12 14 16 
# 5 6 7 8 

#print pattern for row numbers
for i in range(4):
    for j in range(4):
        print(i,end=" ")
    print()
#Output :
# 0 0 0 0 
# 1 1 1 1 
# 2 2 2 2 
# 3 3 3 3 

#print pattern for column numbers
for i in range(4):
    for j in range(4):
        print(j,end=" ")
    print()
#output :
# 0 1 2 3 
# 0 1 2 3 
# 0 1 2 3 
# 0 1 2 3

#Name right angle pattern
name="Sreek"
for i in range(len(name)):
    print(name[:(i+1)])
#Output :
# S
# Sr
# Sre
# Sree
# Sreek

#Name pattern
name="Sreek"
for i in range(len(name)+1):
    print(name[i-1]*i)
#Output :
# S
# rr
# eee
# eeee
# kkkkk 


#increase number in right angle pattern
n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()
    n+=1
#Output :
# 1
# 2 2
# 3 3 3
# 4 4 4 4

#increase number in right angle pattern
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    n+=1
#Output :
# 1
# 1 2
# 1 2 3
# 1 2 3 4

#increase number continuesly
n=int(input())
num=1
for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()
#Output : 
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 

#Decrease number in inverted right angle triangle
n=int(input())
for i in range(n):
    for j in range(n-i):
        print(j+1,end=" ")
    print()
#Output :
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1

#Decrease number continuesly
n=int(input())
for i in range(n, 0, -1):
    for j in range(i):
        print(i,end=" ")
    print()
#Output :
# 4 4 4 4 
# 3 3 3 
# 2 2 
# 1 

#number square pattern
n=int(input())
for i in range(n):
    for j in range(n):
        print(j+1,end=" ")
    print()
#Output :
# 1 2 3 4 
# 1 2 3 4 
# 1 2 3 4 
# 1 2 3 4

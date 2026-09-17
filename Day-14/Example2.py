#increase number in right angle pattern
n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()
    n+=1

#increase number in right angle pattern
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    n+=1

#increase number continuesly
n=int(input())
num=1
for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()

#Decrease number in inverted right angle triangle
n=int(input())
for i in range(n):
    for j in range(n-i):
        print(j+1,end=" ")
    print()

#Decrease number continuesly
n=int(input())
for i in range(n, 0, -1):
    for j in range(i):
        print(i,end=" ")
    print()

#number square pattern
n=int(input())
for i in range(n):
    for j in range(n):
        print(j+1,end=" ")
    print()
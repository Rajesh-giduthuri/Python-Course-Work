#right angle triangle pattern
n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()
#single loop right angle triangle pattern
n=int(input())
for i in range(1,n+1):
    print("* "*i)


#inverted right angle triangle pattern
n=int(input())
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()
#single loop inverted right angle triangle pattern
n=int(input())
for i in range(n,0,-1):
    print("* "*i) 

    
#opposite inverted right angle triangle pattern
n=int(input())
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    print()
#single loop opposite inverted right angle triangle pattern
n=int(input())
for i in range(n,0,-1):
    print("  "*(n-i)+"* "*i) #two spaces


#right aligned normal triangle pattern
n=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
#single loop right aligned normal triangle pattern
n=int(input())
for i in range(1,n+1):
    print("  "*(n-i)+"* "*i) #two spaces

#pyramid pattern
n=int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()

#Single loop Pyramid pattern
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))

# #Inverted Pyramid pattern
n=int(input())
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for j in range(2*(n-i)-1):
        print("*",end="")
    print()

#Inverted Pyramid pattern
n=int(input())
for i in range(n,0,-1):
    print(" "*(n-i)+"*"*(2*i-1))

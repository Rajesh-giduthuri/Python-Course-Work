#nested loops

#Matrix print
m=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(m)):
    for j in range(len(m[0])):
        print(m[i][j],end=" ")
    print()

#Square pattern
n=int(input())
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()

#numbers in square pattern 
n=1
for i in range(3):
    for j in range(3):
        print(n,end=" ")
        n+=1
    print()

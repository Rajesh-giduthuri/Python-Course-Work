#Diagonal pattern
n=int(input()) #should be odd num
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#Diagonal difference
m=[[10,20,30,40],[50,60,70,80],[90,100,200,300],[400,500,600,700]]
d1=0
d2=0
for i in range(len(m)):
    for j in range(len(m[0])):
        if i==j:
            d1+=m[i][j]
        elif (i+j)==(len(m)-1):
            d2+=m[i][j]
    print()
print(d1,d2)
print(abs(d1-d2))

#Plus pattern
n=int(input()) # should be odd num
for i in range(n):
    for j in range(n):
        if i==(n//2) or j==(n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


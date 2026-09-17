# #find the factors of n

n=int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")

#perfect number ((sum-number) of factors of a number==number)
n=int(input())
s=0
for i in range(1,n+1):
    if n%i==0:
        s+=i
if (s-n)==n:
    print("Perfect")
else:
    print("Not perfect")

#perfect number in range
a=int(input())
b=int(input())
for i in range(a,b+1):
    s=0
    for j in range(1,i):
        if i%j==0:
            s+=j
    if s==i:
        print(i,end=" ")
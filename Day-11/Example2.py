#sum of digits in number

n=int(input())
s=0
while n>0:
    d=n%10
    s+=d
    n=n//10
print(s)
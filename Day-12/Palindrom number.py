#check is it a palindrom number or not

n=int(input())
temp=n
rev=0
while n>0:
    d=n%10
    rev=(rev*10)+d
    n=n//10
if temp==rev:
    print("Palindrom")
else:
    print("Not Palindrom") 
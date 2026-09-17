#count the number of digits

n=int(input())
cou=0
while n>0:
    n=n//10
    cou+=1
print(cou)


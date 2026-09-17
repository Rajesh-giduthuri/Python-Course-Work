#prime or not

def prime(n):
    cou=0
    for i in range(1,n+1):
        if n%i==0:
            cou+=1
    if cou==2:
        return "Prime"
    else:
        return "Not Prime"
print(prime(int(input())))

#prime numbers in a range
def pri(x,y):
  l=[]
  for i in range(x,y+1):
    if prime_check(i):
      l.append(i)
  return l
def prime_check(n):
    cou=0
    for i in range(1,n+1):
        if n%i==0:
            cou+=1
    if cou==2:
      return True
    else:
      return False
    
x=int(input())
y=int(input())
print(pri(x,y))
print(f"Total Prime numbers in b/w {x} - {y} : {len(pri(x,y))}")

#output :
#2
#100
#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
#Total Prime numbers in b/w 2 - 100 : 25
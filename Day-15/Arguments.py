# Based on the arguments , how we are passing to the function, functions can be categorized into 5 types

#Types

#--> Positional arg
def f1(x,y): #positions will change if arg pos changes
    print(x,y)
    return x/y
print(f1(2,5))
print(f1(5,2))

#--> Keyword arg
def f2(a,b): #position will not change as specified with keys
    print(a,b)
    return a/b
c=5
d=6
print(f2(a=c,b=d))
print(f2(b=d,a=c))

#--> Defualt arg
def f3(a,b,c=0,d=0): #defualt parameters should be at last
    print(a,b,c,d)
    return a+b+c+d
print(f3(2,5))
print(f3(2,5,3))
print(f3(2,5,3,4))

#--> Variable lenght arg
def f4(*var): #unknown number of parameters
    print(type(var)) #tuple
    tot=0
    for i in var:
        tot+=i
    return tot
print(f4(1,2,3,4,5,6))

#--> Variable length Keyword arg
def f5(**var): #unknown number of parameters with keys
    print(type(var)) #Dictionary
    tot=0
    for i in var.values():
        tot+=1
    return tot
print(f5(a=1,b=2,c=3,d=4))

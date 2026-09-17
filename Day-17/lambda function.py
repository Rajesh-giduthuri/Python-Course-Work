#lambda function : An anonymous function that doesn't have a name
# lambda is used for simple funtions

def square(n):
    return n*n
square(10)

#square of num
square=lambda x:x*x
print(square(5))

#greater ele
great=lambda a,b: a if a>b else b
print(great(23,34))


#Higher order functions (function is passed inside a function as parameter)

#filter()
l=[1,2,3,4,5,6]
res=filter(lambda x:x%2==0,l)
print(list(res))

#map()
l=[1,2,3,4,5,6]
res=map(lambda x:x>10,l)
print(list(res))

#reduce()
from functools import reduce
l=[1,2,3,4,5,6]
res=reduce(lambda a,b:a+b,l)
print(res)

#sorted()
stu=[('siri',34),
     ("ravi",35),
     ("sree",65)]
res=sorted(stu,key=lambda x:x[1])
print(res)

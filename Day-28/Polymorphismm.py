#polymorphism (many + forms) (method overloading , overriding)
# Ability of a single interface(method,function,operator) to perform in a diff way based on the data type or class

#method overriding : overrides the new method with previous one to handle we use default,var length or ver len key arg
class A:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c): #overrides the prev add()
        return a+b+c
a=A()
#print(a.add(10,20)) #A.add() missing 1 required positional argument: 'c'
print(a.add(10,20,30))

#to overcome the method overriding useing default arg
class cal:
    def add(self,a,b,c=0,d=0): #only four arg
        return a+b+c+d
a=cal()
print(a.add(10,20,30))

#to overcome the method overloading useing var-len arg
class cal:
    def add(self,*a): #multiple arg stroed as tuple datatype
        return sum(a)
a=cal()
print(a.add(1,2,3,4,5,6,7,8,9))
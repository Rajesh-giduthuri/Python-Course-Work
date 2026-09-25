#overriding
class employee:
    def work(self):
        print("Working")
        #return "Working"
class developer(employee):
    def work(self):
        super().work() #to handle overriding
        print("Develop") #overrides the par class work
        #return "Develop"
d=developer()
d.work()
employee.work(d) #calling directly by class name and method also some referance

# res=[employee(),developer()] #for available overriding methods
# for i in res:
#     print(i.work())

#overloading (operator)
#operator a+b is used internally as a.__add__(b)
# - __sub__
# * __mul__
# / __truediv__
# // __floordiv__
# % __mod__
# == __eq__
print(10+20)
print("python"+"code")
print([1,2,3]+[4,5,6]) 

class cal:
    def __init__(self,a):
        self.val=a
    def __add__(self,b):
        return self.val+b.val
a=cal(10)
b=cal(20)
print(a+b)
c=cal(100)
res=(a+b)+c.val
print(res)
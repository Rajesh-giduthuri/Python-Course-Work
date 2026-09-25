#Abstraction : hiding the unneccessary implementation by showing only necessary details

from abc import ABC, abstractmethod
class shapes(ABC): #only common features are abstracted 
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class square(shapes):  #Heirarchical inheritance
    def __init__(self,side):
        self.side=side
    def square_details(self):
        print(f"Square side is: ",self.side)
    def area(self):
        area=self.side*self.side
        return area
    def perimeter(self):
        peri=4*self.side
        return peri
class rectangle(shapes):  #Heirarchical inheritance
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        area=self.l*self.b
        return area
    def perimeter(self):
        peri=2*(self.l+self.b)
        return peri
class circle: 
    def __init__(self,r):
        self.r=r
    def area(self):
        area=(3.14*(self.r*self.r))
        return area
    def circumference(self):
        circum=((2*3.14)*self.r)
        return circum

sq=square(2)
rec=rectangle(2,3)
cir=circle(2)

print(f"Area of Square is: ",sq.area())
print(f"Perimeter of Square is: ",sq.perimeter())
sq.square_details()
print()
print(f"Area of Rectangle is: ",rec.area())
print(f"Perimeter of Rectangle is: ",rec.perimeter())
print()
print(f"Area of Circle is: ",cir.area())
print(f"Circumference of Circle is: ",cir.circumference())
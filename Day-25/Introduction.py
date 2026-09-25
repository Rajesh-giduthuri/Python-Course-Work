# #OOPs : Object Oriented Programming
# -->Reuse
# -->Maintain
# -->Extend

# #Concepts in OOPs
# -->Class
# -->Object
# -->Abstraction
# -->Encapsulation
# -->Inheritence
# -->Polymorphism

# #Class : It is a blueprint of an instance

# Class class_name:
#         ------------ methods 
#         ------------- attributes
# to take object_name=class_name

# #simple Class & Object     
class course:
    def exam(self):
        print("exams")
    def attend(self):
        print("attended")
    def assignments(self):
        print("assignments")
stu=course()
stu.exam()
stu.attend()

#Constructor
class course:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def stu_details(self,dept):
        self.dep=dept
        print(f"name: {self.name} roll: {self.roll} marks: {self.marks}")
    def exam(self):
        print("exams")
    def attend(self):
        print(self.dep)
        print("attended")
stu1=course("kaka",324,67) #object 1
stu2=course("sas",438,56) #object 2
stu1.exam()
stu1.attend()
stu1.stu_details("python")

stu2.exam()
stu2.attend()
stu2.stu_details("java")

#classmethod
class course:
    def __init__(self,name):
        self.name=name
    @classmethod
    def method1(self):
        #print(self.name)
        print(f"name is {self.name}")
s=input()
stu=course(s)
#stu.method1()
course.method1()
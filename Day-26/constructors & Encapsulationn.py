#Encapsualtion : wrapping the data(attributes & methods) into a single unit 
# to provide data security by public , protect , private

# pubilc--> self.attribute_name (everywhere in the code)
# protect--> self._attribute_name (everywhere in the code but won't prefer outside)
# private--> self.__attribute_name (only inside the class)

#constructor (default , parameterized) : a special type of method used to initialize newly created objects

class company:
    def __init__(self,name,id,salary):
        self.name=name #public attribute
        self._id=id    #protect attribute
        self.__salary=salary  #private attribute
    def salary(self):
        return self.__salary
    def datails(self):
        print(f"Employee name is: {self.name}, emp_id: {self.id}")

emp=company("kaka",43,5756)
print(emp.name)
print(emp._id)
#print(emp.__salary) #private attribute
print(emp.salary()) #calling the method for private data

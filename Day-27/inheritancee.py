#inheritance : Aquireing the properties from parent class to child class

#single inheritance
class company:
    def __init__(self,com_name,loc,xy):
        self.com_name=com_name
        self._loc=loc
        self.__xy=xy #accessed only inside the class not even subclass
    def agenda(self):
        print("Abstract of company")
    def clients(self):
        print("Clients")
    def CEO(self):
        print("I am the CEO")
        print(self.__xy) #accessed only inside the class not even subclass
class cloud_company(company): #single inheritance
    def cloud(self):
        print("Company data in the cloud")
    def details(self):
        print(f"Company name is: {self.com_name} and location is at {self._loc}")
        
c=cloud_company("Google","Hyd",23)
c.agenda()
c.cloud()
c.clients()
c.details()
c.CEO()
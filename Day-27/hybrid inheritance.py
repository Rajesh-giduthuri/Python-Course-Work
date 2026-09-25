#Hybrid inheritance 

class company:
    def Rules(self):
        print("Rule is Rule")
class HR_team(company):  #Heirarchical inheritance
    def hiring(self):
        print("Hiring")
class front_end(company):  #Heirarchical inheritance
    def front_end(self):
        print("Desinging")
class back_end(company):  #Heirarchical inheritance
    def back_end(self):
        print("Python")
class clients(HR_team,front_end,back_end):  #Multiple inheritance
    def meetings(self):
        print("client meetings")

c1=clients()
c1.meetings()
c1.front_end()
c1.back_end()
c1.Rules()
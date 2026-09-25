#Heirarchical inheritance

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

c1=HR_team()
c2=front_end()
c3=back_end()

c1.hiring()
c1.Rules()
print()
c2.front_end()
c2.Rules()
print()
c3.back_end()
c3.Rules()
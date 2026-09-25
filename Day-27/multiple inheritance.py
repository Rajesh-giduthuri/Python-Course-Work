#multiple inheritance

class Employee:
    def work(self):
        print("Working")
class Developer:
    def develop(self):
        print("developing")
class tester(Employee,Developer): #multiple inheritance
    def test(self):
        print("testing")

obj=tester()
obj.work()
obj.develop()
obj.test()
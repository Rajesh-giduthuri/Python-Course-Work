#multi-level inheritance

class Employee:
    def work(self):
        print("Working")
class Developer(Employee): #multi level inheritance
    def develop(self):
        print("developing")
class tester(Developer): #multi level inheritance
    def test(self):
        print("testing")

obj=tester()
obj.work()
obj.develop()
obj.test()
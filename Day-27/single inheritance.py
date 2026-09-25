#single inheritance

class Employee:
    def work(self):
        print("Working")
class Developer(Employee):
    def code(self):
        print("coding")

obj=Developer()
obj.work()
obj.code()

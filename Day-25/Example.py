#Employee Data

class employee():
    def __init__(s,name,id,b_sal):
        s.name=name
        s.id=id
        s.b_sal=b_sal
    def emp_details(s,exp):
        s.exp=exp
        if exp>=2:
            sa=s.b_sal+(0.2*s.b_sal)
            print(f"Name: {s.name} ID: {s.id} Salary: {int(sa)}")
        elif exp>=1:
            sa=s.b_sal+(0.1*s.b_sal)
            print(f"Name: {s.name} ID: {s.id} Salary: {int(sa)}")
        else:
            print(f"Name: {s.name} ID: {s.id} Salary: {s.b_sal}")

empl=employee("Sree",21,100)
print("Enter the experience 0 or 1 or 2: ")
ex=int(input())
empl.emp_details(ex)

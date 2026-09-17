#Scope : Region to access the variable
#(LEGB)
#--> Local scope
#--> Enclosing scope
#--> Global scope
#--> Builtin scope

#local scope
def f1():
    x=10
    print(x)
f1()
print(x)
#output : 10  error

#enclosing scope
def f2():
    x=10
    def f():
        y=20
        print(x+y)
    f()
f2()
#output : 30

#global scope
x=10
def f3():
    print(x)
f3()
print(x)
#output : 10 10

#builtin scope
def f4():
    l=[1,2,3]
    print(sum(l))
f4()
#output : 6

#Modify Global var
x=20
def f5():
    global x
    x=x+10
    print(x)
f5()
print(x)
#output : 30 30

#Modify Enclosing var
def f6():
    x=100
    def f():
        nonlocal x
        x=x+100
        print(x)
    f()
f6()
#output : 200


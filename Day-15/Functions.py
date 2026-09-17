#Function : it is a block of code to perform a specific task

def addition(a,b): #function defination (parameters)
    return a+b #block
addition(10,20) #function call (arguments)

# Why function :
# ->Reusability
# ->complexity will be reduced
# ->maintain the modularity

#Types of functions
# ->Builtin functions (len(),min(),max(),sum(),....)
# ->user defined functions

# -->with return & with parameters
def add1(a,b):
    return a+b
print(add1(10,20))

# -->with return & without parameters
def add2():
    a=10
    b=20
    return a*b
print(add2())

# -->without return & with parameters
def add3(a,b):
    print(a+b)
add3(10,20)

# -->without return & without parameters
def add4():
    a=10
    b=20
    print(a+b)
add4()

## Type conversions in Python

# Implicit type conversion
a=5
b=10.5
c=a+b  # b is implicitly converted to float
print(type(c))  # float

# Explicit type conversion
d=str(a)  # a is explicitly converted to string
print(type(d))  # str

e=int(b)  # b is explicitly converted to integer
print(type(e))  # int

f=float(a)  # a is explicitly converted to float
print(type(f))  # float
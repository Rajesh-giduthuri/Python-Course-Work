#pass by value
#pass by reference
#--->pass by object reference

#When performing modification the reference remains same
#when performing reassignment the reference are diff

def f1(x):
    x=20
    print(id(x))
    print(x)
a=10
print(id(a))
f1(a)
#output :  #diff references because, int 10,20 are immutable datatype
# 140710617785544   
# 140710617785864   
# 20

def f2(x):
    x.append(5)
    print(id(x))
    print(x)
a=[1,2,3,4]
print(id(a))
f2(a)
#output : same reference because, list is mutable datatype that changes the pack of ele
# 2509047619712
# 2509047619712
# [1, 2, 3, 4, 5]

def f3(x):
    x=[10,20,30]
    print(id(x))
    print(x)
a=[1,2,3]
print(id(a))
f3(a)
#output : diff reference because, list is changed to the variable and the reference is diff
# 2035955687552
# 2035955835520
# [10, 20, 30]
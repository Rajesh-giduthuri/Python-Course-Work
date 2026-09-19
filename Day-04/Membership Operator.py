#membership operators
# in , not in

l=[1,2,3,4,5]
print(3 in l)    
print(6 in l)    
print(3 not in l) 
print(6 not in l) 

name="python"
print('p' in name)
print('z' in name)
print('p' not in name)
print('z' not in name)

dic={"name":"python","version":3.11}
print("name" in dic)
print(1 in dic)
print(3.11 in dic.values())
#tuple
#immutable #ordered #indexing and slicing 

#methods
t=(1,2,3,4,1)
print(t[4])
print(t.count(1))
print(t.index(3))
t.sort()
print(t)

print(*t) #unpacking

# t1=(11,22,33,[1,2,3])
# print(len(t1))
# print(t1)
# t1[3][2]=100
# print(t1)
# print(len(t1))

# l=list(t)
# print(t)
# print(l)
# l[0]=10
# print(l)
# t2=tuple(l)
# print(t2)
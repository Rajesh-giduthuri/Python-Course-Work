#sets
#unordered #mutable #unique ele

s=set() #empty set

s1={1,2,3,4}
print(s1) #ordered changes

#set operations
#union
s2={3,4,5,6}
print(s1|s2) #union
print(s1.union(s2))

#intersection
print(s1&s2)
print(s1.intersection(s2))

#difference
print(s1-s2)
print(s1.difference(s2))
print(s2.difference(s1))

#symmetric diff
print(s1^s2)
print(s1.symmetric_difference(s2))

#issubset
s3={12,34,55}
s4={55}
print(s4.issubset(s3))

#issuperset
print(s3.issuperset(s4))

#frozenset(immutable , ordered)
s5={10,20,40} #frozen that will not effected by any operations as normal set 

#set methods
s3.add(10) #added at any pos because set is unordered
print(s3)

s3.update([10,50,60])
print(s3)

s3.remove(50)
# s3.remove(100) # Error because ele not in set
s3.discard(100) #None if ele not in set
print(s3)

s3.pop() #pop any ele because set is unordered
#In some platforms like Hackerrank when performing pop on set it removes min ele
print(s3)

s4.clear() #del ele but not the reference
del(s4) #del along with the reference from memory
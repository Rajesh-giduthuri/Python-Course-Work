#lists
#mutable #ordered #supports indexing and slicing

#list operations
li=[1,2,3,4]
print(li[::-1]) #reverse()
print(*li) #unpacking

#l=list(map(int,input().split()))

#concatenation
l1=[1,2,3]
l2=[4,5,6]
print(l1+l2)
print(l1,l2)
 
#repetition
print(l1*3)

#copy
x=l1.copy()
print(x)

#membership operator (in , not in)
print(10 in l1)
print(100 not in l2)
print(1 in l1)

#list methods
l1.append(10) #single ele at last
l1.append([20,30])
print(l1)

l1.extend([20,40,60]) #multiple ele at last
print(l1)

l1.insert(2,100) # insert at position
print(l1)

l1.pop() #del last ele
l1.pop(3) #del at position
print(l1)

l1.remove(1) #del ele
print(l1)

#sorting
l3=[2,4,7,9,-5,0]
l3.sort() #sorts original list
print(l3)
print(sorted(l3)) #sorts in duplicate object
l3.sort(reverse=True)
print(l3)

print(l3.count(0))
print(l3.index(0))
print(len(l3))
print(min(l3))
print(max(l3))
print(sum(l3))
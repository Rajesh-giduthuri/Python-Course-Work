#dictionarires(key , values)
#ordered based on keys #unique keys #mapping datatype

std={"name":"siri",
     "rol":"101",
     "marks":"8.5"}
print(std)

std["name"]="sree"
print(std) #duplicates are not supported and key is reasigned with new value

s="sreekanth"
d={'s':1,'r':1,'e':2,'k':1}
print(d['e'])
print(d.get('e')) 

#methods
print(d.keys())
print(d.values())
print(d.items())

d.update({'e':3})
print(d)

d.pop('r')
print(d)
d.popitem() #del last item
print(d)

x=10
print(hash(x)) #unique number for only immutable data type

#most repeated key
s = "Python code code"
l = s.split()

d = {}
for w in l:
    d[w]=d.get(w,0)+1

k=max(d,key=d.get)
print(k)
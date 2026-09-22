#collections module

# import collections
# from collections import Counter
# name="Sreekanth"
# r=Counter(name)
# print(r)

# l=[1,2,4,4,5,2,2]
# print(Counter(l))

#default dictionary : used for dictionaries when searchin for key which is not in dict 
# not raises an error like normal frequency check in dict
# from collections import defaultdict
# d=defaultdict(int)
# d["Apple"]=1
# print(d["name"]) #return 0 instead of error

#Queue
from collections import deque
d=deque([1,2,3,6,8])
d.append(4)
d.appendleft(10)
d.pop()
d.popleft()
print(d)

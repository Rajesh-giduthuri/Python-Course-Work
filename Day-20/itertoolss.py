#itertools module

#permutations
from itertools import permutations
num=[1,2,3,4]
print(list(permutations(num)))

#combinations
from itertools import combinations
num=[1,2,3,4]
print(list(combinations(num,3)))

#product
from itertools import product
a=[1,2,3]
b=["A","B","C"]
print(list(product(a,b)))


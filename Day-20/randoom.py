# random topic

import random
random.randint(1,6)
n=[10,20,30,40,50]
print(random.choice(n))
print(random.choices(n,k=3))
print(random.sample(n,k=3))
print(random.shuffle(n))
print(random.randrange(1,10))

# sample 
# is used to get unique values from the list
# choices
# whereas choices can return duplicate values.
# shuffle is used to shuffle the list in place and returns None.
# randrange is used to get a random number from the given range.
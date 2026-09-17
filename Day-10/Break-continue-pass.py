#Break to stop the iteration
#Continue to skip the current iteration
#Pass to terminate the iteration

for i in range(10):
    if i==5:
        break
    print(i)

for i in range(10):
    if i==5:
        continue
    print(i)

for i in range(10):
    if i%2==0:
        pass
    else:
        print(i)
#while loop

i=1
while i<=10:
    print(i,end=" ")
    i+=1
# #output : 1 2 3 4 5 6 7 8 9 10

i=5
while i>0:
    print(i,end=" ")
    i-=1
# #output : 5 4 3 2 1

i=1
while i<=10:
    if i==5:
        break
    print(i,end=" ")
    i+=1
else:
    print("Loop completed") #when condition false
# #output : 1 2 3 4 

i=0
while i<10:
    i+=1
    if i==5:
        continue
    print(i,end=" ")
else:
    print("Loop completed")
#output : 1 2 3 4 6 7 8 9 10 
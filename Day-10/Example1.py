#find the target
l=[1,2,3,4,5,6,6,7,98,6,5,4]
k=int(input())
for i in range(len(l)):
    if l[i]==k:
        print(i)
else:
    print("Loop completed")
#positive or negative and even or odd
n=int(input())
if n>0:
    if n%2==0:
        print(f"{n} is positive and even")
    else:
        print(f"{n} is positive and odd")
elif n<0:
    if n%2==0:
        print(f"{n} is negative and even")
    else:
        print(f"{n} is negative and odd")
else:
    print("input is zero")
#Recursion : A function calling itself again and again
# should have a base condition to stop the loop

#factorial
def fact(n):
    if n==0 or n==1: #base condition
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

#fibonacci
def fibonacci(n):
    if n==0: #base condition
        return 0
    if n==1: #base condition
        return 1

    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(6))

#countdown
def countdown(n):
    if n<=0: #base condition
        print("Blastoff!")
        return
    print(n)
    countdown(n-1)
countdown(3)

#sum of natural numbers
def sum_of_natural(n):
    if n==1: #base condition
        return 1
    return n+sum_of_natural(n-1)
print(sum_of_natural(10))

#sum of even natural
def sum_of_even(n):
    if n%2==0:
        if n==2: #base condition
            return 2
        return n+sum_of_even(n-2)
    else:
        return sum_of_even(n+1)
print(sum_of_even(10))
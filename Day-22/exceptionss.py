# exception: is an event that can handled by python only on 

# RuntimeError:
# 1-ZeroDivisionError
# 2-ValueError
# 3-KeyError
# 4-IndexError
# 5-FileNotFoundError
# 6-AttributeError

# a=10
# b=0
# # print(a/b)----ZeroDivisionError
#

# # a=10
# # b='d'
# # print(a/b)----TypeError

# dict={'c':4} 
# print(d['g'])------KeyError

# l=[1,2,3,4,5]
# print(l[10])
# print(l)-------IndexError:list index out of range


# # -----------------------EXCEPTION HANDLING--------------
# Exception handling:--keywords( try,except,else,finally )

# --try: block of code where we have the error in our code
# --except:
#        print(-------)
# --else:
# ----------
# --finally:
#        print('done')


# --------code-----------

a=int(input("enter a:"))
b=int(input("enter b:"))
try:
    print(a/b)
except:
    print("something went wrong")
else:
    print("there is not error")
finally:
    print("execution done")        
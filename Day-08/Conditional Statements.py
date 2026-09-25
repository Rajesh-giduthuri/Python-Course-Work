#Control Statements
#conditional statements

#simple if
n=int(input())
if n>0:
    print("positive")

#if else
age=int(input())
if age>18:
    print("Eligible") 
else:
    print("Not Eligible")

#if elif else
n=int(input())
if n>0:
    print("+ve")
elif n<0:
    print("-ve")
else:
    print("Zero")

#Nested if
marks=int(input())
attendance=int(input())
if marks >= 90:
    print("Marks requirement met.")
    if attendance >= 85:
        print("Scholarship Approved!")  
    else:
        print("Attendance requirement not met.")
else:
    print("Marks requirement not met.")
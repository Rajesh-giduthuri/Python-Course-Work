# with open("Perfect numbers.txt","w") as file1:
#     file1.write("first 5 Perfect numbers: ")
with open("Perfect numbers.txt","w") as file1:
    cou=0
    n=1
    while cou<=5:
        s=0
        for i in range(1,n):
            if n%i==0:
                s+=i
        if s==n:
            file1.write(str(n)+"\n")
            cou+=1
        n+=1
print("First 5 perfect numbers are written in Perfect numbers.txt file.")
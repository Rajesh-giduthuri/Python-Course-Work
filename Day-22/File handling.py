#file handling

#file operations : open() , write() , read() , close()

#writing into a file
file=open("test.txt","w") #write mode
data="Hi there! How are you....."
file.write(data)

file=open("test.txt","w") #write mode
data="Hello there! How are you....."
file.write(data)
file.write("Hi") #overwrites the data

#appending the data into a file
file=open("test.txt","a") #append mode
file.write("\nwelcome!")

#reading the data in the file
file=open("test.txt","r") #read mode
file.readlines()

file=open("test.txt","r") #read mode
file.read()

file.close() #every file should be closed at last
with open("filename.txt","w") as file: #with used to close the file automatically when work is done
    file.write("OOOO")
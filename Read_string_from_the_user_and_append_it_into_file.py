# Write a program to read a string from the user and append it into a file.
mystr=input("Enter your String: ")
f=open("abc.txt","w")
f.write(mystr)
f.close()
f=open("abc.txt","a")
mystr1=input("Enter another string for append: ")
f.write(mystr1)
f.close()
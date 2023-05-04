# Write a program to read and display first and last n lines from a file.
file=open("text.txt","r")
lines = file.readlines()
firstline = lines[:1]
lastline = lines[-1:]
print("first line is :", firstline)
print("last line is :", lastline)
# strip() function can be used to remove \n and spaces ;)
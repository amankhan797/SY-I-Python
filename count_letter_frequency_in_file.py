# Write a program which reads a text file and counts the number of times a certain letter Appears in the text file.
f=open("text.txt","r")
data=f.read()
word=input("Write a word for counting: ")
print(data.count(word))
f.close()
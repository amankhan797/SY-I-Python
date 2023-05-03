# Read a text file and print all the numbers present in the text file. Also print the size of the file.
numbers=[]
f=open("text.txt","r")
for line in f:
    words=line.split()
    for word in words:
        if word.isnumeric():
            numbers.append(int(word))
print(numbers)
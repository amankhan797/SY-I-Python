# Write a Python program to accept a string and from a given string where all occurrences of its first character have been changed to '$', except the first char itself.
mystr=input("Enter your string: ")
first_char = mystr[0]
newmystr = first_char + mystr[1:].replace(first_char, '$')
print(newmystr)
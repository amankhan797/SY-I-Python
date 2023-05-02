# Write text file named test.txt that contains integers, characters and float numbers. Write a Python program to read the test.txt file. And print appropriate message using exception to print whether line contains integer, character or float value.
file=open('test.txt', 'w')
file.write('10\n')
file.write("Aman khan pathan\n")
file.write('3.14\n')

file=open('test.txt', 'r')
for line in file:
    try:
        value = int(line)
        print(line," is an integer  datatype")
    except ValueError:
        try:
            value = float(line)
            print(line," is float  datatype")
        except ValueError:
            print(line ,"is characters  datatype")
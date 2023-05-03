# Write a program which accepts 10 integers and prints "DUPLICATES" if any of the values entered are duplicates otherwise prints "ALL UNIQUE".
mylist1=[]
for i in range(0,10):
    num=int(input("enter number: "))
    mylist1.append(num)
myset=set(mylist1)
mylist2=list(myset)
if len(mylist1)==len(mylist2):
    print("ALL UNIQUE")
else:
    print("DUPLICATE")
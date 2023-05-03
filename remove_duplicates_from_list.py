# Write a Python program to accept n numbers in list and remove duplicates from a list.
num=int(input("How many numbers you wantv0 tenter: "))
mylist=[]
for i in range(0,num):
    element=int(input("Enter element :"))
    mylist.append(element)
temp=set(mylist)
mylist=list(temp)
print(mylist)
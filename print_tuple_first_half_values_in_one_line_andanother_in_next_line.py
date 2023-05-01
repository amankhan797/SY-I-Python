# Write a program to create tuple of n numbers, print the first half values of tuple in one line and the last half values of tuple on next line.
num=int(input("how many elements you want to Enter :"))
mylist=[]
for i in range(0,num):
      a=int(input("Enter element"))
      mylist.append(a)
mytuple=tuple(mylist)
half=len(mytuple)//2
print("First half is :",mytuple[:half])
print("Second half is",mytuple[half:])
# Write a program to perform the add and remove operations on a set.
myset=set()
for i in range(0,5):
  a=int(input("Enter element"))
  myset.add(a) #add operation on a set.
print("Set Elements are :",myset)
b=int(input("Which element you want to remove :"))
myset.remove(b)#remove operations on a set.
print("Set Elements after remove :",myset)
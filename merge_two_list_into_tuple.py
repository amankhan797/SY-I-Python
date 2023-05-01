# Write a Python program to accept two lists and merge the two lists into list of tuple.
list1=[]
list2=[]
print("Enter values of list 1")
for i in range(0,4):
      a=int(input("Enter element"))
      list1.append(a)
print("Enter values of list 2")
for i in range(0,4):
      a=int(input("Enter element"))
      list2.append(a)      
mytuple=tuple(list1+list2)
print(mytuple) #list of tuple
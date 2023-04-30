# Write a python program which will calculate the average of the values in list passed by the user and the value should not be an empty list. If value is empty list, it should raise error.
class myexception(Exception):
  pass
mylist=[]
num=int(input("how many elements you want to insert"))
try:
  if num==0:
    raise myexception  
  else:
    for i in range(0,num):
      a=int(input("Enter element"))
      mylist.append(a)
    print("average of the values in list is :",sum(mylist)/len(mylist))
except myexception:
  print("list cannot be empty ")

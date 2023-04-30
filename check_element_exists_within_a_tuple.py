# Write a program to check if an element exists within a tuple.
mytuple=(1,2,3,4,5)
print("Tuple is :",mytuple)
a=int(input("Enter element you want to check :"))
flag=0
for i in mytuple:
  if i==a:
    flag+=1   
if flag>0:
  print("Element found")
else:
  print("Element not found")
#Program to find sum, max and min in given set.
a=int(input("How many elements you want to enter :"))
set1=set()
for i in range(0,a):
  b=int(input("Enter Element :"))
  set1.add(b)
print("sum of set is:",sum(set1))
print("Max of set is:",max(set1))
print("min of set is:",min(set1))
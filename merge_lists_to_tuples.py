# Write a Python program to accept two lists and merge the two lists into list of tuple.
mylist1=[]
mylist2=[]
merged_list=[]
size=int(input("Enter the size of List: "))
print("_____Enter elements for list 1_____")
for i in range(0,size):
    num=int(input("Enter Element :"))
    mylist1.append(num)
print("_____Enter elements for list 2_____")
for i in range(0,size):
    num=int(input("Enter Element :"))
    mylist2.append(num)

mytup1=tuple(mylist1)
mytup2=tuple(mylist2)
merged_list.append(mytup1)
merged_list.append(mytup2)
print(merged_list)
# Write a program to accept a number 'n', and display the following pattern 
# 1 
# 2 3 
# 4 5 6
num=int(input("enter range :"))
A=1
for i in range(0,num):
  for j in range(0,i):
    print(A,end=" ")
    A=A+1
  print("")
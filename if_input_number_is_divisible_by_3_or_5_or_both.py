#Write a program to check whether input number is divisible by 3 or 5 or both.
num=int(input("Enter number :"))
if (num%3==0):
  print("number is divisible by 3")  
elif(num%5==0):
  print("number is divisible by 5")
else:
  print("number is not divisible by 3 and 5")
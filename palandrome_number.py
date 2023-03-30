#program to check if the given number is palandrome or not.
num=int(input("Enter a number"))
rem=0
temp=0
rev=0
while num >0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
if(temp==rev):
    print("Number is Palandrome")
else:

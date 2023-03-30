num=int(input("Enter a number"))
rem=0
rev=0
while num >0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
print("sum of given number is : ",rev)

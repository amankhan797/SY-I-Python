#Sum of a given number.
num=int(input("Enter a number"))
sum=0	
while num >0:
    rem=num%10
    sum=sum+rem
    num=num//10
print("sum of given number is : ",sum)

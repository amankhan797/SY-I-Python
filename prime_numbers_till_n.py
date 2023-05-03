# Write a program which accepts an integer value 'n' and prints all prime numbers till 'n'.
n = int(input("Enter a number: "))
if n < 2:
    print("There are no prime numbers till", n)
else:
    print("Prime numbers till", n, "are:")

    for num in range(2, n+1):
        is_prime =0
        for i in range(2, num):
            if num % i == 0:
                is_prime+=1
        if is_prime<=0:
            print(num)
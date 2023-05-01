# Write a program which prints Fibonacci series of a number. 
a,b=0,1
print(a)
print(b)
for i in range(2, 10):
  c = a + b
  print(c)
  a, b = b, c
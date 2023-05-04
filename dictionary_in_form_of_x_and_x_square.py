# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 
# Sample Dictionary (n = 3) 
# Expected Output: {1: 1, 2: 4, 3: 9}
mydict=dict()
for key in range(1,size+1):
    value=key*key
    mydict[key]=value
print(mydict)

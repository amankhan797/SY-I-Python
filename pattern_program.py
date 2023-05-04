# Write a program to accept a number 'n', and display the following pattern 
#     * 
#    ** 
#   *** 
#  **** 
# *****
for i in range(0,6):
    print(" " * (6 - i) + "*" * i)
#Python program to check if the given string is palandrome or not
a=input("Enter String :")
if(a==a[::-1]):
  print("string is palandrome")
else:
  print("string not is palandrome")
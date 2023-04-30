#Write python program using an anonymous function to find area of circle, circumference of circle.
r=int(input("Enter radious"))
area =lambda r : print("Area is ",3.14*r**2)
area(r)
circumference =lambda r: print("circumference is :",2*3.14*r)
circumference(r)
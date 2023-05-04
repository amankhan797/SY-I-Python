# Create a class circle having member radius. Use operator overloading to add the radius of two circle objects. Also display the area of the circle.
class Circle1:
    def __init__(self):
        radius1=int(input("Enter radius of circle 1 : "))
        self.radius1=radius1
        print("Area of Circle 1 is: ", 3.14*radius1*radius1)
class Circle2:
    def __init__(self):
        radius2=int(input("Enter radius of circle 1 : "))
        self.radius2=radius2
        print("Area of Circle 1 is: ", 3.14*radius2*radius2)
obj1=Circle1()
obj2=Circle2()
print("____________________")
print("Addition of Radius is: ",int.__add__(obj1.radius1,obj2.radius2))
#Write a Python Program to create a Class Circle and Compute the Area and the Circumference of the Circle. (Use parameterized constructor).
class circle:
  r=0
  def __init__(self,r):
    self.r=r
    print("Area of circle is :",self.r*self.r*3.14)
    print("Circumference of circle is :",2*self.r*3.14)
obj=circle(7)

         

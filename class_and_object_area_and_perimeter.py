# Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area and perimeter. Display area and perimeter. Also delete the object.
class Rectangle: 
  def __init__(self,length,width):
    self.length=length
    self.width=width
  def area(self):
    print("Area of circle is :",self.length*self.width)
  def perimeter(self):
    print("Perimeter of circle is :",2*(self.length+self.width))

length=int(input("Enter length"))
width=int(input("Enter width"))  
obj=Rectangle(length,width)
obj.area()
obj.perimeter()
del obj

#python program to find the maximum salary using Array of objects(object oriented)
maxx=0
class Employee:
    Name=""
    ID=0
    Department=""
    Salary=0
    def accept(self,Name,ID,Department,Salary):
        self.Name=Name
        self.ID=ID
        self.Department=Department
        self.Salary=Salary
        global maxx
        if maxx<self.Salary:
            maxx=self.Salary
    def display(self):
        print("Employee ID is :",self.Name)
        print("Employee Name is :",self.ID)
        print("Employee Department is :",self.Department)
        print("Employee Salary : ",self.Salary)
class manager(Employee):
    bonus=0 
    def accept1(self,bonus):
        self.bonus=bonus
    def display1(self):
        print("Bonus is :",self.bonus)
        print("Total salary :",self.Salary+self.bonus)

#creating object of a class
emparray=[]
n=int(input("how many records you wanna enter :"))
for i in range(0,n):
    Name=input("Enter Name :")
    ID=int(input("Enter ID :"))
    Department=input("Enter Department :")
    Salary=int(input("Enter Salary :"))
    bonus=int(input("Enter Bonus :"))
    obj=manager()
    obj.accept(Name,ID,Department,Salary)
    obj.accept1(bonus)
    emparray.append(obj)
for i in range(0,n):
    if(maxx==emparray[i].Salary):
        emparray[i].display()
        emparray[i].display1()

#Simple class and object program in python
class teacher:
  tname=""
  tnumber=0
  tsubject=""
  tsalary=0
  def accept(self,tname,tnumber,tsubject,tsalary):
    self.tname=tname
    self.tnumber=tnumber
    self.tsubject=tsubject
    self.tsalary=tsalary
  def display(self):
    print("Teacher name is :",self.tname)
    print("Teacher number is :",self.tnumber)
    print("Teachers subject is :",self.tsubject)
    print("Teachers salary : ",self.tsalary)
#creating object of a class
n=int(input("how many records you wanna enter :"))
for i in range(0,n):
    tname=input("Enter Name :")
    tnumber=int(input("Enter number :"))
    tsubject=input("Enter Subject :")
    tsalary=int(input("Enter salary :"))
    obj=teacher()
    obj.accept(tname,tnumber,tsubject,tsalary)
    obj.display()

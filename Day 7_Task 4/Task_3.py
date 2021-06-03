# Task 3 Create a class cal3 that will calculate simple interest. Create
# constructor method which has three parameters .Create calInterest()
# method that will calculate Interest . Create display() method that will
# display Interest.

class cal3:

    def __init__ (self):
        self.p=float(input("Enter the valaue of p: "))
        self.r=float(input("Enter the valaue of r: "))
        self.t=float(input("Enter the valaue of t: "))

    def calInterest(self):
        self.i = (self.p*self.r*self.t)/100

    def display(self):
        print("Interest of this values is:",self.i)

cal=cal3()

cal.calInterest()
cal.display()
        

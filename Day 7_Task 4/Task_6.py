# Task 6 Create a class cal5 that will calculate area of a rectangle. Create
# constructor method which has two parameters .Create calArea()
# method that will calculate area of a rectangle. Create display() method
# that will display area of a rectangle

class cal6:

    def __init__(self):
        self.l= float(input("Enter the value of length: "))
        self.w= float(input("Enter the value of width: "))
    
    def calArea(self):
        self.a=self.l*self.w

    def display(self):
        print("Area of rectangle is:",self.a)

cal=cal6()

cal.calArea()
cal.display()


        
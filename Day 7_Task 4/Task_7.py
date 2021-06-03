# Task 7 Create a class cal6 that will calculate area of a square. Create setdata()
# method that should take length from the user. Create area() method
# that will calculate area . Create display() method that will display area

class cal7():

    def setdata(self):
        self.l = float(input("Enter the length of Square: "))

    def area(self):
        self.a = self.l*self.l
        print("Area of square is:",self.a)

cal=cal7()
cal.setdata()
cal.area()



# Task 2  Create a class cal2 that will calculate area of a circle. Create setdata()
# method that should take radius from the user. Create area() method
# that will calculate area . Create display() method that will display area 

class cal2:

     def setdata(self):
        self.r = int(input("Enter the radius of circle: "))

     def area(self):
        self.era=3.14*self.r*self.r

     def display(self):
        print("Area of circle is:",self.era)

cal=cal2()

cal.setdata()
cal.area()
cal.display()
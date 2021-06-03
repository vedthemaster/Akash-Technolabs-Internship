# Task 1 Create a class cal1 that will calculate sum of three numbers.Create
# setdata() method which has three parameters that contain numbers.
# Create display() method that will calculate sum and display sum

class cal1:


    def setdata(self):
        self.n1=int(input("Give First number: "))
        self.n2=int(input("Give Second number: "))
        self.n3=int(input("Give Third number: "))

    def display(self):
        n=self.n1+self.n2+self.n3
        print("Sum of 3 numbers:",n)

cal=cal1()

cal.setdata()
cal.display()


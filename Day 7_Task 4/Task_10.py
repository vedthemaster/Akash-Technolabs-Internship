# Task 10 Create a arith class. The class should have a parameterized constructor
# and methods to add, subtract and multiply two numbers and to return
# the answers

class arith:

    def __init__(self):
        self.n1 = float(input("Enter the Value of First number: "))
        self.n2 = float(input("Enter the Value of First number: "))
   
    def Sum(self):
        self.s = self.n1 + self.n2
        print("Sum of these 2 number is: ",self.s)

    def Subtract(self):
        self.sub=self.n1-self.n2
        print("Subtraction of these 2 number is: ",self.sub)

    def Multiply(self):
        self.multi=self.n1*self.n2
        print("Multiplication of these 2 number is: ",self.multi)

m=arith()

m.Sum()
m.Subtract()
m.Multiply()


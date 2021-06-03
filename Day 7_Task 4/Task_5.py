# Task 5 Consider an employee class, which contains fields such as name and
# designation. And a subclass, which contains a field salary. Write a
# program for inheriting this relation



class employee:

    def detail(self):
        name = input("Enter your name :")
        self.name =name
        designation = input("Enter your designation :")
        self.designation = designation
        

class money(employee):
     def salary(self):
         sal= int(input(" Enter your salary :"))
         self.sal = sal
         print(self.name, "," ,self.designation,"," ,self.sal)
        
mo = money()
mo.detail()
mo.salary()
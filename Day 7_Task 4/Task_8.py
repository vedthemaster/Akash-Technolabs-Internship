# Task 8 Write a program with use of inheritance: Define a class publisher that
# stores the name of the title. Derive two classes book and tape, which
# inherit publisher. Book class contains member data called page no and
# tape class contain time for playing. Define functions in the appropriate
# classes to get and print the details

class publisher:

    def t(self):
        self.title="Rich Dad and Poor Dad"
        print("Book name is",self.title)

class book(publisher):

    def page_no(self):
        print("There are 157 pages in the book")


class tape(publisher):

    def time(self):
        print("It takes 2hrs for playing the full tape")

b=book()
b.t()
b.page_no()
t=tape()
t.time()



    

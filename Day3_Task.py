#1 Calculate Ave of 5 Num

n=int(input("Enter the number of elements to be inserted :"))
a=[]
for i in range(0,n):
    elem=int(input("Enter the amount: "))
    a.append(elem)
avg=sum(a)/n
print("Averge of Numbers in list",avg)

#2 Check whether number is even or odd

n=int(input("Enter the number: "))
if (n % 2) == 0:
    print("Given num is Even")
else:
    print("Given num is Odd")


#3 Take a year and check whether it is leap year or not

year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))

#4 Take a number and check whether it is zero, positive or negative

n = int (input("Enter the number: "))

if n == 0:
    print("Given num is Zero")
elif n > 0:
    print("Given num is Positive")
else:
    print("Given num is negative")

#5 Take 2 numbers and display greatest number

a1 = int(input("Enter 1st number:"))
a2 = int(input("Enter 2nd number:"))

if a1>a2:
    print(a1," is greater")
elif a2>a1:
    print(a2," is greater")
else:
    print("Both Numbers are equal")

#6 Take a number and find factorial of that number

n= int(input("Enter the number to find Factorial:"))
factorial = 1

for i in range(1,n+1):
    factorial = factorial*i
print("factorial is :",factorial)

#7 Write a program to swap 2 numbers using third variable

a=int(input("Enter first number: "))
b=int(input("Enter Second number: "))

temp=a
a=b
b=temp

print("Value of x after swapping:",a)
print("Value of y after swapping:",b)

#8 Take 2 numbers and find smallest number

a1 = int(input("Enter 1st number:"))
a2 = int(input("Enter 2nd number:"))

if a1<a2:
    print(a1," is smallest")
elif a2<a1:
    print(a2," is smallest")
else:
    print("Both Numbers are equal")

#9 Take a number check if a number is less than 100 or not. If it is less than 100 then check if it is odd or even

a = int(input("Enter the number:"))

if a<100:
    if (a % 2) == 0:
        print("Number is less than 100 and Number is Even")
    else:
        print("Number is less than 100 and Number is Odd")
elif a==100:
    print("Number is Equal to 100")
else:
    print("Number is Greater than 100")

#10 Take a number to print the square of a number if it is less than 10

a=int(input("Enter the number to find the square of that number: "))

if a<10:
    print(a*a,"is the square of the number")
else:
    print("number is greater than 10")

#11 Take a number and check whether it is zero, positive or negative using nested IF…ELSE statement 

a=int(input("Enter the number: "))

if a<=0:
    if a == 0:
        print("Number is 0")
    else:
        print("Number is -ve")
else:
    print("Number is +ve")

#12 Take 3 numbers and find greatest number using nested IF….ELSE statement

a1 = int(input("Enter the 1st number: "))
a2 = int(input("Enter the 2nd number: "))
a3 = int(input("Enter the 3rd number: "))

if a1>a2:
    if a1>a3:
        print(a1,"is Greatest number")
    else:
        print(a3,"is Greatest number")
else:
    if a2>a3:
        print(a2,"is Greatest number")
    else:
        print(a3,"is Greatest number")

#13 Take 3 numbers and find smallest number using logical operator

a1 = int(input("Enter the 1st number: "))
a2 = int(input("Enter the 2nd number: "))
a3 = int(input("Enter the 3rd number: "))

smallest = 0

if a1<a2 and a1<a3:
    smallest = a1
elif a2<a3:
    smallest = a2
else:
    smallest = a3

print(smallest,"is ths smallest number")

#14 Write a program to swap 2 numbers without taking third variable

a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))

a,b=b,a

print("after swapping...")

print(a,"is 1st Number")
print(b,"is 2nd Number")

#15 Take starting number and ending number from the user and print following series

a=int(input("Enter Starting Number:"))
b=int(input("Enter Ending Number:"))

for i in range(a,b+1,-3):
    print("the series is",i)







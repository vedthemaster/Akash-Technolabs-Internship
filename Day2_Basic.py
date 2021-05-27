#Task 1
print('Hello World')
#Task 2 
a,b,c = 1,2,"Ved Patel"
print('Value of a is = ',a)
print('Value of b is = ',b)
print('My Name is = ',c)
#Task 3
name = "Ved"
print("My Name is = ", name)
print(name[0])
print(name[1:3])
print(name[-1])
#Task 4
list1 = [1,3,"Ved",100,"Internship"]
print([list1])
#Task 5
print("list1[2] = ", list1[2])
print("list1[1:4] = ", list1[1:4])
#Task 6
list2 = []
n = int(input('Enter number of elements : '))
for i in range(0,n):
    element = input('Enter Value: ')
    list2.append(element)
print(list2)
#Task 7
tuple1 = [1,3,"Ved",100,"Internship",50,"Python"]
print([tuple1])
print("tuple1[1] = ", list1[1])
print("tuple1[5:] = ", list1[5:])
#Task 8
list2 = []
n = int(input('Enter number of elements : '))
for i in range(0,n):
    element = input('Enter Value: ')
    list2.append(element)
tup = tuple(list2)
print(list2)
print(tup)
#Task 9
d = {1:'Ved', 2 : 'Patel', 'Internship': 'Python'}
print(type(d))
print('d[1] = ',d[1])
print('d[2] = ',d[2])
print('d["Internship"] = ',d["Internship"])
#Task 10
dict = {}
for tonum in range(0,int(input('Input the total number: '))):
    a,b = input('Enter the key value pair : ').split()
    if a in dict:
        dict[a].append(b)
    else:
        dict[a]=[b]
print(dict)

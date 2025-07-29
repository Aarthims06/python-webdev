#variable
a = 10
b = 10
print(a+b)
#datatype
a = 10
print(type(a)) #returns the datatype of a
b = "hello"
print(type(b))
#operator
a = 10
b = 30
c = a+b
print(c)
#before casting
a = "10" #something within "" is considered as string
b = "20"
c = a+b
print(c) #returns 1020
#after casting
a = int("10") #converting one datatype to another
b = int("20")
c = a+b
print(c)
#task1
name = input("Enter your name:")
age = int(input("Enter your age:"))
print(f"{name} is {age} years old")
#task2
a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
c = int(input("Enter 3rd number:"))
d = a*b*c
e = a+b+c
f = d/e
print(d)
print(e)
print(f)
#task3
name = input("Enter your name:")
score = int(input("Enter score:"))
if score<=100:
    a = score/10
dept = input("Enter your dept:")
print("My name is ",name)
print("My score is ",a,"/10")
print("My dept is ",dept)

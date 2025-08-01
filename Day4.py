#task4
a = int(input("Enter a number:"))
if(a%2 == 0):
    print("The number is even")
else:
    print("The number is odd")

#task5
b = int(input("Enter your score:"))
if(b<35):
    print("poor student")
elif(b>35 and b<70):
    print("average student")
else:
    print("Good student")

#task6
a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
operation = input("Whether to add/sub/mul/div ?")
if(operation == "add"):
    print(a+b)
elif(operation == "sub"):
    print(a-b)
elif(operation == "mul"):
    print(a*b)
elif(operation == "div"):
    print(a/b)
else:
    print("invalid input")

#task7
score = int(input("Enter score percentage:"))
if(score>70):
    name = input("Name:")
    dept = input("Department:")
    loc = input("Location:")
    print("You are eligible")
else:
    print("You are not eligible")
    

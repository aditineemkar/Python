print("A Calculator")
var1 = input("Enter the first number:- ")
var2 = input("Enter the second number:- ")
operation = input("What mathematical operation do you want to perform?")
print("Type 1 for substraction")
print("Type 2 for addition")
print("Type 3 for multiplication")
print("Type 4 for division")

if operation==1:
    print(var1-var2)
elif operation==2:
    print(var1+var2)
elif operation==3:
    print(var1*var2)
elif operation==4:
    print(var1/var2)

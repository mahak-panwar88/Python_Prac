#Conditional Statement
# if-else statement
age = 19
if age>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
# match case statements
number = 3
match number:
    case 1:
        print("One")
    case 2|3:
        print("Two or three")
    case _:
        prin("Other number")
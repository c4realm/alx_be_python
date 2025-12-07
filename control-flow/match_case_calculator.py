
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#the goal of the question is to use match case to build a simple calculator

operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        if( num2 == 0):
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print("The result is {result}.")
    case _:
        print("Invaild try again")



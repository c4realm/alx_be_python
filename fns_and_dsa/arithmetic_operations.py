def perform_operation(num1, num2, operation):
    #add
    if operation == "add":
        return num1 + num2
    #subtract
    elif operation == "subtract":
        return num1 - num2
    # *
    elif operation == "multiply":
        return num1 * num2
    #division
    elif operation == "divide":
        if num2 == 0:
            return "Erro: Cannot divide by zero"
        return num1 / num2
    else:
        return "Error: Unknown operation"


    

def calculator():
    print("Simple Calculator")
    num1 = float(input("Enter First number:"))
    op=input("Enter operator (+ ,- ,*,/):")
    num2 = float(input("Enter Second number:"))
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 != 0 :
           result = num1 / num2            
        else:
            result = "Error: Division by zero"
    else:
            result = "Invlalid operator"   
    print("Result =", result)
calculator()
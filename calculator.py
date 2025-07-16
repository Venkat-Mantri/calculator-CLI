operation = input("Enter operation (add, sub, mul, div): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operation == "add":
    result = num1 + num2
elif operation == "sub":
    result = num1 - num2
elif operation == "mul":
    result = num1 * num2
elif operation == "div":
    if num2 == 0:
        result = "Error: Cannot divide by zero"
    else:
        result = num1 / num2
else:
    result = "Error: Unknown operation"

print("Result:", result)

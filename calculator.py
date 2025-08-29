num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
    print(f"{int(num1) if num1.is_integer() else num1} + {int(num2) if num2.is_integer() else num2} = {int(result) if result.is_integer() else result}")
elif operation == "-":
    result = num1 - num2
    print(f"{int(num1) if num1.is_integer() else num1} - {int(num2) if num2.is_integer() else num2} = {int(result) if result.is_integer() else result}")
elif operation == "*":
    result = num1 * num2
    print(f"{int(num1) if num1.is_integer() else num1} * {int(num2) if num2.is_integer() else num2} = {int(result) if result.is_integer() else result}")
elif operation == "/":
    result = num1 / num2
    print(f"{int(num1) if num1.is_integer() else num1} / {int(num2) if num2.is_integer() else num2} = {int(result) if result.is_integer() else result}")
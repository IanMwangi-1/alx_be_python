# match_case_calculator.py

# Simple Calculator using if-elif (Python 3.8 compatible)

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
    print(f"The result is {result}")
elif operation == "-":
    result = num1 - num2
    print(f"The result is {result}")
elif operation == "*":
    result = num1 * num2
    print(f"The result is {result}")
elif operation == "/":
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        result = num1 / num2
        print(f"The result is {result}")
else:
    print("Invalid operation selected.")


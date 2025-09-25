def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations.

    Parameters:
    - num1 (float): first number
    - num2 (float): second number
    - operation (str): 'add', 'subtract', 'multiply', 'divide'

    Returns:
    - result of the operation (float) or error message (str)
    """

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"


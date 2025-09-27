
# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations: add, subtract, multiply, divide.

    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (str): The operation to perform: 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
    float or str: The result of the arithmetic operation, or an error message if invalid.
    """
    
    # Check which operation was requested
    if operation == "add":
        return num1 + num2
    
    elif operation == "subtract":
        return num1 - num2
    
    elif operation == "multiply":
        return num1 * num2
    
    elif operation == "divide":
        if num2 == 0:   # Division by zero check
            return "Error: Cannot divide by zero."
        return num1 / num2
    
    else:
        # If the operation is not recognized
        return "Error: Invalid operation."

    
    


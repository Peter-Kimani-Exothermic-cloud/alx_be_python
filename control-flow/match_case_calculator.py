#User input section
#First we ask user to enter the first number.
#We use float() to convert the text the user types into a number
# that can have decimal places (like 3.14). This is stored in the 'num1' variable.

num1 = float(input("Enter the first number:"))

#do the same for the 2nd number

num2 = float(input("Enter the second number:"))

operation = input("Choose the operation (+, -, *, /):")

# --- Match Case Logic Section ---
# The 'match' statement checks the value of the 'operator' variable.
# It then looks for a 'case' that matches that value.
# When it finds a match, it runs the code indented below that 'case'.
match operation:
    # Case 1: If the user entered "+", this code runs.
    case '+':
        # We calculate the sum and store it in the 'result' variable.
        result = num1 + num2
        # Then, we print a friendly message with the final result.
        print(f"The result is {result}.")

    case '-':
        result = num1 - num2
        print(f"The result is {result}.")

    case '*':
        result = num1 * num2
        print(f"The result is {result}.")
    
    case '/':
        # For division, we have to be careful! We cannot divide by zero.
        # So, we use an 'if' statement to check if 'num2'
        if num2 == 0:
            print("Cannot divide by zero.")
         # If 'num2' is not zero, it's safe to perform the division. 
        else:
            # If 'num2' is not zero, it's safe to perform the division.
            result = num1 / num2
            print(f"The result is {result}.")
    
    case _:
        # We let the user know their input was not valid.
        print("Please enter a valid operation")





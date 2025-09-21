# This script draws a square pattern of asterisks (*) based on a size
# provided by the user. We will use nested loops to achieve this.

# --- User Input Section ---
# First, we ask the user to enter a number for the size of the square.
# We convert the input to an integer using int() because the size must be a whole number.
size = int(input("Enter the size of the pattern: "))

# We'll use a variable to keep track of which row we are currently drawing.
# We start at 0, since it's a good practice in programming to start counting from zero.
row_counter = 0

# --- Nested Loops Logic Section ---
# This is our outer loop. It will continue to run as long as our 'row_counter'
# is less than the 'size' the user entered.
# It handles the movement from one row to the next.
while row_counter < size:
    # This is our inner loop. It's "nested" inside the while loop.
    # It will run 'size' number of times for each time the outer loop runs.
    # Its job is to print the asterisks for a single row.
    # The 'range(size)' gives us numbers from 0 up to (but not including) the 'size'.
    for i in range(size):
        # We print an asterisk (*). The 'end=""' is a very important part!
        # It tells the print function to NOT move to a new line after printing.
        # This keeps all the asterisks for the current row on the same line.
        print("*", end="")
    
    # After the inner loop finishes drawing a full row of asterisks,
    # this print() statement runs.
    # Without any text inside, it simply moves the cursor to a new line,
    # so the next row starts below the previous one.
    print()

    # We increase our row counter by 1. This is crucial!
    # Without this line, the 'while' loop would run forever,
    # because 'row_counter' would never become equal to 'size'.
    row_counter += 1

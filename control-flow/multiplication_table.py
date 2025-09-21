# This script generates a multiplication table for a number provided by the user.
# We will use a 'for' loop to repeat the calculation and printing process.


#User input section
number = int(input("Enter a number to see its multiplication table:"))

# --- Loop and Calculation Section ---

# Now, we start our 'for' loop.
# The 'range(1, 11)' creates a sequence of numbers from 1 up to (but not including) 11.
# So, the numbers will be 1, 2, 3, 4, 5, 6, 7, 8, 9, and 10.
# The variable 'i' will take on each of these values one by one in the loop.

for i in range(1, 11):
    # Inside the loop, we perform the calculation.
    # We multiply the 'number' the user entered by the current value of 'i'.
    # For example, in the first loop, it will be number * 1.
    # In the second loop, it will be number * 2, and so on.
    product = number * i

    # Finally, we print the result for each line of the table.
    # We use an f-string (the 'f' before the quotes) to easily include
    # the values of our variables directly in the text.
    print(f"{number} * {i} = {product}")

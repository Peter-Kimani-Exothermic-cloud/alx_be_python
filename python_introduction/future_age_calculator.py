#Objective: Practice receiving user input in Python and perform a simple arithmetic 
#Operation to calculate the user’s age in a future year.

#Task Description:
#Create a Python script that asks the user for their current 
#And then calculates how old they will be in a specific future year. 
#This task introduces handling user input and reinforces arithmetic operations.

#Instructions:
#Create a file named future_age_calculator.py.
#Prompt the user to input their current age with the question: “How old are you? ”.
#Assume the user will input a valid integer value.
#Calculate how old the user will be in the year 2050. To keep calculations simple, assume the current year is 2023. Therefore, you need to add 27 years to the user’s current age.
#Print the user’s age in 2050 in the format: In 2050, you will be [age] years old.

#Expected Script Flow:
#The script prompts the user for their current age.
#The user enters their age.
#The script calculates and prints how old the user will be in 2050.

#Example Interaction:
#If the user inputs 30 when prompted for their current age, the output should be:
#In 2050, you will be 57 years old.


# This is a Python script that will calculate a user's future age.
# It's a great first program because it covers some of the most basic and important concepts:
# 1. Getting information from the user.
# 2. Doing a simple math calculation.
# 3. Displaying the result back to the user.


#SOLUTION
# --- Step 1: Get the user's current age ---
# The 'input()' function is what we use to ask the user a question
# and wait for them to type something and press Enter.
# The question, "How old are you? ", is the text that will be shown
# to the user.
# When the user types their answer, 'input()' gives us that answer back as
# a string (a sequence of characters, like text).
# We store this text in a variable called 'current_age_str'.
# Think of a variable like a labeled box where you can temporarily
# store a piece of information.


# --- Step 2: Convert the age to a number and do the math ---
# The value we got from 'input()' is a string, but to do math,
# we need a number. This is a crucial step!
# We use the 'int()' function to convert the string 'current_age_str'
# into an integer (a whole number).
# We store this number in a new variable called 'current_age'.
# For example, if the user typed "30", 'current_age' will now hold the number 30.


# Now for the calculation. The problem asks us to find the age in 2050,
# assuming the current year is 2023. That's a difference of 27 years (2050 - 2023).
# We simply add 27 to the user's current age.


# --- Step 3: Print the final result ---
# The 'print()' function displays information on the screen.
# We want to show a specific message: "In 2050, you will be [age] years old."
# To make this easy, we use something called an f-string.
# An f-string is a string that starts with an 'f' before the quotes.
# Inside the string, you can put curly braces '{}' with a variable inside,
# and Python will automatically replace it with the variable's value.
# This makes it very easy to combine text with variables.


current_age_str = input( "How old are you?" )


current_age = int(current_age_str)

age_in_2050 = current_age + 27

print(f"In 2050, you will be {age_in_2050} years old.")



#Objective: Use user input, variables, and arithmetic operations 
# #to calculate and provide feedback on a user’s monthly savings, without applying conditional statements.
#Task Description:
# You will create a script named finance_calculator.py.
# This script will calculate the user’s monthly savings based on inputted monthly income and expenses. 
# It will then project these savings over a year, assuming a fixed interest rate, to demonstrate compound interest’s effect on savings.


monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your total monthly expenses: ")


monthly_savings = float(monthly_income) - float(monthly_expenses)

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are ${monthly_savings:}")
print(f"Projected savings after one year, with interest, is: ${projected_savings:}")








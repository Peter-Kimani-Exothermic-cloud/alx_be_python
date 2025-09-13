#Objective: Use user input, variables, and arithmetic operations 
# #to calculate and provide feedback on a user’s monthly savings, without applying conditional statements.
#Task Description:
# You will create a script named finance_calculator.py.
# This script will calculate the user’s monthly savings based on inputted monthly income and expenses. 
# It will then project these savings over a year, assuming a fixed interest rate, to demonstrate compound interest’s effect on savings.


#Getting user input
monthly_income = input("Enter your monthly income:")
monthly_income = float(monthly_income)

monthly_expenses = input("Enter your total monthly expenses:")
monthly_expenses = float(monthly_expenses)

#Calculating savings
annual_interest_rate = 0.05
monthly_savings = monthly_expenses - monthly_income


projected_annual_savings = monthly_savings * 12 + monthly_savings * 12 * 0.05 







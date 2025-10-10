#Define a function

def safe_divide(numerator, denominator):
   
    try:
        #Convert inputs to float
        numtor = float(numerator)
        dentor = float(denominator)
        result = numtor / dentor
        return f"The result of te division is {result}"
    
    except ZeroDivisionError:
        print("Error: Cannot divide by 0")
    
    except ValueError:
        print("Error: Please enter a number")
    
    finally:
        print("Division Successful")
    




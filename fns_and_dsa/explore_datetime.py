from datetime import datetime, timedelta

def display_current_datetime():
    """
    Part 1: Gets and displays the current date and time.
    """
    # 1. Get the current date and time
    # datetime.now() returns an object representing the exact moment this line ran.
    current_date = datetime.now()

    # 2. Format and print the result as YYYY-MM-DD HH:MM:SS
    # strftime is a function to format the datetime object into a readable string.
    # %Y = Year with century (2024), %m = Month as a number (03), %d = Day of the month (25)
    # %H = Hour (24-hour clock), %M = Minute, %S = Second
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """
    Part 2: Prompts the user for a number of days and calculates a future date.
    """
    # Loop to ensure the user enters a valid integer
    while True:
        try:
            # Prompt the user for input and convert it to an integer
            days_to_add = int(input("\nEnter the number of days to add to the current date: "))
            break # Exit the loop if conversion was successful
        except ValueError:
            print("Invalid input. Please enter a whole number (e.g., 10).")

    # Get the current date again (in case a lot of time passed during user input)
    current_date = datetime.now()
    
    # Define the duration we want to add
    # timedelta is a class that represents a duration, or a difference between two dates.
    time_difference = timedelta(days=days_to_add)
    
    # Calculate the future date
    # You can simply add a datetime object and a timedelta object together!
    future_date = current_date + time_difference
    
    # Print the future date in YYYY-MM-DD format
    # Notice we only include %Y, %m, and %d to show just the date part.
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")


def main():
    """
    The main execution function that runs both parts of the task.
    """
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()



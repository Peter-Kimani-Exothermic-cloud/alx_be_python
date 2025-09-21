# This script creates a personalized daily reminder based on a task's priority and time sensitivity.
# It uses 'match case' and 'if' statements to provide a customized message.

# --- User Input Section ---
# First, we ask the user to enter the description of their task.
# The text they type is stored in the 'task' variable.
task = input("Enter your task: ")

# Next, we ask for the priority level. We'll make sure to get a lowercase version
# of the input right away for easier comparison.
priority = input("Priority (high/medium/low): ").lower()

# Then, we ask if the task is time-bound. We also convert this to lowercase.
time_bound = input("Is it time-bound? (yes/no): ").lower()

# We'll create a variable to hold the final reminder message.
reminder_message = ""

# --- Match Case Logic Section ---
# We use a 'match case' statement to create the entire reminder message
# based on the priority the user entered. This makes the logic cleaner.
match priority:
    # If the user typed "high", this case runs.
    case 'high':
        reminder_message = f"Reminder: '{task}' is a high priority task"
    
    # If the user typed "medium", this case runs.
    case 'medium':
        reminder_message = f"Reminder: '{task}' is a medium priority task"
        
    # If the user typed "low":
    case 'low':
        # The specific message for low priority is handled here directly.
        reminder_message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    
    # The default case for any other input (like 'urgent' or a typo).
    case _:
        # This is a fallback if the priority is not high, medium, or low.
        reminder_message = f"Reminder: '{task}' is a task"

# --- Conditional Logic (if statement) Section ---
# Now, we check if the task is time-bound. This check happens after the
# main message is built, so we can modify it if needed.
if time_bound == 'yes':
    # We add the "immediate attention" phrase only if the priority is not low.
    # This prevents a low-priority task from being marked as urgent.
    if priority != 'low':
        # We concatenate the strings to add the new phrase.
        reminder_message += " that requires immediate attention today!"

# --- Output Section ---
# Finally, we print the complete, customized reminder message.
print(reminder_message)


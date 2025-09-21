# This script creates a personalized daily reminder based on a task's priority and time sensitivity.
# It uses 'match case' and 'if' statements to provide a customized message.

# --- User Input Section ---
# First, we ask the user to enter the description of their task.
# The text they type is stored in the 'task' variable.
task = input("Enter your task: ")

# Next, we ask for the priority level.
# We'll expect them to type "high", "medium", or "low".
# This input is stored in the 'priority' variable.
priority = input("Priority (high/medium/low): ")

# Then, we ask if the task is time-bound.
# We'll expect them to type "yes" or "no".
# The input is stored in the 'time_bound' variable.
time_bound = input("Is it time-bound? (yes/no): ")

# We'll create a variable to hold the reminder message. We'll build on this as we go.
reminder_message = ""

# --- Match Case Logic Section ---
# We use a 'match case' statement to create the first part of our reminder message
# based on the priority the user entered.
match priority.lower():
    # If the user typed "high" (or HIGH, High, etc., thanks to .lower()), this case runs.
    case 'high':
        # We start building the message.
        reminder_message = f"Reminder: '{task}' is a high priority task"
    
    # If the user typed "medium", this case runs.
    case 'medium':
        reminder_message = f"Reminder: '{task}' is a medium priority task"
        
    # If the user typed "low", this case runs.
    case 'low':
        reminder_message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    
    # The default case for any other input (like 'urgent' or a typo).
    case _:
        reminder_message = f"Reminder: '{task}' is a task"

# --- Conditional Logic (if statement) Section ---
# Now, we use an 'if' statement to check if the task is time-bound.
# We check if the user's input, converted to lowercase, is "yes".
if time_bound.lower() == 'yes':
    # If it is, we add the "requires immediate attention" phrase to our message.
    # We use a special if statement here to check if the priority is low.
    # If the priority is low, we don't want to add the "immediate attention" message.
    if priority.lower() == 'low':
        # In this case, we don't add anything. The message is already set above.
        pass
    else:
        # We concatenate the strings to add the new phrase.
        reminder_message += " that requires immediate attention today!"

# --- Output Section ---
# Finally, we print the complete, customized reminder message.
print(reminder_message)

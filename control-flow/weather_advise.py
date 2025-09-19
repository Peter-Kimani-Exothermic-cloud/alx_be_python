# 1. Prompt the user for weather input
# The input() function gets text from the user. We'll store it in a variable.
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# 2. Provide clothing recommendations based on the input

# If the weather is exactly "sunny"...
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")

# Else if the weather is exactly "rainy"...
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")

# Else if the weather is exactly "cold"...
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")

# If none of the above conditions are met...
else:
    print("Sorry, I don't have recommendations for this weather.")

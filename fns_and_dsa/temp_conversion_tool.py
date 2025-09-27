# temp_conversion_tool.py

# ---- Global conversion factors ----
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9   # multiply by this when converting F → C
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5   # multiply by this when converting C → F
FREEZING_POINT_FAHRENHEIT = 32         # the offset used in conversions

# ---- Conversion functions ----
def convert_to_celsius(fahrenheit):
    """
    Convert a Fahrenheit temperature to Celsius using the global factor.
    Formula: (F - 32) * (5/9)
    """
    return (fahrenheit - FREEZING_POINT_FAHRENHEIT) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert a Celsius temperature to Fahrenheit using the global factor.
    Formula: (C * (9/5)) + 32
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_FAHRENHEIT

# ---- Main program ----
def main():
    try:
        # Step 1: Ask for the temperature
        temp_input = input("Enter the temperature to convert: ").strip()

        # Try converting the input into a float (to ensure it's numeric)
        temperature = float(temp_input)

        # Step 2: Ask for the unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Step 3: Decide which conversion to apply
        if unit == "F":
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted}°C")

        elif unit == "C":
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted}°F")

        else:
            # User entered neither "C" nor "F"
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        # This block catches both non-numeric input and wrong unit
        print(f"Invalid temperature. {e}")

if __name__ == "__main__":
    main()

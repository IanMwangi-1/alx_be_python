# temp_conversion_tool.py

# Define global conversion factors exactly as required
FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    Accepts numeric input or raises ValueError with exact message on bad input.
    """
    try:
        f = float(fahrenheit)
    except (TypeError, ValueError):
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    return (f - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    Accepts numeric input or raises ValueError with exact message on bad input.
    """
    try:
        c = float(celsius)
    except (TypeError, ValueError):
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    return (c * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    # User interaction: exact prompts required by the checker
    temperature_input = input("Enter the temperature to convert: ")
    # convert_to_* will raise ValueError with the exact message if input is invalid
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "F":
        result = convert_to_celsius(temperature_input)
        # ensure the input is shown as a float in output
        temp_val = float(temperature_input)
        print(f"{temp_val}°F is {result}°C")
    elif unit == "C":
        result = convert_to_fahrenheit(temperature_input)
        temp_val = float(temperature_input)
        print(f"{temp_val}°C is {result}°F")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()

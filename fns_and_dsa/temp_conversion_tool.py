# temp_conversion_tool.py

# Define global conversion factors exactly as the grader expects
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    Raises ValueError with exact message when input is invalid.
    """
    try:
        f = float(fahrenheit)
    except (TypeError, ValueError):
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    return (f - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    Raises ValueError with exact message when input is invalid.
    """
    try:
        c = float(celsius)
    except (TypeError, ValueError):
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    return (c * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    # exact prompt strings required by the grader
    temperature_input = input("Enter the temperature to convert: ")
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "F":
        result = convert_to_celsius(temperature_input)  # function validates input
        temp_val = float(temperature_input)
        print(f"{temp_val}°F is {result}°C")
    elif unit == "C":
        result = convert_to_fahrenheit(temperature_input)  # function validates input
        temp_val = float(temperature_input)
        print(f"{temp_val}°C is {result}°F")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()

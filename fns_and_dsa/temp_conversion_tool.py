#!/usr/bin/env python3

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global factor.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global factor.
    """
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    # Prompt for temperature (must be numeric)
    temp_str = input("Enter the temperature to convert: ")
    try:
        temp_value = float(temp_str)
    except ValueError:
        # Requirement: raise an error with this exact message for invalid numeric input
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Prompt for unit (C or F)
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'F':
        result = convert_to_celsius(temp_value)
        # Print like the examples: input as float with one decimal, result as Python float string
        print(f"{temp_value:.1f}°F is {result}°C")
    elif unit == 'C':
        result = convert_to_fahrenheit(temp_value)
        print(f"{temp_value:.1f}°C is {result}°F")
    else:
        # Simple message for wrong unit (not required to raise)
        print("Invalid unit. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    main()

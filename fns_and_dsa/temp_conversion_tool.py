# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit - Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius - Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


# Prompt user for input
temp_input = input("Enter the temperature  (numeric value): ")
temp_value = float(temp_input)  

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

# Conversion logic
if unit == "C":
        result = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {result:.2f}°F")

elif unit == "F":
        result = convert_to_celsius(temp_value)
        print(f"{temp_value}°F is {result:.2f}°C")

else:
        raise ValueError("Invalid temperature. Please enter a numeric value.")



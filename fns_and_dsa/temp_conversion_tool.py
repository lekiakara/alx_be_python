# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


# Implement Conversion Functions
def convert_to_celsius(fahrenheit):
    FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


# Main Program 
def main():
    try:
        # Get temperature input
        temp_input = input("Enter the temperature to convert: ")

        # Validate numeric input
        if not temp_input.replace(".", "", 1).isdigit() and not (
            temp_input.startswith("-") and temp_input[1:].replace(".", "", 1).isdigit()
        ):
            raise ValueError("Invalid temperature. Please enter a numeric value.")

        temperature = float(temp_input)

        # Ask for unit type
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "C":
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted}°F")
        elif unit == "F":
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        print(e)


# Run the program only if executed directly
if __name__ == "__main__":
    main()

"""Temperature conversion exercise in python
Define two functions
"""

def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Converts temperature from Celsius to Fahrenheit
    :param celsius: Temperature in Celsius
    """
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Converts temperature from Fahrenheit to Celsius
    :param fahrenheit: Temperature in Fahrenheit
    """
    return (fahrenheit - 32) * 5 / 9

def main():
    """
    Main program function
    :no params passed
    """
    print("Let's convert some temperatures!")
    while True:

        conv_type: str = input(
            "Celsius to Fahrenheit(C) or Fahrenheit to Celsius(F)? C or F:"
        ).upper()
        if conv_type not in ("C", "F"):
            print("Invalid input. Please try again.")
            continue

        try:
            temp_str: float = input("What is the starting temperature?: ")
            temp = float(temp_str)
        except ValueError:
            print("Invalid input. Please enter a numeric value (e.g., 25 or 98.6).")
            continue

        if conv_type == "C":
            converted_temp = celsius_to_fahrenheit(temp)
            print(f"{temp} C is {converted_temp:.1f} F.")
        else:
            converted_temp = fahrenheit_to_celsius(temp)
            print(f"{temp} F is {converted_temp:.1f} C.")

        repeat: str = input("Would you like to convert another temperature? Y or N:").upper()
        if repeat != "Y":
            break

if __name__ == "__main__":
    main()

# EOF
#

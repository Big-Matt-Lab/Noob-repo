"""
Temperature conversion exercise in python. Simple intergration of 
two functions to perform temperature conversions. Main exercise was to
incorporate error handling and to write clean code in a most pythonic way.

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

    This function prompts the user to choose a conversion type and enter a 
    temperature. It validates the inout, calls the appropriate function and 
    and prints the formatted result to the console. The program repeats
    until the user decides to stop.

    :return: None
    """
    print()
    print("Let's convert some temperatures!")
    while True:

        print()
        conversion_type: str = input(
            "Celsius to Fahrenheit(C) or Fahrenheit to Celsius(F)? C or F:").upper()
        if conversion_type not in ("C", "F"):
            print("Invalid input. Please try again.")
            continue

        try:
            temp_str = input("What is the starting temperature?: ")
            temp = float(temp_str)
        except ValueError:
            print("Invalid input. Please enter a numeric value (e.g., 25 or 98.6).")
            continue

        if conversion_type == "C":
            converted_temp = celsius_to_fahrenheit(temp)
            print(f"{temp} °C is {converted_temp:.1f} °F.")
        else:
            converted_temp = fahrenheit_to_celsius(temp)
            print(f"{temp} °F is {converted_temp:.1f} \u00B0C.")
            
        print()

        repeat = input("Would you like to convert another temperature? Y or N:").upper()
        if repeat != "Y":
            print()
            break

if __name__ == "__main__":
    main()

# EOF
#

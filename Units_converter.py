# Function for taking inputs
def get_input(prompt):
    while True:
        try:
            return float(input(prompt))  # Ask user and convert to float
        except ValueError:
            print("\nInvalid input! Please enter a valid number.\n")

# Banner
print("=" * 40)
print("           UNIT CONVERTER            ")
print("=" * 40)

# Conversion functions
def km_to_miles():
    km = get_input("Enter Kilometers: ")
    print(f"{km} Kilometers = {km * 0.621371:.2f} Miles\n")

def miles_to_km():
    miles = get_input("Enter Miles: ")
    print(f"{miles} Miles = {miles / 0.621371:.2f} Kilometers\n")

def kg_to_pounds():
    kg = get_input("Enter Kilograms: ")
    print(f"{kg} Kilograms = {kg * 2.20462:.2f} Pounds\n")

def pounds_to_kg():
    pounds = get_input("Enter Pounds: ")
    print(f"{pounds} Pounds = {pounds / 2.20462:.2f} Kilograms\n")

def c_to_f():
    celsius = get_input("Enter Celsius: ")
    print(f"{celsius}°C = {(celsius * 9 / 5) + 32:.2f}°F\n")

def f_to_c():
    fahrenheit = get_input("Enter Fahrenheit: ")
    print(f"{fahrenheit}°F = {(fahrenheit - 32) * 5 / 9:.2f}°C\n")

def inches_to_feet():
    inches = get_input("Enter Inches: ")
    print(f"{inches} Inches = {inches / 12:.2f} Feet\n")

def feet_to_inches():
    feet = get_input("Enter Feet: ")
    print(f"{feet} Feet = {feet * 12:.2f} Inches\n")

def meters_to_cm():
    meters = get_input("Enter Meters: ")
    print(f"{meters} Meters = {meters * 100:.2f} Centimeters\n")

def cm_to_meters():
    cm = get_input("Enter Centimeters: ")
    print(f"{cm} Centimeters = {cm / 100:.2f} Meters\n")

def inches_to_meters():
    inches = get_input("Enter Inches: ")
    print(f"{inches} Inches = {inches * 0.0254:.2f} Meters\n")

def meters_to_inches():
    meters = get_input("Enter Meters: ")
    print(f"{meters} Meters = {meters / 0.0254:.2f} Inches\n")

def inches_to_cm():
    inches = get_input("Enter Inches: ")
    print(f"{inches} Inches = {inches * 2.54:.2f} Centimeters\n")

def cm_to_inches():
    cm = get_input("Enter Centimeters: ")
    print(f"{cm} Centimeters = {cm / 2.54:.2f} Inches\n")

# Dictionary mapping
conversions = {
    1: ("Kilometers to Miles", km_to_miles),
    2: ("Miles to Kilometers", miles_to_km),
    3: ("Kilograms to Pounds", kg_to_pounds),
    4: ("Pounds to Kilograms", pounds_to_kg),
    5: ("Celsius to Fahrenheit", c_to_f),
    6: ("Fahrenheit to Celsius", f_to_c),
    7: ("Inches to Feet", inches_to_feet),
    8: ("Feet to Inches", feet_to_inches),
    9: ("Meters to Centimeters", meters_to_cm),
    10: ("Centimeters to Meters", cm_to_meters),
    11: ("Inches to Meters", inches_to_meters),
    12: ("Meters to Inches", meters_to_inches),
    13: ("Inches to Centimeters", inches_to_cm),
    14: ("Centimeters to Inches", cm_to_inches)
}

# Main loop
while True:
    print("\nChoose a conversion option:")
    print("0 - Exit\n")

    for key, (name, _) in conversions.items():
        print(f"{key}. {name}")
    print()

    try:
        choice = int(input("Enter your choice: ").strip())
    except ValueError:
        print("\nInvalid input! Please enter a number.\n")
        continue

    if choice == 0:
        print("\nThanks for using this Unit Converter!\n")
        break

    elif choice in conversions:
        print("-" * 40)
        conversions[choice][1]()  # Execute the function
        print("-" * 40)
    else:
        print("\nInvalid choice! Please select a valid option.\n")


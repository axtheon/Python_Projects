# Function for taking inputs
def get_input(prompt):
    while True:  # keep looping until valid input
        try:
            return float(input(prompt)) # The prompt will be given at the time of usage
        except ValueError:
            print("\nInvalid input! Please enter a number.\n")

 # Banner
print("="*25)
print("   UNIT CONVERTER   ")
print("="*25)

# Functions for conversion
def km_to_miles():
    km = get_input("Enter Kilometers: ") # Using the function for inputs and adding prompt
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
    10: ("Centimeters to Meters", cm_to_meters)
}


while True:
    print("\nChose an option:")
    print("0 to exit")
    for key, (name,_) in conversions.items(): # Prints the conversions dictionary ignoring the functions
        print(f"{key}: {name}")
    print()

    try:
        choice = int(input("Enter your choice: ").strip())
    except ValueError:
        print("\nInvalid input! Please enter a number.\n")
        continue

    if choice == 0:
        print("\nThanks for Using this program!\n")
        break

    elif choice in conversions: # Checks if any key in the conversions matches the choice
        conversions[choice][1]() # Calls the function

    else:
        print("\nInvalid input! Please enter a number assigned to the choices.\n")

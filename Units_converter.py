print("\nThis is a Unit converter.")
print("Enter 0 to quit!\n")

while True:
    try:
        choice = int(input("""1. Kilometers to Miles.
2. Miles to Kilometers.
3. Celsius to Fahrenheit.
4. Fahrenheit to Celsius.
5. Kilogram to Pounds.
6. Pounds to Kilogram.\n
Enter a number assigned to the Units: """))
    except ValueError:
        print("\nInvalid input! Please enter a number.\n")
        continue

    if choice == 0:
        break

    elif choice == 1:
        try:
            kilometers = float(input("Enter Kilometers: "))
        except ValueError:
            print("\nInvalid input! Please enter a number.\n")
            continue
        miles = kilometers * 0.621371
        print(f"{kilometers} Kilometers = {miles:.2f} Miles\n")

    elif choice == 2:
        try:
            miles = float(input("Enter Miles: "))
        except ValueError:
            print("\nInvalid input! Please enter a number.\n")
            continue
        kilometers = miles / 0.621371
        print(f"{miles} Miles = {kilometers:.2f} Kilometers\n")

    elif choice == 3:
        try:
            celsius = float(input("Enter Celsius: "))
        except ValueError:
            print("\nInvalid input! Please enter a number.\n")
            continue
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} Celsius = {fahrenheit:.2f} Fahrenheit\n")

    elif choice == 4:
        try:
            fahrenheit = float(input("Enter Fahrenheit: "))
        except ValueError:
            print("\nInvalid input! Please enter a number.\n")
            continue
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit} Fahrenheit = {celsius:.2f} Celsius\n")

    elif choice == 5:
        try:
            kilogram = float(input("Enter Kilogram: "))
        except ValueError:
            print("\nInvalid input! Please enter a number.\n")
            continue
        pounds = kilogram * 2.20462
        print(f"{kilogram} Kilogram = {pounds:.2f} Pounds\n")

    elif choice == 6:
        try:
            pounds = float(input("Enter Pounds: "))
        except ValueError:
            print("\nInvalid input! Please enter a number.\n")
            continue
        kilogram = pounds / 2.20462
        print(f"{pounds} Pounds = {kilogram:.2f} Kilogram\n")

    else:
        print("\nInvalid input!\n")

print("\nThank you for using this program.")
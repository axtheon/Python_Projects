print("\nIt's a simple calculator.")
print("Enter 0 as first number to quit!")

while True:
    try:
        num1 = float(input("\nEnter first number: "))
    except ValueError:
        print("Invalid choice! Please enter a number.")
        continue

    if num1 == 0:
        break

    operator = input("Enter operator (+,-,*,/): ")

    try:
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid choice! Please enter a number.")
        continue

    if operator == "+":
        print("\nThe answer is: ", num1 + num2)
    elif operator == "-":
        print("\nThe answer is: ", num1 - num2)
    elif operator == "*":
        print("\nThe answer is: ", num1 * num2)
    elif operator == "/":
        if num2 != 0:
            print("\nThe answer is: ", num1 / num2)
        else:
            print("\nError! Can't divide by zero.")
    else:
        print("\nInvalid choice!")

print("\nThanks for using this calculator, and BYE!")

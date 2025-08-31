# A program to find the area of these three shapes by using the values entered by the user.
while True:
    try:
        choice = int(input("1 = Triangle\n2 = Parallelogram\n3 = Rhombus\n0 = Exit\nEnter your choice: "))

        if choice == 0:
            print("Thanks for using this program!\n")
            break

        elif choice == 1:
            base = float(input("Enter base of triangle: "))
            height = float(input("Enter height of triangle: "))
            area = 0.5 * base * height
            print("The area of the triangle is:", area, "\n")

        elif choice == 2:
            base = float(input("Enter base of parallelogram: "))
            height = float(input("Enter height of parallelogram: "))
            area = base * height
            print("The area of the parallelogram is:", area, "\n")

        elif choice == 3:
            d1 = float(input("Enter first diagonal of rhombus: "))
            d2 = float(input("Enter second diagonal of rhombus: "))
            area = 0.5 * d1 * d2
            print("The area of the rhombus is:", area, "\n")

        else:
            print("Invalid choice! Please enter 0, 1, 2, or 3.\n")

    except ValueError:
        print("Invalid input! Please enter a number (0, 1, 2, or 3).\n")

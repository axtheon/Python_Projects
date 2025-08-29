from datetime import datetime

print("\nDAYS BETWEEN DATES CALCULATOR.")
print("Input format: YYYY-MM-DD (Example: 2000-01-01)\n")

while True:
    try:
        s1 = input("Enter 1st date, or 0 to exit: ")
        if s1.strip() == "0":
            break

        s2 = input("Enter 2nd date: ")

        date1 = datetime.strptime(s1.strip(), "%Y-%m-%d")
        date2 = datetime.strptime(s2.strip(), "%Y-%m-%d")

        if date1 > date2:
            date1, date2 = date2, date1

        diff = date2 - date1
        days = diff.days
        weeks = days // 7
        leftover_days = days % 7
        years_approx = days / 365.25

        print("\nDifference:")
        print(f"Days: {days}")
        print(f"Weeks and Days: {weeks} Weeks and {leftover_days} Days")
        print(f"Years Approx: {years_approx:.2f}")
    except ValueError:
        print("\nInvalid date! Please use the format YYYY-MM-DD.\n")

print("Thanks for using this program!")
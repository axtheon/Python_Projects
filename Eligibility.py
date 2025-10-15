# A program which prints the eligibility of a student for BSSE, BSCS, and BSIT
# with respect to their required percentage. The required percentage for BSSE
# is 90%, BSCS 80%, and BSIT 50%.
while True:
    print("Enter your percentage to find out,\nif you are eligible for any of these courses:\nBSSE.\nBSCS.\nBSIT")
    try:
       percentage = int(input("Enter your Percentage (Enter 0 to exit): "))
    except ValueError:
        print("\nYou entered an invalid value, please try again.\n")
        continue
    if percentage == 0:
        print("Thanks for using this program!\n")
        break
    elif percentage >= 90:
        print("You are eligible for BSSE.\n")
    elif percentage >= 80:
        print("You are eligible for BSCS.\n")
    elif percentage >= 50:
        print("You are eligible for BSIT.\n")
    else:
        print("You are not eligible for any of these courses!\n")

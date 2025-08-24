# A program which prints the eligibility of a student for BSSE, BSCS, and BSIT
# with respect to their required percentage. The required percentage for BSSE
# is 90%, BSCS 80%, and BSIT 50%.

print("Enter your percentage to find out,\nif you are eligible for any of these courses:\nBSSE.\nBSCS.\nBSIT")
percentage = int(input("Enter your Percentage: "))

if percentage >= 90:
    print("You are eligible for BSSE.")
elif percentage >= 80:
    print("You are eligible for BSCS.")
elif percentage >= 50:
    print("You are eligible for BSIT.")
else:
    print("You are not eligible for any of these courses!")
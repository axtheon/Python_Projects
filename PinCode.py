# An unlocking dialog box in python in which if the password is same as the pre-written
# password, it will print Unlocked 3 times and if it's not,
# it will give you three chances and after that you won't be able to unlock.

password = "Abdullah"
attempts = 3

while True:
    a = input("Enter the password (or 0 to exit): ")

    if a == "0":
        print("Exiting program...")
        break

    if a == password:
        print("Unlocked")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Wrong password! You have {attempts} {'try' if attempts == 1 else 'tries'} left.\n")
        else:
            print("Your device is locked for 24 hours!")
            break

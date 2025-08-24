# An unlocking dialog box in python in which if the password is same as the pre-written
# password, it will print Unlocked 3 times and if it's not,
# it will give you three chances and after that you won't be able to unlock.

password = "Abdullah"

a = input("Enter the password: ")

if a == password:
    print("Unlocked")
    exit()
else:
    print("You have only 2 tries left!")

    a = input("Enter the password: ")

if a == password:
    print("Unlocked")
    exit()
else:
    print("You have only 1 try left!")

    a = input("Enter the password: ")

if a == password:
    print("Unlocked")
else:
    print("Your device is locked for 24 hours!")

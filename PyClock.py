import time

print("""\nNote: If you are running in pycharm or any IDE like it,
It's most likely that Ctrl+c won't stop the code.
So you have to stop it manually.
It will work in CMD, Powershell or other terminals.
""")
# Function for clock.
def clock():
    print("Press Ctrl + C to stop!\n")
    try:
        while True:
            print(time.strftime("%H:%M:%S"), end=" ", flush=True)
            time.sleep(1)
            print("\r", end="", flush=True)
    except KeyboardInterrupt:
        print("\nReturning to Main Menu!\n")

# Function for stopwatch.
def stopwatch():
    print("Stopwatch started, Press Ctrl + C to quit!\n")
    start = time.time()
    try:
        while True:
            elapsed = time.time() - start
            mins, sec = divmod(int(elapsed), 60)
            ms = int((elapsed % 1) * 1000)
            print(f"{mins:02}:{sec:02}:{ms:03}", end="", flush=True)
            time.sleep(0.01)
            print("\r", end=" ", flush=True)
    except KeyboardInterrupt:
        print("\nReturning to Main Menu!\n")


# Function for timer.
def timer():
    print("Press Ctrl + C to quit!\n")
    try:
        seconds = int(input("Enter seconds: "))
    except ValueError:
        print("Invalid input. Please input seconds.\n")
        return
    try:
        while seconds > 0:
            mins, sec = divmod(seconds, 60)
            print(f"{mins:02}:{sec:02}", end="", flush=True)
            time.sleep(1)
            print("\r", end=" ", flush=True)
            seconds -= 1

        print("\nTime's Up!\n")
    except KeyboardInterrupt:
        print("\nReturning to Main Menu!\n")

# Execution.
while True:
    print("\n=== CLOCK MENU ===")
    print("1. Clock.\n2. Stopwatch.\n3. Timer.\n0. Quit.")

    try:
        choice = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please try again.")
        continue

    if choice == 0:
        print("Thanks for using this program.")
        break

    elif choice == 1:
        clock()

    elif choice == 2:
        stopwatch()

    elif choice == 3:
        timer()

    else:
        print("Invalid input. Enter one of the number assigned to options!.\n")

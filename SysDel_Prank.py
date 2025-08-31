import time
import random


def scary_loading():
    print("Initializing system wipe...", end="", flush=True)
    for i in range(5):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")


def main():
    number = random.randint(0, 10)
    attempts = 3

    print("Welcome to the Guessing Game!")
    print("You have 3 chances to guess the number between 0 and 10.")
    print("If you fail, your C drive will be deleted! \n")

    while attempts > 0:
        try:
            guess = int(input(f"Guess ({attempts} tries left): "))
        except ValueError:
            print("Invalid input. Enter a number.")
            continue

        if guess == number:
            print("🎉 Correct! You saved your PC.")
            return  # <-- stop the function

        elif guess > number:
            print("Too high!")
        else:
            print("Too low!")

        attempts -= 1

    print("\nYou failed all 3 attempts!")
    scary_loading()

    # FAKE DANGEROUS MESSAGE
    print("⚠️ WARNING: Deleting C:\\ Drive...")
    time.sleep(2)
    print("Error: ACCESS DENIED.")
    print("Gotcha! No files were harmed. This was just a prank.")


if __name__ == "__main__":
    main()

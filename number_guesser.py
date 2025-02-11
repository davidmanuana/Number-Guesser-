import random

start = input("Do you wanna play? Enter y or n: ").lower()
user_name = input("Enter your Username: ")

if start != "y":
    print("Maybe next time!")
    quit()

print(f"\nHello {user_name}, LET THE GAME BEGIN!\n")

while True:
    top_of_range = input("Type a number (greater than 0) to set the range: ")
    if top_of_range.isdigit():
        top_of_range = int(top_of_range)
        if top_of_range > 0:
            break
        else:
            print("Please enter a number larger than 0.")
    else:
        print("Please enter a valid number.")

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    user_guess = input("Make a guess: ")
    
    if not user_guess.isdigit():
        print("Please enter a valid number.")
        continue

    user_guess = int(user_guess)
    guesses += 1

    if user_guess == random_number:
        print(f"🎉 Congratulations {user_name}, you guessed the number in {guesses} tries! 🎉")
        break
    elif user_guess > random_number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")

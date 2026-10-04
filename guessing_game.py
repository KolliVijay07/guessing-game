import random

number = random.randint(1, 10)
player_name = input("Hey player! What's your name: ")

print("Okay", player_name, "! Let's begin our game")

level = input("Choose the level (Easy/Medium/Hard): ").upper()

# Set number of attempts based on level
attempts = {
    "EASY": 7,
    "MEDIUM": 5,
    "HARD": 3
}

if level in attempts:
    max_attempts = attempts[level]

    print(f"You have selected {level} level - so guess the number in {max_attempts} attempts")
    print("I'm going to choose a number between 1 and 10")

    number_of_guesses = 0

    while number_of_guesses < max_attempts:
        guess = int(input("Enter your guess: "))
        number_of_guesses += 1

        if guess < number:
            print("Your guess is too low")
        elif guess > number:
            print("Your guess is too high")
        else:
            print(f"You guessed the number in {number_of_guesses} tries!")
            break

    else:
        print(f"You could not guess the number.")
        print(f"The number was {number}")

else:
    print("Invalid level! Please choose Easy, Medium, or Hard.")
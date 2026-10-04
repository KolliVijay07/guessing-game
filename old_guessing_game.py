import random
number=random.randint(1,10)
number_of_guesses=0
player_name=input("Hey player!What's your name:")
print("okay",player_name,"!Let's begin our game")
level=input("Choose the level(Easy/Medium/Hard):")
if level.upper()=='EASY':
    print("You have selected EASY level-so guess the number in 7 attempts")
    print("I'm going to guess a number between 1 and 10")
    while number_of_guesses<7:
        guess=int(input())
        number_of_guesses+=1
        if guess < number:
            print("Your guess is too low")
        elif guess  > number:
            print("Your guess is too high")
        elif guess == number:
            break
    if guess == number:
        print("You guessed the number in",str(number_of_guesses),"tries!")
    else:
        print("You could not guess the number\nThe number was",str(number))
elif level.upper()=='MEDIUM':
    print("You have selected MEDIUM level-so guess the number in 5 attempts")
    print("I'm going to guess a number between 1 and 10")
    while number_of_guesses<5:
        guess=int(input())
        number_of_guesses+=1
        if guess < number:
            print("Your guess is too low")
        elif guess  > number:
            print("Your guess is too high")
        elif guess == number:
            break
    if guess == number:
        print("You guessed the number in",str(number_of_guesses),"tries!")
    else:
        print("You could not guess the number\nThe number was",str(number))
else:
    print("You have selected HARD level-so guess the number in 3 attempts")
    print("I'm going to guess a number between 1 and 10")
    while number_of_guesses<3:
        guess=int(input())
        number_of_guesses+=1
        if guess < number:
            print("Your guess is too low")
        elif guess  > number:
            print("Your guess is too high")
        elif guess == number:
            break
    if guess == number:
        print("You guessed the number in",str(number_of_guesses),"tries!")
    else:
        print("You could not guess the number\nThe number was",str(number))
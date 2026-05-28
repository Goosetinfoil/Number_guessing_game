import random

top_of_range = input("Type a number: ")
guesses = 0

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0: 
        print("Please print a number larger than 0")
        quit()
else:
    print("Choose a number next time")
    quit()

number = random.randint(0, top_of_range)

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number")
        continue
    
    if user_guess == number:
        print("You got it!")
        break
    elif user_guess > number:
        print("Your guess is greater than the number")
    else:
        print("Your guess is smaller than the number")

print("You got it in", guesses, "guesses")
number = 10
max_guesses = 3
remaining_guesses = max_guesses

print("I'm thinking of a number...")

while remaining_guesses > 0:
    guess = input(f"What number am I thinking of? You have {remaining_guesses} guesses left. (Enter 'q' to quit): ")
    
    if guess == 'q':
        print(f"The number was {number}.")
        break
    
    guess = int(guess)

    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    
    remaining_guesses -= 1

if remaining_guesses == 0:
    print(f"Sorry, you've run out of guesses. The number was {number}.")
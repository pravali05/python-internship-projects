
import random

# Generate a random number
secret_number = random.randint(1, 100)

attempts = 0
score = 100

print("Welcome to Number Guessing Game!")
print("Guess a number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret_number:
        print("Congratulations! Correct guess!")
        break

    elif guess < secret_number:
        print("Too Low! Try Again.")

    else:
        print("Too High! Try Again.")

    score = max(0, score - 10)

print("You guessed the number!")
print("Attempts:", attempts)
print("Final Score:", score)

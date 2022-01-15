
import random

number_secret = random.randrange(1, 10)
print(number_secret)
while True:
    number_guess = int(input("Type a guess number between 1 and 10:\n"))
    if number_guess > number_secret:
        print("Too much!")
        number_guess = int(input("Type a guess number between 1 and 10:\n"))
    elif number_guess < number_secret:
        print("Not enough!")
        number_guess = int(input("Type a guess number between 1 and 10:\n"))
    elif number_guess == number_secret:
        print("Congratulations! You guessed right number!")
        break


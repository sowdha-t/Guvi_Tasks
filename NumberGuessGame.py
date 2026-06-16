#Number Guess Game

import random

start_range = 1
end_range =100
max_attempt = 10
attempts = 0

#Generating random number using random module which gives us in between range 1 to 100
secret_number = random.randint(start_range, end_range)
#for testing purpose
#print(secret_number)
print("Welcome to the Number Guess Game")
print(f"Guess the secret number between {start_range} and {end_range} in {max_attempt} attempts")
while True and attempts <= max_attempt:

    try:
        user_guess = int(input("Guess the secret number: "))

        if user_guess < start_range or user_guess > end_range:
            attempts += 1
            print(f"Please enter a number between {start_range} and {end_range}" )
            continue
        elif user_guess > secret_number:
            attempts += 1
            print("Your guess is too high")
        elif user_guess < secret_number:
            attempts += 1
            print("Your guess is too low")
        elif user_guess == secret_number:
            attempts += 1
            print(f"hurrah....You guessed the number correctly in {attempts} attempts")
            break
        else:
            continue

    except ValueError:
        attempts += 1
        print(f"Please enter a number between {start_range} and {end_range}")
        continue
else:
    print(f"You have reached the maximum attempts allowed and the secret number is {secret_number}")



"""
Problem Statement 04 : Write a program to find the sum of the first and last digit of an integer
"""

#Getting a valid input from the user
try:
    input_number = int(input("Enter a number: "))
    input_number = abs(input_number)                #Converting to positive integer if user enters negative integer
    # This statement retrieves the last digit of the given number
    last_digit = input_number % 10

    # This statement retrieves the first digit of the given number
    while input_number >= 10:
        input_number = input_number // 10

    first_digit = input_number
    sum_digits = first_digit + last_digit           #adding both first_digit and last_digit

    print(f"Sum of first digit: {first_digit} and last digit: {last_digit} =", sum_digits)
except ValueError:                                  #If user enters a string or any other types
    print("Invalid input")







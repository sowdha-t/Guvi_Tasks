"""
Problem Statement: 01 You have been given a Python list [10,501,22,37,100,999,87,351]
Your task is to create two list one which have all the even numbers and another list which
will have all the odd numbers.

"""

given_list = [10,50,22,37,100,999,87,351]

even_list = []
odd_list = []

for num in given_list:
    if num % 2 == 0:                    #If it's divided by 2, it is added to even list
        even_list.append(num)
    else:
        odd_list.append(num)
print(f"The even numbers are: {even_list}")
print(f"The odd numbers are: {odd_list}")
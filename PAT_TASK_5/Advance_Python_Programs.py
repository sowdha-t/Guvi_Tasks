
print("""
Problem Statement :01 
Given a list of dictionaries, each representing a person with 'name' and 'age' keys,
use lambda functions to filter out people under 18 and then map the remaining peoples name to a new list.

""")

student_age_details = [
    {"name":"renu", "age":15},
    { "name":"ramya", "age":19},
    { "name":"devi", "age":20},
    { "name":"poorani", "age":21},
    { "name":"gomathi", "age":14},
    { "name":"janani", "age":18},
    { "name":"jemi", "age":24},
    {"name":"kalai", "age":12},
    { "name":"kavi", "age":10},
    { "name":"mahi", "age":17}
]

student_under_18 = list(map(
    lambda student: student["name"],             #mapping only those names to a list
    filter(
        lambda student: student["age"] < 18,     #Filtering out people who are under 18 and passing to map object
        student_age_details
    )
    )
)

#Using List comprehension
student_under_18_listcompre = [student["name"] for student in student_age_details if student["age"] < 18]

print(f"Students who are under 18(Using lambda map and filter: {student_under_18}")
print(f"Students who are under 18(Using list comprehension: {student_under_18_listcompre}")

print("#####"*20)
print(
"""
Problem Statement : 02
Given a list of numbers , use the reduce function and a lambda expression to calculate product of all the 
numbers in the list
"""
)

numbers = [3,5,3,1]

from functools import reduce            #importing reduce function from functool
product_of_numbers = reduce(lambda x,y: x*y, numbers)
print(f"Product of numbers in the number list: {product_of_numbers}")

print("#####"*20)
print("""
Problem Statement : 03 
Write a list comprehension that creates a new list of squares of even numbers from a given list,
using a lambda function to check for even numbers
"""
      )
numbers = [3,6,4,1,3,2]

sq_numbers_using_map_filter = list(
    map(
        lambda x : x**2,
            filter(lambda x : x % 2 == 0, numbers)
        )
    )

sq_numbers_using_list_comprehension = [num ** 2 for num in numbers if num % 2 == 0]

print(f"List of sq_numbers from even number list(using map and filter): {sq_numbers_using_map_filter}")
print(f"List of sq_numbers from even number list(using list comprehension): {sq_numbers_using_list_comprehension}")

print("#####"*20)
print(
"""
Problem Statement : 04
Write a lambda function to check if a given string is number. 
"""
)
given_string = input("Enter a string(We will print True if the string entered is number): ")
#given_string = "12"
str_check = lambda x : x.strip().isdigit()
print("Check if the given string is number :",str_check(given_string))

print("#####"*20)
print(
"""
Problem Statement : 05
Use a lambda function to extract the year, month and date from a datetime object
"""
)
from datetime import datetime

extracted_date = lambda dt : {"year" :dt.year, "month" : dt.month ,"date" : dt.day}
given_date = datetime.today()
print(extracted_date(given_date))


print("#####"*20)
print(
"""
Problem Statement : 06
Create a lambda function to generate a fibonacci series upto n terms.
"""
)

count = 0
first_term = 0
second_term = 1
fibonacci_series = [first_term, second_term]
input_check = True
while input_check:
    try:
        nth_term = int(input("Enter nth term to calculate fibonacci series: "))
        if nth_term < 0:
            input_check = True
            print("Please enter a positive numeric value")
            continue
        input_check = False
        sum = lambda x, y: x + y
        while count < nth_term - 2:
            total = sum(first_term, second_term)
            fibonacci_series.append(total)
            first_term = second_term
            second_term = total
            count = count + 1


    except ValueError:
        print("Please enter a numeric value")
        continue

print(fibonacci_series)

print("#####"*20)

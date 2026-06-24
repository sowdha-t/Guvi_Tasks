"""Problem Statement : 4
Given the Python List [10,501,22,37,100,999,87,351]
Find out how many numbers are there in the given Python List which are Happy Numbers
A happy number is a positive integer that eventually reaches 1
when you repeatedly replace the number with the sum of the squares of its digits"""

given_list = [10,501,22,37,100,999,87,351]
happy_number_list = []

#This function performs the addition of the given number. It returns the total of square of individual digit
def check_sum(num):
    total = 0
    while num > 0:
        rem = num % 10
        total = total + rem ** 2
        num = num // 10
    return total

'''This function performs the check for happy number by getting the total sum of the each squared digit
and calling itself recursively till the resultant sum is not 1 or it repeats itself '''
def check_happy_num(num, duplicate_check=None):
    if duplicate_check is None:
        duplicate_check = set()

    total = check_sum(num)
    #print(total)

    if total == 1:
        return True
    elif total in duplicate_check:              #This check is performed to see whether the happy number list already contains the same number
        return False

    duplicate_check.add(total)

    return check_happy_num(total, duplicate_check)

#This loop is to check for each number in the given list a happy number or not
for num in given_list:
    if check_happy_num(num):
        happy_number_list.append(num)


if len(happy_number_list) != 0:
    print(happy_number_list)
    print("Number of happy numbers:", len(happy_number_list))
else:
    print("No happy numbers in the given list")



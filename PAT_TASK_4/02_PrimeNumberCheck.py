"""
Problem Statement: 02
Given the Python List [10,501,22,37,100,999,87,351] your task is to count all the
prime numbers and create a new python list which will contain all the prime numbers in it
"""

def check_prime(num):
    if num <= 1:                    #if a number is 1, it is not a prime
        return False
    elif num <= 3:                  #If a number 2 or 3, it is not a prime
        return True
    else:
        for i in range(4, num):
            if num % i == 0:        #If the number is divided by the given num, then it is not a prime
                return False
        else:
            return True

#checking for prime number from the list
given_list = [10,50,22,37,100,999,87,351]
prime_list = []
for num in given_list:
    #print(num)
    if check_prime(num):                    #If the function returns true, it is added to prime number list
        prime_list.append(num)


if not prime_list:
    print("No prime numbers found in the list")
else:
    print(f"The prime numbers found in the list:{prime_list} ")
    print(f"prime numbers count from the list:{len(prime_list)}")
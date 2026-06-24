"""
Problem Statement: 09
You have given a python list  [10,20,30,9] and a value of 59. Write a Python program
to find the triplet in the list whose sum is equal to the given value
"""

given_list = [10,20,30,9]
length = len(given_list)
triplets = []
given_value = 59

for i in range(0,length):
    for j in range(i+1,length):                 #checking second element
        for k in range(j+1,length):             #checking third element
            if given_list[i] + given_list[j] + given_list[k] == given_value:            #Checking if the value sums up to given value
                sub_list = [given_list[i],given_list[j],given_list[k]]                  #If so, add it in a list
                triplets.append(sub_list)

if len(triplets) == 0:
    print("There is no triplet in the list")
else:
    print(f"There is a triplets with sum equal to {given_value} :{triplets} and its count is {len(triplets)}")
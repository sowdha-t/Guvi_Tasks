"""
Problem Statement: 10
Given a list  [4,2,-3,1,6] write a program to find if there is a sub-list with sum equal to zero
"""

given_list = [4,2,-3,1,6]
length = len(given_list)
all_sublists = []

for i in range(0,length):
    for j in range(i+1,length):
        for k in range(j+1,length):
            if given_list[i] + given_list[j] + given_list[k] == 0:
                sub_list = [given_list[i],given_list[j],given_list[k]]
                all_sublists.append(sub_list)


if len(all_sublists) == 0:
    print("There is no sub-list")
else:
    print(f"There is a sub-list with sum equal to zero :{all_sublists} and its count is {len(all_sublists)}")

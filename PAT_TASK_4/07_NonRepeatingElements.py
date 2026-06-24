"""
Problem Statement: 07
Write a Python program to find the first non-repeating elements in a
given list of integers.
"""

given_list = [5,5,3,5,7,8]

print("#"*20,"Using dictionary Method","#"*20)
non_repeating_item = dict()

for num in given_list:
    if num in non_repeating_item:
        non_repeating_item[num] += 1
    else:
        non_repeating_item[num] = 1


for item in given_list:
    if non_repeating_item[item] == 1:
        print(f"First Non-Repeating Number: {item}")
        break
else:
    print(f"No Non-Repeating Number")

print("#"*20,"Using List Method","#"*20)

'''Using List method'''
for item in given_list:
    if given_list.count(item) == 1:
        print(f"First Non-Repeating Number: {item}")
        break
else:
    print(f"No Non-Repeating Number")





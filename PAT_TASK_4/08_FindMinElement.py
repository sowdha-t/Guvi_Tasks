"""
Problem Statement: Write a program to find the minimum element in a sorted and rotated list?

"""

list_example = [3,6,7,9,0,1,-5]

#List sorted
list_example.sort()
print(list_example)

#list rotated
list_example.reverse()
print(list_example)

#finding the minimum element in the list
print(f"Minimum element in the list:{min(list_example)}")
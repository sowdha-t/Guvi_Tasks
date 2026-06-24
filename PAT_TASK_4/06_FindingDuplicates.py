"""
Problem Statement: 06
You have given three lists. You have to find the duplicates in the three lists. Write a program
for the same. You can use your own lists

"""
#This function checks each item in the list present in other two list and add the common item in all list
#to the duplicate list and returns the duplicate list
def find_duplicates(list1,list2,list3):
    duplicate_num_list = []
    for num in list1:
        if num in list2 and num in list3 and num not in duplicate_num_list:
            duplicate_num_list.append(num)
    return duplicate_num_list

list1 = [1,2,2,6,6,6,7,7,73,4,5]
list2 = [6,7,8]
list3=[5,6,7,8,9,10]

list4 = ["apple", "banana", "cherry","mango"]
list5 = ["kiwi","watermelon","mango"]
list6=["mango","mango","kiwi"]

print(f"Duplicates in the three number list:{find_duplicates(list1,list2,list3)}")
print(f"Duplicates in the three fruit list:{find_duplicates(list4,list5,list6)}")



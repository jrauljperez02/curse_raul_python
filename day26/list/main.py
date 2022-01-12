#lets work with file 1
with open('list/file1.txt') as list1:
    list1 = list1.readlines()

list_file1 = [int(num) for num in list1]

#lets work with file 2
with open('list/file2.txt') as list2:
    list2 = list2.readlines()

list_file2 = [int(num) for num in list2]


#lets comprobate if numbers are the same
final_list = [num for num in list_file1 if num in list_file2]

print(final_list)
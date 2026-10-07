# Copyright (c) 2026 Abdelrhman Taha
# All Rights Reserved.
#
# This material is part of the Python-for-Data-Science course.
# Unauthorized reproduction, redistribution, or commercial use is prohibited.

#---------------------------------
#-------Lists Methods part 2------
#---------------------------------

# 1. Clear()
my_list = [1, 2, 3, 4, 5]
my_list.clear()
print(my_list)  # Output: []











# 2. Copy()
my_list = [1, 2, 3, 4, 5]
new_list = my_list.copy()
print(my_list) # Output: [1, 2, 3, 4, 5]
print(new_list)  # Output: [1, 2, 3, 4, 5]

my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
print(new_list)  # Output: [1, 2, 3, 4, 5]






# 3. Count()
my_list = [1, 2, 3, 4, 5, 5, 5]
print(my_list.count(5))  # Output: 3



# 4. Index()
my_list = [1, 2, 3, 4, 5]
print(my_list.index(3))  # Output: 2
# print(my_list.index(6))  # Output: ValueError: 6 is not in list


# 5. Insert()
my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 10)
print(my_list)  # Output: [1, 2, 10, 3, 4, 5]
my_list.insert(-1,20)
print(my_list)  # Output: [1, 2, 10, 3, 4, 20, 5]



# 6. Pop()
my_list = [1, 2, 3, 4, 5]
print(my_list.pop())  # Output: 5
print(my_list)  # Output: [1, 2, 3, 4]
print(my_list.pop(1))  # Output: 2
print(my_list)  # Output: [1, 3, 4]
print(my_list.pop(-1))  # Output: 4
print(my_list)  # Output: [1, 3]
print(my_list.pop()) # Output: 3
print(my_list)  # Output: [1]



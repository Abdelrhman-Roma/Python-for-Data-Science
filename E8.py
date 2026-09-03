# Copyright (c) 2026 Abdelrhman Taha
# All Rights Reserved.
#
# This material is part of the Python-for-Data-Science course.
# Unauthorized reproduction, redistribution, or commercial use is prohibited.

#Problem 1 — Personal Information
name = "   abdelrhman taha   "
age = 20
city = "cairo"
gpa = 3.756
#Write a program that:
#1. Removes the extra spaces from name.
#2. Converts the name to title case.
#3. Converts city to uppercase.
#4. Prints all information using an f-string.

#5. Prints the GPA with exactly 2 decimal places.
#==================================================================
# Answer:
name = name.strip()
name = name.title()
city = city.upper()
# print(f"my name is : {name} and my city is {city} and my gpa is {gpa:.2f}")

#=============================================================
#Problem 2 — String Challenge
text = "  I Love Python And Python Loves Me  "
#Write a program that:
#1. Removes the extra spaces.
#2. Converts the text to lowercase.
#3. Counts how many times "python" appears.
#4. Checks if the text starts with "i".
#5. Checks if the text ends with "me".
#6. Replaces "python" with "programming".
#7. Prints the final text.
#===================================================
#Answer:
# text = text.strip()
# text = text.lower()
# print(text.count("python"))
# print(text.startswith("i"))
# print(text.endswith("me"))
# text = text.replace("python","programming")
# print(text)


#=======================================================
#Problem 3 — Indexing, Slicing & Formatting
course = "Python Programming"
name = "Abdelrhman"
age = 20
#Write a program that:
#1. Prints the first character of course.
#2. Prints the last character of course.
#3. Prints "Python" using slicing.
#4. Prints "Programming" using slicing.
#5. Prints every second character of course.
#6. Prints the length of course.
#7. Prints the student's information using an f-string.
#===================================================================
#Answer:
# print(course[0])
# print(course[-1])
# print(course[0:6])
# print(course[7:])
# print(course[::2])
# print(len(course))
# print(f"my name is {name} and i study {course} and my age is {age}")

#==========================================================
#Problem 4 — Username & Message
username = "Python_Developer_2026"
message = "   I love Python and Python is easy   "
# Write a program that:
# 1. Removes the extra spaces from message.
# 2. Converts username to lowercase.
# 3. Converts message to title case.
# 4. Prints the first character of username.
# 5. Prints the last character of username.
# 6. Counts how many times "Python" appears in message.
# 7. Replaces "Python" with "Programming".
# 8. Checks whether username is a valid identifier.
# 9. Creates a new string containing:
# username - message
# using join().
# 10. Prints the final result using an f-string.
# Bonus: Print the length of username and the length of message.
#==================================================================
#Answer:
# message = message.strip()
# username = username.lower()
# message = message.title()
# print(username[0])
# print(username[-1])
# print(message.count("python"))
# print(message.replace("Python","Programming"))
# print(username.isidentifier())
# print('-'.join([username,message]))
# print(f"{username} and {message}")
# print(f"length username {len(username)}")
# print(f"length message {len(message)}")




#==========================================================
#Problem 5 — Shopping Bill Challenge
item = "  python book  "
price = 250
quantity = 3
discount = 50
# Write a program that:
# 1. Removes the extra spaces from item.
# 2. Converts item to title case.
# 3. Calculates the total price:
# 4. Calculates the final price after the discount:
# 5. Calculates the average price per item:
# 6. Prints the item name.
# 7. Prints the total price.
# 8. Prints the discount.
# 9. Prints the final price.
# 10. Prints the average price with 2 decimal places using an f-string.
#=================================================================================
#Answer:
# item = item.strip().title()
# total_price = price * quantity
# after_discount = total_price - discount
# average = total_price / quantity
# print(name)
# print(total_price)
# print(discount)
# print(after_discount)
# print(f"{average:.2f}")

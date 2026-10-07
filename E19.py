#=================================================================#
#====================== Small Exercise ===========================#
#=================================================================#


#---------------------------------------------------------------#
# Part 1: Type Conversion
#---------------------------------------------------------------#

# 1. أنشئ String يحتوي على:
# "12345"
test = "12345"
# ثم حوّله إلى:
# int
#
# واطبع القيمة والـ type.
test = int(test)
print(test)
print(type(test))


# 2. أنشئ String يحتوي على:
# "25.5"
test_float = "25.5"
# ثم حوّله إلى:
# float
#
# واطبع القيمة والـ type.

test_float = float(test_float)
print(test_float)
print(type(test_float))

# 3. أنشئ String:
# "Python"
test_str = "Python"
# حوّله إلى:
# tuple
# ثم اطبع النتيجة.
test_str_tuple = tuple(test_str)
print(test_str_tuple)
print(type(test_str_tuple))

# 4. أنشئ List:
# [1, 2, 3, 4, 5]
test_list = [1, 2, 3, 4, 5]
# حوّلها إلى:
# tuple
# ثم اطبع النتيجة.
test_list_tuple = tuple(test_list)
print(test_list_tuple)
print(type(test_list_tuple))


# 5. أنشئ Tuple:
# ("Python", "C++", "Java")
test_tuple = ("Python", "C++", "Java")
# حوّلها إلى:
# list
# ثم اطبع النتيجة.
test_tuple_list = list(test_tuple)
print(test_tuple_list)
print(type(test_tuple_list))

# 6. أنشئ List:
# ["Python", "Python", "C++", "Java", "C++"]
test_list = ["Python", "Python", "C++", "Java", "C++"]
# حوّلها إلى:
# set
# ثم اطبع النتيجة.
test_list_set = set(test_list)
print(test_list_set)
print(type(test_list_set))
# 7. أنشئ List تحتوي على:
# [("name", "Ahmed"), ("age", 20)]
test_list_of_tuples = [("name", "Ahmed"), ("age", 20)]
# حوّلها إلى Dictionary
# باستخدام dict()

# ثم اطبع النتيجة.
test_dict = dict(test_list_of_tuples)
print(test_dict)
print(type(test_dict))

#---------------------------------------------------------------#
# Part 2: User Input
#---------------------------------------------------------------#

# 8. اطلب من المستخدم إدخال اسمه
# ثم اطبع:
name = input("Enter your name: ")
# Hello Ahmed
#
# باستخدام f-string.
print(f"Hello {name}")

# 9. اطلب من المستخدم إدخال عمره.
#
# حوّل القيمة إلى int
# ثم اطبع عمره بعد سنة واحدة.
age = int(input("Enter your age: "))
print(f"Your age after one year will be: {age + 1}")

# 10. اطلب من المستخدم إدخال طوله بالمتر.
#
# حوّل القيمة إلى float
# ثم اطبع الطول.
height = float(input("Enter your height in meters: "))
print(f"Your height is: {height} meters")

# 11. اطلب من المستخدم إدخال رقمين.
#
# حوّل الرقمين إلى int
# ثم اطبع:
#
# الجمع
# الطرح
# الضرب
# القسمة
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print(f"Sum: {x + y}")
print(f"Difference: {x - y}")
print(f"Product: {x * y}")
print(f"Division: {x / y}")

#---------------------------------------------------------------#
# Part 3: Mini Challenge
#---------------------------------------------------------------#

# اطلب من المستخدم إدخال البيانات التالية:
#
# Name
# Age
# Height
# Favorite Number
#
# ثم اطبع البيانات في شكل منظم باستخدام f-string.
#
# مثال:
#
# Name: Ahmed
# Age: 20
# Height: 1.75
# Favorite Number: 7
#
# ثم احسب عمر المستخدم بعد 5 سنوات واطبعه.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
favorite_number = int(input("Enter your favorite number: "))

print(f"Name: {name}")
print(f"Age: {age + 5}")
print(f"Height: {height}")
print(f"Favorite Number: {favorite_number}")


#---------------------------------------------------------------#
# Bonus Challenge
#---------------------------------------------------------------#

# اطلب من المستخدم إدخال:
#
# First Number
# Second Number
#
# ثم احسب متوسط الرقمين.
#
# تذكر أن input() ترجع String،
# لذلك يجب استخدام Type Conversion المناسبة.
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
print(f"The average of {x} and {y} is: {(x + y) / 2}")



#-----------------------------------
#---------Control Flow--------------------------
#-----------------------------------

# If , Elif , Else

# syntax:
# if condition:
#     # code to execute if condition is True    
# elif another_condition:
#     # code to execute if another_condition is True
# else:
#     # code to execute if all conditions are False


# if statement









# elif statement









# else statement



# nested













# Ternary Operator
# Syntax:
# value_if_true if condition else value_if_false









#-----------------------------------#
#--------- Small Exercise ----------#
#-----------------------------------#


#===========================================================#
# Part 1: if Statement
#===========================================================#

# 1. أنشئ متغيرًا باسم age وضع فيه عمرًا.
#
# إذا كان العمر أكبر من أو يساوي 18:
# اطبع:
# "You are an adult"


#===========================================================#
# Part 2: if / else
#===========================================================#

# 2. اطلب من المستخدم إدخال رقم.
#
# إذا كان الرقم أكبر من 0:
# اطبع:
# "Positive"
#
# وإلا:
# اطبع:
# "Not Positive"


#===========================================================#
# Part 3: if / elif / else
#===========================================================#

# 3. اطلب من المستخدم إدخال درجة الطالب.
#
# إذا كانت الدرجة أكبر من أو تساوي 90:
# اطبع "Excellent"
#
# إذا كانت الدرجة أكبر من أو تساوي 80:
# اطبع "Very Good"
#
# إذا كانت الدرجة أكبر من أو تساوي 60:
# اطبع "Pass"
#
# غير ذلك:
# اطبع "Fail"


#===========================================================#
# Part 4: Multiple Conditions
#===========================================================#

# 4. اطلب من المستخدم إدخال عمره.
#
# إذا كان العمر أقل من 13:
# اطبع "Child"
#
# إذا كان العمر من 13 إلى 17:
# اطبع "Teenager"
#
# إذا كان العمر من 18 إلى 59:
# اطبع "Adult"
#
# إذا كان العمر 60 أو أكثر:
# اطبع "Senior"


#===========================================================#
# Part 5: Nested if
#===========================================================#

# 5. اطلب من المستخدم إدخال:
#
# username
# password
#
# إذا كان username صحيحًا:
#     تحقق من password
#
# إذا كان username و password صحيحين:
# اطبع:
# "Login Successful"
#
# إذا كان username صحيحًا ولكن password خطأ:
# اطبع:
# "Wrong Password"
#
# وإذا كان username خطأ:
# اطبع:
# "Wrong Username"


#===========================================================#
# Part 6: Ternary Operator
#===========================================================#

# 6. أنشئ متغيرًا باسم number.
#
# باستخدام Ternary Operator فقط،
# تحقق هل الرقم Even أم Odd.
#
# مثال:
#
# number = 10
#
# الناتج:
# Even


#===========================================================#
# Part 7: Mini Challenge
#===========================================================#

# 7. أنشئ برنامجًا بسيطًا لتحديد حالة الطالب.
#
# اطلب من المستخدم إدخال:
#
# name
# age
# score
#
# ثم:
#
# إذا كان العمر أقل من 18:
#     اطبع أن الطالب يحتاج إلى موافقة ولي الأمر.
#
# وإذا كان العمر 18 أو أكثر:
#     تحقق من الدرجة:
#
#     90 أو أكثر  -> "Excellent"
#     80 أو أكثر  -> "Very Good"
#     60 أو أكثر  -> "Pass"
#     أقل من 60   -> "Fail"
#
# في النهاية اطبع اسم الطالب وحالته.


#===========================================================#
# Bonus Challenge
#===========================================================#

# 8. اطلب من المستخدم إدخال ثلاثة أرقام:
#
# num1
# num2
# num3
#
# باستخدام if / elif / else،
# أوجد أكبر رقم بينهم.
#
# ثم استخدم Ternary Operator للتحقق
# هل أكبر رقم Even أم Odd.
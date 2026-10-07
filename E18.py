# Copyright (c) 2026 Abdelrhman Taha
# All Rights Reserved.
#
# This material is part of the Python-for-Data-Science course.
# Unauthorized reproduction, redistribution, or commercial use is prohibited.


#============================================================#
#-------------------- Small Exercise ------------------------#
#============================================================#


# لدينا عدد يمثل رصيد حساب بنكي

balance = 1000


# 1. أضف 500 إلى الرصيد باستخدام +=
balance += 500

# 2. اطرح 200 من الرصيد باستخدام -=
balance -= 200

# 3. اضرب الرصيد في 2 باستخدام *=
balance *= 2

# 4. استخدم %= 500 لإيجاد باقي قسمة الرصيد على 500
balance %= 500

# 5. أنشئ متغيرًا باسم number بقيمة 5
number = 5
# واستخدم **= لرفع الرقم للقوة 3
number **= 3


# 6. أنشئ متغيرًا باسم total بقيمة 25
total = 25
# واستخدم //= 4 لإجراء القسمة الصحيحة
total //= 4

#============================================================#
#---------------- Comparison Operations ---------------------#
#============================================================#

# لدينا درجات طالبين

student1_score = 85
student2_score = 70


# 7. تحقق هل درجة الطالب الأول تساوي درجة الطالب الثاني
# باستخدام ==
print(student1_score == student2_score)

# 8. تحقق هل درجة الطالب الأول لا تساوي درجة الطالب الثاني
# باستخدام !=
print(student1_score != student2_score)

# 9. تحقق هل درجة الطالب الأول أكبر من درجة الطالب الثاني
# باستخدام >
print(student1_score > student2_score)

# 10. تحقق هل درجة الطالب الثاني أقل من درجة الطالب الأول
# باستخدام <
print(student1_score < student2_score)

# 11. تحقق هل درجة الطالب الأول أكبر من أو تساوي 90
# باستخدام >=
print(student1_score >= student2_score)


# 12. تحقق هل درجة الطالب الثاني أقل من أو تساوي 70
# باستخدام <=
print(student1_score <= student2_score)


#============================================================#
#------------------------ Bonus -----------------------------#
#============================================================#

# لديك متغير يمثل سعر منتج

price = 1000

# أضف 200 إلى السعر
# ثم اطرح 100
# ثم اضرب السعر في 2
price += 200
price -= 100
price *= 2

# بعد ذلك تحقق:
#
# هل السعر النهائي أكبر من 2000؟
print(price > 2000)
# هل السعر النهائي يساوي 2200؟
print (price == 2200)
# هل السعر النهائي أقل من أو يساوي 2200؟
print(price <= 2200)
#
# استخدم Comparison Operators المناسبة.



print("="*100)
#================================================================================
#========================= Type Converstion and User Input ======================
#================================================================================

# Conversion


# str()
# print(type(str(x)))


# tuple()
a = "python" #String
b = [1,2,3,4] # list
c = {"A" , "B" , "C"} # set
d = {"code1" : 1 , "code2" : 2} #dictionary

print(tuple(a))
print(tuple(b))
print(tuple(c))
print(tuple(d))
print("-"*50)






# list()
a = "python" #String
b = (1,2,3,4) # tuple
c = {"A" , "B" , "C"} # set
d = {"code1" : 1 , "code2" : 2} #dictionary


print(list(a))
print(list(b))
print(list(c))
print(list(d))
print('-'*50)







# set()
a = "python" #String
b = (1,2,3,4) # tuple
c = ["A" , "B" , "C"] # list
d = {"code1" : 1 , "code2" : 2} #dictionary

print(set(a))
print(set(b))
print(set(c))
print(set(d))
print('-'*50)








# dict()
a = "python" #String
b = (("one",1),("two",2),("three",3)) # tuple
c = [["A",1] , ["B",2] , ["C",3]] # list
d = {"code1",1,"code2",2} # set

# print(dict(a))
print(dict(b))
print(dict(c))
# print(dict(d))
print("-"*50)


# User Input

# input()

# # What is input()?

# The input() function is used to take data from the user while the program
# is running.

# Example:

# name = input("enter your name: ")

# print(f"Hello {name}")


# One of the most important things to remember:

# input() always returns a string (str).

# Example:

# age = input("Enter your age: ")

# print(type(age))

# Example:

# age = int(input("Enter your age: "))

# print(age + 1)


# print(type(age))



# Example:

name = input("Enter your name: ").strip().capitalize()
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

print(f'Hello {name}')
print(age)
print(height)

# Example:
num1 = int(input("Enter Your First Number: "))
num2 = int(input("Enter Your Second Number: "))
print(num1 + num2)








#=================================================================#
#====================== Small Exercise ===========================#
#=================================================================#


#---------------------------------------------------------------#
# Part 1: Type Conversion
#---------------------------------------------------------------#

# 1. أنشئ String يحتوي على:
# "12345"
#
# ثم حوّله إلى:
# int
#
# واطبع القيمة والـ type.


# 2. أنشئ String يحتوي على:
# "25.5"
#
# ثم حوّله إلى:
# float
#
# واطبع القيمة والـ type.


# 3. أنشئ String:
# "Python"
#
# حوّله إلى:
# tuple
# ثم اطبع النتيجة.


# 4. أنشئ List:
# [1, 2, 3, 4, 5]
#
# حوّلها إلى:
# tuple
# ثم اطبع النتيجة.


# 5. أنشئ Tuple:
# ("Python", "C++", "Java")
#
# حوّلها إلى:
# list
# ثم اطبع النتيجة.


# 6. أنشئ List:
# ["Python", "Python", "C++", "Java", "C++"]
#
# حوّلها إلى:
# set
# ثم اطبع النتيجة.


# 7. أنشئ List تحتوي على:
# [("name", "Ahmed"), ("age", 20)]
#
# حوّلها إلى Dictionary
# باستخدام dict()
#
# ثم اطبع النتيجة.


#---------------------------------------------------------------#
# Part 2: User Input
#---------------------------------------------------------------#

# 8. اطلب من المستخدم إدخال اسمه
# ثم اطبع:
#
# Hello Ahmed
#
# باستخدام f-string.


# 9. اطلب من المستخدم إدخال عمره.
#
# حوّل القيمة إلى int
# ثم اطبع عمره بعد سنة واحدة.


# 10. اطلب من المستخدم إدخال طوله بالمتر.
#
# حوّل القيمة إلى float
# ثم اطبع الطول.


# 11. اطلب من المستخدم إدخال رقمين.
#
# حوّل الرقمين إلى int
# ثم اطبع:
#
# الجمع
# الطرح
# الضرب
# القسمة


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
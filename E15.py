# Copyright (c) 2026 Abdelrhman Taha
# All Rights Reserved.
#
# This material is part of the Python-for-Data-Science course.
# Unauthorized reproduction, redistribution, or commercial use is prohibited.


#----------------------------------#
#----- Small Exercise -------------#
#----------------------------------#

# لدينا بيانات عن 3 طلاب في كورس Python

student1 = {
    "name": "Ahmed",
    "age": 20,
    "country": "Egypt",
    "score": 85
}

student2 = {
    "name": "Mona",
    "age": 21,
    "country": "Egypt",
    "score": 92
}

student3 = {
    "name": "Omar",
    "age": 19,
    "country": "Egypt",
    "score": 78
}


# 1. أنشئ Dictionary باسم students
# يحتوي على الطلاب الثلاثة بالشكل التالي:
#
# "student1" : student1
# "student2" : student2
# "student3" : student3
students = {
    "student1": student1,
    "student2": student2,
    "student3": student3
}

# 2. اطبع Dictionary بالكامل.
print(students)

# 3. اطبع اسم الطالب الأول باستخدام [].
print(students["student1"]["name"])

# 4. اطبع درجة الطالب الثاني باستخدام get().
print(students["student2"].get("score"))


# 5. اطبع جميع Keys الموجودة في students.
print(students.keys())

# 6. اطبع جميع Values الموجودة في students.
print(students.values())

# 7. اطبع عدد الطلاب الموجودين في students
# باستخدام len().
print(len(students))

# 8. اطبع جميع بيانات الطالب الثالث.
print(students["student3"])

# 9. اطبع عمر الطالب الأول
# باستخدام الـ nested dictionary.
print(students["student1"]["age"])


# 10. اطبع عدد العناصر الموجودة داخل بيانات الطالب الثاني.
print(len(students["student2"]))

#----------------------------------#
#---------- Bonus -----------------#
#----------------------------------#

# أنشئ Dictionary جديد باسم course
# يحتوي على:
#
# "name" : "Python for Data Science"
# "level" : "Beginner"
# "students" : students
course = {
    "name": "Python for Data Science",
    "level": "Beginner",
    "students": students
}
# ثم اطبع الـ Dictionary بالكامل.
print(course)

# اطبع اسم الكورس.
print(course["name"])

# اطبع اسم الطالب الثاني من داخل الـ nested dictionary.
print(course["students"]["student2"]["name"])

# اطبع عدد الطلاب المسجلين في الكورس.
print(len(course["students"]))

print("="*100)
#=====================================================================







#-------------------------------------------------------
#-----------------Dictionary Methods--------------------
#-------------------------------------------------------


# clear()

brand = {
    "brand_name" : "Nike"
}
print(brand)
brand.clear()
print(brand)

print("-" * 50)
#=========================================================

# update()

brand = {
    "brand_name": "Nike"
}
print(brand)
brand["total_sales"] = 500
print(brand)
brand.update({"type":"shoes"})
print(brand)

print("-"*50)
#===============================================================

# copy()
 
test = {
    "key_test" : "value_test"
}
copy_test = test.copy()
print(copy_test)
test.update({"key2":"value2"})
print(test)
print(copy_test)
print("-"*50)
#=======================================================================

# setdefault()

user = {
    "name" :"abdelrhman"
}
print(user)
print(user.setdefault("age",20))
print(user)
print("-"*50)
#===============================================================

# popitem()

user = {
    "name": "abdelrhman",
    "score": 100
}
print(user)
user.update({"level" : 3})
print(user.popitem())

print("-"*50)

#======================================================================

# items()
user = {
    "name": "abdelrhman",
    "score": 100
}
all_users = user.items()
print(user)
user["level"] = 36
print(all_users)
# print('-'*50)
#============================================================================

# fromkeys()

a = ("key1" , "key2" , "key3")
b = 0

print(dict.fromkeys(a,b))




#-------------------------------------------------------#
#----------------- Small Exercise ----------------------#
#-------------------------------------------------------#


# لدينا Dictionary يحتوي على بيانات أحد المنتجات

product = {
    "name": "Laptop",
    "price": 25000,
    "category": "Computer"
}


# 1. اطبع الـ Dictionary.


# 2. أضف مفتاح جديد "stock" وقيمته 10
# باستخدام update().


# 3. أضف مفتاح جديد "brand" وقيمته "ASUS"
# باستخدام update().


# 4. أنشئ نسخة مستقلة من product باستخدام copy()
# وضعها في متغير باسم product_copy.


# 5. أضف "discount": 10 إلى product
# ثم اطبع product و product_copy
# ولاحظ الفرق بينهما.


# 6. استخدم setdefault() لإضافة:
# "rating": 4.5
# ثم اطبع الـ Dictionary.


# 7. استخدم setdefault() مرة أخرى على المفتاح "name"
# وحاول إعطاءه قيمة مختلفة.
# لاحظ ماذا يحدث.


# 8. استخدم items() للحصول على جميع
# الـ key-value pairs الموجودة في product.


# 9. أضف مفتاح جديد "color" وقيمته "Gray"
# ثم اطبع الـ items مرة أخرى.
# لاحظ ماذا يحدث للمتغير الذي حصلت عليه من items().


# 10. استخدم popitem() لحذف آخر عنصر
# من الـ Dictionary.
# اطبع العنصر الذي تم حذفه.


# 11. اطبع الـ Dictionary بعد استخدام popitem().


# 12. أنشئ Dictionary جديد باستخدام fromkeys()
# باستخدام الـ keys التالية:
#
# "name", "age", "country", "score"
#
# واجعل القيمة الافتراضية لجميع الـ keys هي 0.


# 13. استخدم clear() لحذف جميع عناصر product_copy.


# 14. اطبع product_copy بعد استخدام clear().


#-------------------------------------------------------#
#---------------------- Bonus ---------------------------#
#-------------------------------------------------------#

# ما الفرق بين:
#
# copy()
# clear()
#
# وما الفرق بين:
#
# setdefault()
# update()
#
# وماذا يحدث عند استخدام:
#
# popitem()
#
# على Dictionary فارغ؟
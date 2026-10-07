# Copyright (c) 2026 Abdelrhman Taha
# All Rights Reserved.
#
# This material is part of the Python-for-Data-Science course.
# Unauthorized reproduction, redistribution, or commercial use is prohibited.


#-------------------------------------------------------#
#----------------- Small Exercise ----------------------#
#-------------------------------------------------------#

# لدينا Dictionary يحتوي على بيانات أحد المنتجات

product = {
    "name": "Laptop",
    "price": 25000,
    "category": "Computer"
}


# 1. اطبع الـ Dictionary
print(product)


# 2. أضف مفتاح جديد "stock" وقيمته 10
# باستخدام update()
product.update({"stock": 10})


# 3. أضف مفتاح جديد "brand" وقيمته "ASUS"
# باستخدام update()
product.update({"brand": "ASUS"})


# 4. أنشئ نسخة مستقلة من product باستخدام copy()
# وضعها في متغير باسم product_copy
product_copy = product.copy()


# 5. أضف "discount": 10 إلى product
# ثم اطبع product و product_copy
product.update({"discount": 10})

print("product:", product)
print("product_copy:", product_copy)


# 6. استخدم setdefault() لإضافة:
# "rating": 4.5
# ثم اطبع الـ Dictionary

product.setdefault("rating", 4.5)

print(product)


# 7. استخدم setdefault() مرة أخرى على المفتاح "name"
# وحاول إعطاءه قيمة مختلفة.
# لاحظ ماذا يحدث.

product.setdefault("name", "HP")

print(product)


# 8. استخدم items() للحصول على جميع
# الـ key-value pairs الموجودة في product.

items = product.items()

print(items)


# 9. أضف مفتاح جديد "color" وقيمته "Gray"
# ثم اطبع الـ items مرة أخرى.
# لاحظ ماذا يحدث للمتغير الذي حصلت عليه من items().

product.update({"color": "Gray"})

print(items)


# 10. استخدم popitem() لحذف آخر عنصر
# من الـ Dictionary.
# اطبع العنصر الذي تم حذفه.

deleted_item = product.popitem()

print("Deleted item:", deleted_item)


# 11. اطبع الـ Dictionary بعد استخدام popitem()

print(product)


# 12. أنشئ Dictionary جديد باستخدام fromkeys()
# باستخدام الـ keys التالية:
# "name", "age", "country", "score"
# واجعل القيمة الافتراضية لجميع الـ keys هي 0.

keys = ["name", "age", "country", "score"]

new_dict = dict.fromkeys(keys, 0)

print(new_dict)


# 13. استخدم clear() لحذف جميع عناصر product_copy.

product_copy.clear()


# 14. اطبع product_copy بعد استخدام clear().

print(product_copy)


#-------------------------------------------------------#
#---------------------- Bonus ---------------------------#
#-------------------------------------------------------#

# copy()
# ينشئ نسخة مستقلة من الـ Dictionary.

# clear()
# يحذف جميع العناصر من الـ Dictionary نفسه.


# setdefault()
# يضيف الـ key فقط إذا لم يكن موجودًا.
# إذا كان الـ key موجودًا، لا يغير قيمته.

# update()
# يضيف keys جديدة أو يعدل قيم keys موجودة.


# popitem()
# يحذف آخر key-value pair في الـ Dictionary
# ويرجع العنصر المحذوف على شكل tuple.

# عند استخدام popitem() على Dictionary فارغ
# سيحدث KeyError.

#=============================================================================================

#===================================
#-------------Boolean---------------
#===================================

# Boolean Values are True and False only

name = "TEST"
print(name.islower())
print("-"*50)
#========================================================
print(10 < 5)
print(79 > 5)
print(100 > 100)
print("-"*50)
#========================================================

# bool()

# True
print(bool("python"))
print(bool(100))
print(bool(50.50))
print(bool(True))
print(bool([1,2,3,4,5]))
print('-'*50)

# False

print(bool(0))
print(bool(""))
print(bool([]))
print(bool(False))
print(bool(()))
print(bool(None))
print('-'*50)


#========================================================

# Boolean Operations

#========================================================

age = 20
grad = 100
level = 1

# and 

print(grad > 250 and level < 3 and age < 30 )


#or 

print(grad > 250 or level > 3 or age < 30)


# not 

print(not age > 10)


print("="*50)
#==========================================================#
#====================== Excersis ===========================#
#==========================================================#


# التمرين 1 — المقارنة
# اكتب ناتج تنفيذ كل سطر:

# print(10 > 5)
# print(3 > 8)
# print(7 < 20)
# print(100 < 50)


#==========================================================#

# التمرين 2 — الدالة bool()
# اكتب ناتج تنفيذ كل سطر:

# print(bool(10))
# print(bool(0))
# print(bool("Python"))
# print(bool(""))
# print(bool([1, 2, 3]))
# print(bool([]))


#==========================================================#

# التمرين 3 — العامل and
# ما الذي سيتم طباعته؟

age = 20
grade = 300

# print(age > 18 and grade > 250)
# print(age > 25 and grade > 250)


#==========================================================#

# التمرين 4 — العامل or
# ما الذي سيتم طباعته؟

age = 20
grade = 200

# print(age > 18 or grade > 250)
# print(age > 25 or grade > 250)


#==========================================================#

# التمرين 5 — العامل not
# ما الذي سيتم طباعته؟

age = 20

# print(age > 18)
# print(not age > 18)
# print(not age < 18)


#==========================================================#

# التمرين 6 — العمليات المنطقية
# أكمل الكود:

age = 22
grade = 280

result = age > 18 and grade > 250

# print(result)

# قم بتغيير قيم age و grade
# ولاحظ متى تكون النتيجة True ومتى تكون False.


#==========================================================#

# التمرين 7 — درجات الطالب
# لدى أحد الطلاب الدرجات التالية:

math = 80
python = 90

# اكتب تعبيرات Boolean للإجابة عن الأسئلة التالية:

# 1. هل درجة الرياضيات أكبر من 50؟

# 2. هل درجة Python أكبر من 50؟

# 3. هل كلتا الدرجتين أكبر من 50؟

# 4. هل درجة واحدة على الأقل أكبر من 95؟


#==========================================================#

# التمرين 8 — تحدي
# لدينا:

age = 19
score = 85

# اكتب تعبير Boolean واحد يتحقق من أن:
# عمر الطالب أكبر من 18
# ودرجته أكبر من 70.
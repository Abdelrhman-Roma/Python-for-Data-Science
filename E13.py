# Copyright (c) 2026 Abdelrhman Taha
# All Rights Reserved.
#
# This material is part of the Python-for-Data-Science course.
# Unauthorized reproduction, redistribution, or commercial use is prohibited.




#----------------------------------
#----- Set Methods ----------------
#----------------------------------

# difference() or  -

a =  {1,2,3,4}
b =  {1,2,"c++","python"}
print(a)
print(a.difference(b))
print(a - b)
print(a)
print('-'*50)
#===================================================
# difference_update

c = {1,2,3,4}
d = {1,2,"c++","python"}
print(c)
c.difference_update(d)
print(c)
print("-"*50)
#====================================================

# intersection() or  &

set1 = {1,2,3,4,"a","b"}
set2 = {"c","d","e","f","g",2,5,6,7}
print(set1)
print(set1.intersection(set2))
print(set1 & set2)
print(set1)
print('-'*50)
#====================================================

# intersection_update()
set1 = {1,2,3,4,"a","b"}
set2 = {"c","d","e","f","g",2,5,6,7}
print(set1)
set1.intersection_update(set2)
print(set1)
print('-'*50)


#===========================================================

# symmetric_difference() or ^

set3 = {1,2,3,4,'i','j','f'}
set4 = {"python","i",1,4,"C++"}
print(set3)
print(set3.symmetric_difference(set4))
print(set3 ^ set4)
print(set3)
print('-'*50)
#=====================================================

# symmetric_difference_update()
set3 = {1,2,3,4,'i','j','f'}
set4 = {"python","i",1,4,"C++"}
print(set3)
set3.symmetric_difference_update(set4)
print(set3)
print('-'*50)
#=============================================================

# issuperset()
set5 = {1,2,3,4}
set6 = {1,2,3}
set7 = {1,2,3,4,5}
print(set5.issuperset(set6))
print(set5.issuperset(set7))
print('-'*50)
#=================================================================
# issubset()

set8 = {1,2,3,4}
set9 = {1,2,3}
set10 = {1,2,3,4,5}
print(set8.issubset(set9))
print(set8.issubset(set10))
print('-'*50)

#==============================================================
# isdisjoint()
set11 = {1,2,3,4}
set12 = {1,2,3}
set13 = {11,12,13}
print(set11.isdisjoint(set12))
print(set11.isdisjoint(set13))


#----------------------------------#
#----- Small Exercise -------------#
#----------------------------------#

# لدينا مجموعتان من الطلاب المسجلين في مادتين مختلفتين

python_students = {"Ahmed", "Ali", "Mona", "Sara", "Omar"}

data_students = {"Ali", "Mona", "Youssef", "Omar", "Khaled"}


# 1. أوجد الطلاب الموجودين في Python فقط
# استخدم difference()


# 2. أوجد الطلاب الموجودين في Data Science فقط
# استخدم -


# 3. أوجد الطلاب المشتركين بين المادتين
# استخدم intersection()


# 4. أوجد الطلاب الموجودين في مادة واحدة فقط
# استخدم symmetric_difference()


# 5. لدينا مجموعة تحتوي على جميع الطلاب

all_students = {
    "Ahmed", "Ali", "Mona", "Sara",
    "Omar", "Youssef", "Khaled", "Hassan"
}

# تحقق هل جميع طلاب Python موجودون في all_students
# استخدم issubset()


# 6. تحقق هل all_students تحتوي على جميع طلاب Python
# استخدم issuperset()


# 7. لدينا مجموعة من الطلاب الغائبين

absent_students = {"Hassan", "Mahmoud"}

# تحقق هل لا يوجد أي طالب مشترك بين absent_students
# و python_students
# استخدم isdisjoint()


#----------------------------------#
#---------- Bonus -----------------#
#----------------------------------#

# استخدم intersection_update() لإيجاد الطلاب المشتركين
# ولاحظ ماذا يحدث للمجموعة الأصلية.


# استخدم difference_update() لإيجاد الطلاب المختلفين
# ولاحظ ماذا يحدث للمجموعة الأصلية.


#----------------------------------#
#---------- Questions -------------#
#----------------------------------#

# ما الفرق بين difference() و difference_update()؟

# ما الفرق بين intersection() و intersection_update()؟

# ما الفرق بين symmetric_difference()
# و symmetric_difference_update()؟
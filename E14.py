# Copyright (c) 2026 Abdelrhman Taha
# All Rights Reserved.
#
# This material is part of the Python-for-Data-Science course.
# Unauthorized reproduction, redistribution, or commercial use is prohibited.


#----------------------------------#
#----- Small Exercise -------------#
#----------------------------------#

python_students = {"Ahmed", "Ali", "Mona", "Sara", "Omar"}

data_students = {"Ali", "Mona", "Youssef", "Omar", "Khaled"}


# 1. أوجد الطلاب الموجودين في Python فقط
# استخدم difference()

python_only = python_students.difference(data_students)
print(f"Python only: {python_only}")


# 2. أوجد الطلاب الموجودين في Data Science فقط
# استخدم -

data_only = data_students - python_students
print(f"Data Science only: {data_only}")


# 3. أوجد الطلاب المشتركين بين المادتين
# استخدم intersection()

common_students = python_students.intersection(data_students)
print(f"Common students: {common_students}")


# 4. أوجد الطلاب الموجودين في مادة واحدة فقط
# استخدم symmetric_difference()

only_one_subject = python_students.symmetric_difference(data_students)
print(f"Only one subject: {only_one_subject}")


# 5. لدينا مجموعة تحتوي على جميع الطلاب

all_students = {
    "Ahmed", "Ali", "Mona", "Sara",
    "Omar", "Youssef", "Khaled", "Hassan"
}

# تحقق هل جميع طلاب Python موجودون في all_students
# استخدم issubset()

print(f"Python students are subset: {python_students.issubset(all_students)}")


# 6. تحقق هل all_students تحتوي على جميع طلاب Python
# استخدم issuperset()

print(f"All students are superset: {all_students.issuperset(python_students)}")


# 7. لدينا مجموعة من الطلاب الغائبين

absent_students = {"Hassan", "Mahmoud"}

# تحقق هل لا يوجد أي طالب مشترك بين absent_students
# و python_students
# استخدم isdisjoint()

print(f"No common absent Python students: {absent_students.isdisjoint(python_students)}")


#----------------------------------#
#---------- Bonus -----------------#
#----------------------------------#

# intersection_update()

python_copy = python_students.copy()

python_copy.intersection_update(data_students)

print(f"After intersection_update: {python_copy}")
print(f"Original python_students: {python_students}")


# difference_update()

python_copy = python_students.copy()

python_copy.difference_update(data_students)

print(f"After difference_update: {python_copy}")
print(f"Original python_students: {python_students}")


#----------------------------------#
#---------- Questions -------------#
#----------------------------------#

# ما الفرق بين difference() و difference_update()؟
# Answer:
        # الفرق ان difference() ما بي تعدلش علي set الاساسيه بل بي ترجعلي value اما الdifferece_update() بي تعدل علي الset الاساسيه


# ما الفرق بين intersection() و intersection_update()؟
# Answer:
        # الفرق ان intersection() ما بي تعدلش علي set الاساسيه بل بي ترجعلي value اما الintersection_update() بي تعدل علي الset الاساسيه


# ما الفرق بين symmetric_difference()
# و symmetric_difference_update()؟
# Answer:
        # الفرق ان symmetric_difference() ما بي تعدلش علي set الاساسيه بل بي ترجعلي value اما الsymmetric_difference_update() بي تعدل علي الset الاساسيه



print('-'*100)


#===========================================================================================

#------------------------------Dictionary---------------------------------------------------
#===========================================================================================


#1.Dictionary Items put in {}
#2 Dictionary Items are contains Key:Value
#3 Dictionary Key Need to be Immutable like (number , string , tuple) list not allowed
#4 Dictionary value can have any data types
#5 nested dictionary
#6 number of elements
#7 Create Dictionary from Variables





#1.Dictionary Items put in {} , Key : value

real_players = {
    "name": "Kylian",

    "age": 26,
    "country": "french",
    "goal": 300,
    "average_game_rate": 8.5,
    (1,2,3,4) : "test",
    "test2" : [1,2,3,4,5]
}

print(real_players)
print('-'*50)

print(real_players['name'])
print('-'*50)
print(real_players.get('name'))
print('-'*50)


print(real_players.keys())
print('-'*50)
print(real_players.values())
print('-'*50)


#5 nested dictionary

courses = {
    "course1" : {
        "name" : "python_course",
        "status" : "complete"
    },
    "course2" : {
        "name" : "C++",
        "status" : "not complete"
    },
    "course3": {
        "name" : "java",
        "status": "N/A"
    }

}

print(courses)
print('-'*50)

print(courses['course1'])
print('-'*50)
print(courses['course2'])
print('-'*50)


print(courses['course1']['status'])
print('-'*50)
print(courses['course2']['status'])
print('-'*50)


#6 number of elements
print(len(courses))
print('-'*50)
print(len(courses['course3']))
print('-'*50)






#7 Create Dictionary from Variables


test1 = {
    'name': "abdelrhman",
    'id': 1
}
test2 = {
    "name":"ahmed",
    "id":2
}
test3 = {
    "name":"roma",
    "id":3
}


tests = {
    'one' : test1,
    'two' : test2,
    'three': test3
}


print(tests)
print('-'*50)

print(tests['one']['name'])








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


# 2. اطبع Dictionary بالكامل.


# 3. اطبع اسم الطالب الأول باستخدام [].


# 4. اطبع درجة الطالب الثاني باستخدام get().


# 5. اطبع جميع Keys الموجودة في students.


# 6. اطبع جميع Values الموجودة في students.


# 7. اطبع عدد الطلاب الموجودين في students
# باستخدام len().


# 8. اطبع جميع بيانات الطالب الثالث.


# 9. اطبع عمر الطالب الأول
# باستخدام الـ nested dictionary.


# 10. اطبع عدد العناصر الموجودة داخل بيانات الطالب الثاني.


#----------------------------------#
#---------- Bonus -----------------#
#----------------------------------#

# أنشئ Dictionary جديد باسم course
# يحتوي على:
#
# "name" : "Python for Data Science"
# "level" : "Beginner"
# "students" : students
#
# ثم اطبع الـ Dictionary بالكامل.


# اطبع اسم الكورس.


# اطبع اسم الطالب الثاني من داخل الـ nested dictionary.


# اطبع عدد الطلاب المسجلين في الكورس.
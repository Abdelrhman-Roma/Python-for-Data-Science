# Copyright (c) 2026 Abdelrhman Taha
# All Rights Reserved.
#
# This material is part of the Python-for-Data-Science course.
# Unauthorized reproduction, redistribution, or commercial use is prohibited.

#------------
#----List----
#------------

#[1] List Items are Enclosed in Square Brackets
#[2] List Items are Ordered
#[3] List Items are Mutable
#[4] List Items can be of Any Data Type
#[5] List Items can be Duplicates
#=================================================

# mylist = ["python", "java", "c++", "c#","c++", "javascript",1,True,False,3.14]


#accessing list items
# print(mylist[0])
# print(mylist[-1])
# print(mylist[2])
# print(mylist[-4])
#slicing list items
# print(mylist[:4])
# print(type(mylist[2:]))
# print(type(mylist[0]))
# print(mylist[::2])
#editing list items

# mylist[0] = "snake"
# print(mylist)
#mylist[0:3] = "programing"
# mylist[0:3] = ["programming","test","test2","test4"]
# print(mylist)


#==============================================
# Lists Methods


#1. .append() - Adds an item to the end of the list


# myCourses = ["Python", "Java", "C++"]
# myGames = ["FIFA", "PUBG", "Call of Duty"]

# myCourses.append("CSS")
# print(myCourses)
# myCourses.append(100)
# myCourses.append(3.14)
# myCourses.append(True)
# print(myCourses)
# myCourses.append(myGames)
# print(myCourses)
# print(myCourses[6])
# print(myCourses[7][0])


#2. extend() - Adds the elements of a list (or any iterable), to the end of the current list
# myCourses.extend(["HTML", "JavaScript"])
# print(myCourses)
# print(myCourses[8])






#3.remove() - Removes the first item with the specified value
# myCourses.append("CSS")
# print(myCourses)
# myCourses.remove("CSS")
# print(myCourses)





#4.Sort() - Sorts the list ascending by default
# mynumbers = [5, 2, 9, 1, 5, 6]
# mylitters = ["c",'e','a','d']
# mylitters.sort()
# print(mylitters)

#mynumbers.sort(reverse = False)
# mylitters.sort(reverse = True)
# print(mylitters)




#5. reverse() - Reverses the order of the list

# mymixedlist = [1, "Python", 3.14, True]
# mymixedlist.reverse()
# print(mymixedlist)

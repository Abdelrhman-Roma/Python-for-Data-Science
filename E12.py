# Copyright (c) 2026 Abdelrhman Taha
# All Rights Reserved.
#
# This material is part of the Python-for-Data-Science course.
# Unauthorized reproduction, redistribution, or commercial use is prohibited.


#-----------------------------------------------
#-----------------Set--------------------------
#------------------------------------------
#1. Set Items put in {}
#2. Set Items Not Ordered and Not Indexed and Slicing
#3. Set has only Immutable data
#4. Set Items is Unique
#5. Set Methods part 1




#1. Set Items put in {}

set1 = {1,2,3,4,5}






#2. Set Items Not Ordered and Not Indexed and Slicing

# print(set1[1:3])









#3. Set has only Immutable data
# numbers
# string 
# Tuple

set2 ={1,2,3,"abdelrham","python",(1,3,4,True)}
print(set2)









#4. Set Items is Unique
set3 = {1,2,1,3,1,3,2,3}
print(set3)









#5. Set Methods part 1


#1. clear()
set3 = {1,2,1,3,1,3,2,3}
set3.clear()
print(set3)




#2. union() or |
set4 ={1,2,3}
set5 = {4,5,6}
print(set4.union(set5))
print(set4 | set5)
set6 = {7,8,9}
print(set4.union(set5,set6))


#3. add()
set6 = {1,2}
set6.add(3)
set6.add(4)
print(set6)



#4. copy()
set7 ={1,2,3,4}
set8 = set7.copy()
print(set7)
print(set8)
set7.add(5)
print(set7)
print(set8)



#5. remove()
set9 = {'a','b','c','d'}
set9.remove('b')
print(set9)
# set9.remove('e')
print(set9)

#6. discard()

set9 = {'a','b','c','d'}
set9.discard('b')
print(set9)
set9.discard('e')
print(set9)



#7. pop()
set10 ={1,2,3,4,5}
print(set10.pop())


#8. update()
set11 = {'a','b','c'}
set12 = {'d','e','f'}
set11.update(set12)
print(set11)
set11.update([1,2,3,4,5])
print(set11)














































# Copyright (c) 2026 Abdelrhman Taha
# All Rights Reserved.
#
# This material is part of the Python-for-Data-Science course.
# Unauthorized reproduction, redistribution, or commercial use is prohibited.

#----------------------------------------------
#--------------- Tuples -----------------------
#==============================================

#1. Tuples Items put in () or without ()
#2. Tuple are ordered, Use Index to access Items
#3. Tuple are Immutable means you can't add or delete
#4. Tuple Items is not Unique
#5. Tuple can have different Data Types
#6. Tuple Methods








#1. Tuples Items put in () or without ()

test1 = (1,2,3,4,5)
test2 = 1,2,3,4,5










#2. Tuple are ordered, Use Index to access Items

test1 = (1,2,3,4,5)
print(test1[0])
print(test1[-1])










#3. Tuple are Immutable means you can't add or delete

test2 = (1,2,3,4,5)
# test2[0] = ()
print(test2)








#4. Tuple Items is not Unique

test4 = (1,2,3,4,5,5,7,6)









#5. Tuple can have different Data Types

test5 = (1,2,True,"ster")












#6. Tuple Methods


#1.Tuple with one Element
mytuple = (1,)
mytuple2 = 1,
print(mytuple)
print(mytuple2)

print(type(mytuple))
print(type(mytuple2))

print(len(mytuple))

#2.Tuple Concatenation
tuple1 = (1,2,3)
tuple2 = (4,5,6)
tuple3 = tuple1 + tuple2
print(tuple3)

tuple4 = tuple1 + ("abdo","taha") + tuple2
print(tuple4)
#3.Tuple,List,String Repeat (*)
tupl1 = (1,2,3)
print(tupl1 * 4)
list1 = [1,2,3]
print(list1 * 5)
s = "python"
print(s*3)



#4. count()
tuple5 =("a","b","c","a","a","b")
print(tuple5.count("a"))
print(tuple5.count("b"))



#5. index()
tuple6 =("a","b","c","a","a","b")
print(tuple6.index("b"))



#6. Tuple Destruct
a = ("a","b","c","d")
x,y,_,z= a
print(x)
print(y)
print(z)


    #6.1 Nested Tuple Destructuring
b = ("a",("b","c"))
x,(y,z) = b
print(x)
print(y)
print(z)







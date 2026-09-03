# Copyright (c) 2026 Abdelrhman Taha
# All Rights Reserved.
#
# This material is part of the Python-for-Data-Science course.
# Unauthorized reproduction, redistribution, or commercial use is prohibited.

#    =============Variables============


# 1. Syntax:
#           Variable Name = Value or None
#========================================
# 2. Variables Rules
# 1.can you write using (a-z , A-Z) or Underscore ( _ )
# 2.can't start with number or any spical character except Underscore
# 3.can include (0-9) or Underscore
# 4.cannot include special Characters
# 5.Variables are Sensitive
#===========================================
# 3. most comman ways to write variables
# 1.camelCase
myAge = 20
myName = "your name"
#2. snake_case
my_age = 20
my_name_is = "Abdelrhman"

#3.UPPER_CASE
PI = 3.14159
MY_AGE = 30 #note: UPPER_CASE use in Constant ex PI = 3.14159
#============================================
# 4.Variables Change Dynamiclay
# ex:
x = 20
print(x) # 20
x = "your name"
print(x) # your name
x = 10.5
x = "python"
print(x) # python

#=============================================
# 5. Reserved words
#
# important Reserved Words in Python
#----------------------------------
# False       None        True
# and         as          assert
# async       await       break
# case        class       continue
# def         del         elif
# else        except      finally
# for         from        global
# if          import      in
# is          lambda      match
# nonlocal    not         or
# pass        raise       return
# try         while       with
# yield

#note you can write help("keywords") to get all Reserved Words
#------------------------------------
#ex 
# for = 4 # error
# True = 8 # error

# 6.to assign multiple Variables
#ex1 
a,b,c =1,2,3
print(a)
print(b)
print(c)
#ex2
x = y = z = 0
print(x)
print(y)
print(z)
#ex3
a,b = 10 , 20
print(a) #10
print(b) #20

b,a = a,b
print(a) #20
print(b) #10






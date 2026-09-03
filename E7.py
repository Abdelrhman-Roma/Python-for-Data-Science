#============================
# Numbers

# Integer (int)
print(type(1))
print(type(100))
print(type(-10))
print(type(-100))
print("-"*50)
#==============================================
# Float 
print(type(1.500))
print(type(100.99))
print(type(-10.99))
print(type(0.99))
print('-'*50)
#==============================================
# Complex 
complex_number = 1+2j
print(type(1+2j))
print(complex_number.real)
print(complex_number.imag)


# Some Rules:
#1. you can Convert from int to float or Complex
#2. you can Convert from float to int or Complex
#3. you cannot convert Complex to any Type

#test 1
print(100)
print(float(100))
print(complex(100))

#test 2
print(10.50)
print(int(10.50))
print(complex(10.50))

#test 3
print(1+2j)
# print(int(1+2j)) #error
# print(float(1+2j)) #error
print('-'*50)



#part 2 
#====================================
#        Arithmetic Operators
#====================================
#1.  + addition
#2.  - Subtraction
#3.  * Multiplication
#4.  / Division
#5.  % Modulus
#6. ** Exponent
#7. // Floor Division


# Addition
print(10+20)
print(-10+20)
print(1 + 2.2)
print(1.5 + 1.5)
print('-'*50)
#=============================================

#Subtraction
print(60 - 30)
print(10 - 15)
print(-15 - 10)
print(1.6 - 1.7)
print(-1.5 - 1.5)
print('-'*50)
#===============================================

# Multiplication
print(10 * 3) 
print(5 * 2)
print(1.5 * 5)
print('-'*50)
#===============================================

# Division
print(100/10)
print(100/50)
print('-'*50)
#===============================================

# Modulus
print(10%2) 
print(12%3) #12/3 = 4   % = 0
print(9%2) 
print(8%3) # 8%3    8-3 = 5-3 = 2-3 = 0 
print('-'*50)
#===============================================

# Exponent
print(4**5)
# print(4 * 4 * 4 * 4 * 4)
print(5**2)
# print(5 * 5)
print('-'*50)
#===============================================

# Floor Division
print(100//20) 
print(110//20)
print(123//10)


print(5 * 3 + 5 / 2 - 3)  
#1. ()
# 2. * , /
# 3. + , - 


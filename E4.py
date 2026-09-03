# =========== String ============

#1. String is a sequence of characters 
#   enclosed in single quotes or double quotes.
#
stringOne = 'Hello World'
print(stringOne)
print('-'*50)
stringTwo = "Hello World"
print(type(stringTwo))
print(stringTwo)
print('-'*50)
stringThree = '''Hello
world'''
print(stringThree)
print('-'*50)
stringFour = """Hello 
Wrold"""
print(stringFour)
print('-'*50)
#==========================================================
#2.String Indexing and Slicing
#   1.All Data in python is Object
#   2.Object is a collection of data and methods that act on that data
#   3.Every Element Has its own index number starting from 0 to n-1
#   4.use [] to access the elements of the string
#   5. use [start:stop] or [start:stop:steps] to slice the string, Tuples or Lists
#           note: stop not include

# Indexing
stringFive = "I learn Data Science" #19-1 =18 start = 0 end = 18
print(stringFive[0]) # I
print(stringFive[8]) # D
print(stringFive[-1]) # e  
print(stringFive[-7]) # S
print('-'*50)

# Slicing [start:stop]
print(stringFive[2:7]) # learn
print(stringFive[8:12]) # Data
print(stringFive[15:18]) # ien
print('-'*50)
print(stringFive[:7]) # I learn (when you don't write the start index, it defaults to 0)
print(stringFive[9:]) # Data Science (when you don't write the stop index, it defaults to the length of the string)
print('-'*50)

# Slicing [start:stop:step] the Default step is 1
print(stringFive[0:10:1]) # I learn Data Science (when you don't write the step, it defaults to 1)
print(stringFive[::2]) # IlanDt cec (when you write the step, it will skip the characters based on the step value)






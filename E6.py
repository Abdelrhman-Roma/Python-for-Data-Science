#-------------------------------------
#----- Strings Formatting ------------
#-------------------------------------

name = "Abdelrhman"
age = 20
city = "Cairo"
gpa = 2.0
print("My Name is: " + name)
# print("My age is: " + age )
# old formating 

print("My name is: %s " % name)
print("My age is: %d" % age)
print("MY gpa is: %.2f" % gpa)
print("My name is: %.2s" % name)
print("my name is %s my age is %d my gpa is %.2f" % (name , age , gpa))
print("-"*50)
#================================================
#new formating 1. .format()
print("My name is: {}".format(name))
print("My age is: {}".format(age))
print("MY gpa is: {:.2f}".format(gpa))
print("My name is: {:.4s}".format(name))
print('-'*50)
#================================================
# more advance (money formating)
money =33333333383838838388
print("my balance is : {:,d}".format(money))
print('-'*50)
#=================================================
#ReArrange formating
a,b,c ="one","two","three"
print("test {} {} {}".format(a,b,c))
print("test {2} {0} {1}".format(a,b,c))
a,b,c =10,20,30
print("test {2:.2f} {0:d} {1:.3f}".format(a,b,c))
print('-'*50)

#new formating f-string formating V3.6+

print(f"my name is {name:.2s}")
print(f"my gpa is : {gpa:.2f}")
print(f"my name is {name} and my age is {age} and my gpa is {gpa}")





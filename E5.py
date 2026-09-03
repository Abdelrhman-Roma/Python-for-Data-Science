# Copyright (c) 2026 Abdelrhman Taha
# All Rights Reserved.
#
# This material is part of the Python-for-Data-Science course.
# Unauthorized reproduction, redistribution, or commercial use is prohibited.

# #====================================
# #======== Strings Methods ===========
# #====================================

# #1.len()
str1 ="hello python hello python"
print(len(str1))
str2 = "hello python             hello python"
print(len(str2))
print('-'*50)

# 2.strip() , rstrip() , lstrip()
str3 ="        hello world         "
print(len(str3))
print(str3.strip())
print(len(str3.strip()))
print(str3.rstrip())
print(len(str3.rstrip()))
print(str3.lstrip())
print(len(str3.lstrip()))
# # #note:what if i add prametar
str4 ="==========hello world=========="
str5 ="&*&*&*&*&*&hello world&*&*&*&*&*&*"
# # #how to remove the extra char
print(str4.strip("="))
print(str5.strip("&*"))

print('-'*50)
# #===============================================

# #3. title()
str6 = "I love 3d animations and i love 3d Shapes"
print(str6.title())
print('-'*50)
# #======================================================

# 4.istitle()
print(str6.istitle())
str6 ="I Love 3D Animations"
print(str6.istitle())
print('-'*50)
# #===============================================

# #5.capitalize()
str7 = "i love 3d animations and i love 3d Shapes"
print(str7.capitalize())
print('-'*50)
# #===============================================

# #6. zfill => zero fill
a,b,c,d = "1" , "11" ,"111","1111"
print(a.zfill(4))
print(b.zfill(4))
print(c.zfill(4))
print(d.zfill(4))
print('-'*50)

# #================================================

# #7. upper() , lower()
str8 = "roma"
str9 = "ABDELRHMAN"
print(str8.upper())
print(str9.lower())
print('-'*50)
# #================================================

# #8. isupper() , islower()
print(str8.isupper())
print(str8.islower())
print(str9.isupper())
print(str9.islower())
print("-"*50)
# #================================================

# #9.split() rsplit() 
str10 = "I love python and C++"
str11 = "I-love-python-and-C++"
print(str10.split())
print(str11.split('-',2))
print(str10.rsplit(" ",2))



print('-'*50)

# #================================================
# #10.splitlines()
str12 = """i love python
python love me
i hate python"""
print(str12.splitlines())
str12 = "i love python\npython love me\ni hate python"
print(str12.splitlines())
print('-'*50)

# #================================================
# #11.center()
str12 = "Abdelrhman"
print(str12.center(20,"*"))
print('-'*50)

# #================================================
# #12. rjust() , ljust()
print(str12.rjust(15,"*"))
print(str12.ljust(15,"*"))
print('-'*50)


# #==================================================
# #13.count("",start,end)
str13 = "I love love Love love love python"
print(str13.count("love"))
print(str13.count("love",0,16))

print('-'*50)
# #================================================
# #14.swapcase()
str14 = "I Love Python"
str15 = "i lOVE pYTHON"
print(str14.swapcase())
print(str15.swapcase())
print('-'*50)

# #================================================
# #15.startswith()
str16 = "I study python"
print(str16.startswith("i"))
print(str16.startswith("I"))
print(str16.startswith("p",8,13))
print('-'*50)

# #=================================================
# #16.endswith()
str16 = "I study python"
print(str16.endswith("n"))
print(str16.endswith("o"))
print(str16.endswith("y",0,7))
print('-'*50)

# #=================================================
# #17.index(substring,start,end)
str17 = "I love python"
print(str17.index("love"))
# print(str17.index("love",7))
print('-'*50)

# #================================================
# #18.find
print(str17.find("love"))
print(str17.find("love",7))
print('-'*50)

# #================================================
# #19.expandtabs()
str18="i\tlove\tpython\tso\tmuch"
print(str18)
print(str18.expandtabs(4))
print('-'*50)

# #================================================
#20.isspace()
str19 = " "
print(str19.isspace())
str19 = ""
print(str19.isspace())
print('-'*50)

# #================================================
# #21.isidentifier()
str20 = "python_numbers"
print(str20.isidentifier())
str20 = "pythonNumbers"
print(str20.isidentifier())
str20 = "3python-Numbers"
print(str20.isidentifier())
print("-"*50)

# #===============================================
# #22. isalpha(),isalnum(),isnumeric()
str21 = "Abcde"
str22 = "Abcde123"
print(str21.isalpha())
print(str22.isalpha())

print(str21.isalnum())
print(str22.isalnum())
str22 ="123445"
print(str22.isnumeric())
print(str22.isnumeric())

print('-'*50)

# #===============================================
# #23. replace(old value ,new value , count)
str23 = "hello python , python is the best ,python python"
print(str23.replace("python","snake"))
print(str23.replace("python","snake",1))
print(str23.replace("python","snake",2))
print('-'*50)

# #=========================================================
#24. sperated.join(Iterable)
str24 = ["python","C++","java"]
print(",".join(str24))
# #=========================================================

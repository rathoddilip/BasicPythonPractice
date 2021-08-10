a = 10
b = "Dilip"
# type of a
print(type(a))
# type of b
print(type(b))
# use like this if we have single quotes in our strings
msg = "hello guy's"
print(msg)
msg = 'Hello guy"s'
print(msg)
# if we want double quotes and single quotes we can use 3 single quotes
stringMsg = '''hello guy's "welcome to python"'''
print(stringMsg)
# concatenating two  strings
str1 = "hello "
str2 = "guy's"
concatenateStr = str1 + str2
print("string concatenate: ", concatenateStr)
# print particular char from string using passing index number
# 0 is start index and 4 is last index of string
print("particular char", concatenateStr[0:4])

# if we don't know the last index char then we can used negative index concep
print("negative index value:", str1[-4:-1])
# skip the char
name = "dilipRathod"
skp = name[1::3]  # --> here skipping the 3 number char
print(skp)
# functions of string
# endsWith(),count(),replace(old,new),len(),capitalize(),find()

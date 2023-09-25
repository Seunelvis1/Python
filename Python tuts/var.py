from math import *
# var1 = 20
# var2 = 30
# print(var1 + var2)

# print(var2 - var1)
# name = "Seun"
# print("Hi, + name + How are you? \n what is your age?")
# print(len(name))
# print(name.replace("S", "T"))

# print(abs(-10))
# print(max(4,6,5,2,1))Seun
# print(min(4,6,5,2,1))
# print(round(3.5))
# print(bin(334))
# print(sqrt(10))

# name = input("what is your name?")
# age = int(input("what is your age?"))
# print("welcome " +name + " you are ", age, " years old")

# sentence = input("Enter your sentence")
# print(sentence)
# word1 = input("Enter the word you want to replace: ")
# word2 = input("Enter the replacement: ")
# print(sentence.replace(word1,word2))

# countries = ["Nigeria", "Spain", "Niger", "Benin", "united kingdom", "Ghana"]
# print(countries)
# print(countries[1][0])
# print(countries[:3])
# print(type(countries))
# countries[2] = "USA"
# print(len(countries))
# #list constructor
# nation = list(("SA", "Gambia", "London"))
# print(nation)
# list functions and methods (extend, append, insert, del, index, count, sort, reverse, copy, pop, clear)
# countries.extend(nation)
# countries.append("Tanzania")
# countries.insert(1, "Cameroun")
# countries.remove("Benin")
# del countries[0]
# print(countries.index("united kingdom"))
# print(countries)
# #Tuples in Python - Tuples are immutable list i.e unchangeable

# num = (1,2,3,4,5,6,7,)
# num1 = tuple((5,6,7,8,9,19))
# print(type(num1))
# print(num[0:3])



# # functions in python
# name = input("What is your name: ")
# age = input("What is your Age: ")
# age2 = 60
# def greetings(name, age):
#     print("welcome " + name + " You are ",age2, " years old")
# greetings(name, age2)

# def my_function():
#     return 7 + 1
# print(my_function())
# if statements
# a,b,c = 10, 30, 30

# if a > b:
#     print("it is greater")
# elif b > c or b > a:
#     print( b, " is greater than ", c)
# else:
#     print("not all")
# value = input("Input a value")
# if type(value) == str:
#     print(value, " is a string")
# else:
#     print("We don\'t know the type of ", value)

# value = int(input('Input a number'))

# if value % 5 == 0:
#     print(value, " is divisible by 5")
# else:
#     print(value, "cannot be divible 5")

# value = input('Input a number')

# if len(value) == 10:
#     print(value, " is okay")
# elif len(value) > 10:
#     print(value, " is too much")
# elif len(value) <= 4:
#     print(value, " is the minimum")

# checks if the number is even or odd

# value = int(input("Input Number: "))
# if value%2 == 0:
#     print(value, " is an even number")
# else:
#     print(value, " is an odd number")

# Dictionairies in Python

# Dict1 = {"country": "Nigeria",
#          "name": "Oluwaseun",
#          "Degree": "Bsc",
#          "Age": 56,
#          "is_tall": True,
#          "friends": ["Peter", "Paul", "Precious", "Daytaller"]
#          }
# xx = Dict1["name"]
# print(Dict1["Degree"])
# print(type(Dict1))
# print(xx)

#While loop in Python
# i = 1
# while i <= 10:
#     print(i)
#     i+=1

# for loop
'''
mylist = ["Oluwaseun", "Precious", "Daytaller", "Blessing"]
myDict = {
    "name": "Oluwaseun",
    "Country": "Nigeria",
    "Age": 40,
    "friends": ["Amara", "Grace", "Chris", "Isreal", "Benteke"]
}'''
# for range in myDict:
#     print(range)
#     if range == "Country":
#         break
# for range in myDict:
#     if range == "Age":
#         break
#     print(range)
'''
for x in range(10):
    print(x)
for x in range(4,11):
    print(x)
else:
    print("Loop is over")
'''
# 2D list and nested loop
# x_list = [
#     [1,2,4],
#     [4,5,6],
#     [7,8,9]
# ]
# for x in x_list:
#     print(x_list)
# for lists in x_list:
#     for row in x_list:
#         print(row) I don't understand nested loops yet!
#Build a basic calculator in python
'''num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter Operator: ")

if op == "+":
    print("The addition is ", num1+num2)
elif op == "-":
    print("THe subraction is ", num1-num2)
elif op == "*":
    print("The multiplication is ", num1*num2)
elif op == "/":
    print("The division is ", num1/num2)
elif op == "%":
    print("The modulos is ",num1%num2)
else:
    print("invalid operator") '''
#Try and except in Python
'''try:
    x = int(input("input an integer"))
    print(x)
except:
    print('Something went wrong please, try again')
'''
# Reading FIles in Python
'''file_country = open("country.txt", 'r')
print(file_country.readlines())
# for lines in file_country:
#     print(lines)
file_country.close()'''

# Writing Files in Python
# 'w' for re-writing the whole doc
# 'a' for appending to the bottom of the doc
# "r-" reading and writing
# writing code script ike .py will require you to use /code in between/
'''file_country2 = open("country2.txt", 'a')
file_country2.write("\nThis is a new text messages")
file_country2.close()
file_code = open('code.py', 'a')
file_code.write('\nAge = [20, 40, 30, 16]\n for i in Age\n print(i)')

file_code.close() '''
from code import Student
from code import say_hi
#Classes and Onject in Python
class My_class:
    def __init__(self, name, age):
        self.name = name
        self.age = age
name = input("Enter your name")
age = input("Enter your age: ")
p1 = My_class(name, age)
print(p1.name)
print(p1.age)

class Person(Student):
    pass

p2 = Person
print(p2.name)
say_hi("John")
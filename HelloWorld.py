#!/usr/bin/env python3.6

# The above line makes the file executable with python3.6 given we chmod u+x file.py and execute it as ./file.py
# mainly useful while executing large script files

# This is a full line comment

from operator import floordiv, truediv
from posixpath import split
from re import I #operator interface functions

print ('Hello, world!') # This is a trailing commentpyenv versions

# """ xyz """"This is not a block comment. Python does not have a block comment. This is a multiline string and costs memory.
#Variable
my_string = "hello this is my_string variable"
print (my_string)
#short hand assignment operators += or -=
my_string+=" adding one more two it with+="
print(my_string)
#variable assignment with another variable
v1 = 1;
v2 = "string"
v1 = v2
print (v1)
v1 = 3
print(v1)
#Strings
#single quoted string
s1='hello'
#double quoted string
s2="hello"
#multi line string
s3 = ''' hello how are you
-- hello2
-- hello3 '''
print(s1)
print(s2)
print(s3)

#python string methonds
# returns matching character as indec value strating 0
f1 = "software".find('r')
f2 = "software".find('u')
print(f1)
print(f2)
#returns capitalized string
print("abc".capitalize)
print("ABC".lower)
#Strings with arithmetic operations
s11 = "spain" + "life"
print(s11)
s12 = "hello"*4
print(s12)
#use quotes or special characters in a string, we can do that using the backslash character \
print("tab\tdelimited")
print("new\nline")
print("tab\tdelimited")
print(" \"Double\" in Double")
print("slash\\character")
#Numbers: Integers, Floats, and Scientific Notation
f1 = 10.5 #float
f2 = 2 #int
f3 = f1*f2
print (f3) #if any arithematic operation between two numbers then if any of the number is float then the resulting answer will be in float
#Numeric operators
print(5/3) # returns float type as reminder
print(5//3) #floord division(//) returns reminder as int
print(5 ** 3) #exponent
print(truediv(5,3)) # div using function
print(floordiv(5,3)) # div using floordiv
#Unary and Bitwise Operators
a = 0b010
print(a)
print("bitwise complementary",~a)
print (bin(a))
#boolean operators
#not operator
print(not True)
#the or operation
print(True or False)
#the and operation
print(False and True)
#comparision operators
print(1>2)
print(1<2)
print(1>=2)
print(1<=2)
print(1==2)
print(1!=2)
#The identity operators
print(1 is 1)
print(1 is not 1)
print([]is[])
#typecasting
#int to float
f1 = float(1)
print (f1)
#float to int
i1 = int(f1)
print (i1)
#int or float to string using string intializer
s1 = str(1)
print(s1)
print(str(1.0))
print(str(False))

#immutable: meaning that it cannot be changed
my_str = 'testing'
print(id(my_str))
cap_str = my_str.capitalize()
print(cap_str)
my_str = 'test_02'
print(id(my_str))
print(id('testing'))
# len function
print(len(my_str))
#indexing and slicing
print(my_str[0:7]) #index value of 2
print(my_str[len(my_str)-1]) # print the string index where len-1
#print(my_str[8]) # it errors out when un indexed value is being requested from the string and results index out of range.
print(my_str[0:3]) #slicing the string per index values
print(my_str[1:]) # [index:] gives the rest of the string values after the given index value
print(my_str[1:6:2])# step value range([start,] stop [, step])
print(my_str[::-1])#step option is stepping backward by using a negative step value.We can reverse an entire string by leaving off the start and end indexes and setting the step value to -1:
#Lists
list_l1 = [1,2.0,'three', True] #Lists are heterogenous(can contain any types) and also indexed
print(list_l1[3])
l_l1 = print(len(list_l1))
print(list_l1[0:l_l1])
list_l1[1] = "l1" #we can modify the list unlike strings.
print(list_l1)
list_l1 += ['a','b','c','d','e'] #concanate lists
print(list_l1)
list_l1[2:5]= [1,2,3,4,5]#slicing and assignment
print(list_l1)
#removing a section of the list by assigning empty list to the slice
list_l1[3:] = ''
print(list_l1)
#other way of removing the list is by using del function
del list_l1[0]
print(list_l1)
#One thing to note about del is that it will remove the entire list variable if we don't pass it an index:
del list_l1 #list is deleted
#list functions and methods
list_l2 = [1,2,3,'a','b','c']
#add or append to list
list_l2.append('d')
print(list_l2)
#insert an item at a particular index
list_l2.insert(3, 4)
print(list_l2)
#index method
print(list_l2.index('b'))
#The in and not in Operators
print(4 in list_l2)
print(5 in list_l2)
print(6 not in list_l2)
#sort and reverse functions 
list_l3 = [4,6,2,7,9]
print(sorted(list_l3))
print(list(reversed(list_l3))) #The reversed function doesn't return a list, but typecasting works for the list type also, and when we have a list iterator we can turn it back into a list using the list function:
#Tuples: An immutable sequence type: we can concanate but cannot change the original tuple that we created.
point = (3.0,4)
print(point)
point = point + (5.0,)
print(point)
#One interesting characteristic of tuples is that we can unpack them into multiple variables at the same time:
x, y, z = point
print(x,y,z)
#dictionaries
ages = {'kevin':20, 'rob':43, 'sam': 34}
print(ages)
print(ages['kevin'])#read values from the dict subscripting using the key
ages['tom']=67
print(ages)
del ages['tom'] #items can be removed from a dict using the del statemtn
print(ages)
#in and out operators only work with keys and not values
print('rob' in ages)
print(20 in ages)#doesn't work with values and prints false.
#dict methods
print(ages.keys())
print(list(ages.keys()))#cast a dict to list type
print(ages.values())#values 
print(ages.items())#each item in dict is a key:value
#String Encoding and Functions
print(ord('a'))
print(chr(8482))
#more string methods
eg_s1 = "testing"
print(eg_s1.lower())
print(eg_s1.upper())#full string will be capatilized unlike capitalize method
print(eg_s1.capitalize())#only first character will be capatilized and rest will be in small caps
print("12".isnumeric())
print("a23".isalnum())
#splitting and joining strings
phrase = "This is a simple source code"
words = phrase.split() #space is the default delimiter
print(words)
url = "https://learn.acloud.guru/course/advanced-perspective-of-classes-and-object-oriented-programming-in-python/overview"
course = url.split("/")[-2]
print(course)
#join method
p1 = ",".join(words) #joins the words with , as limiter and we can also have a space character so that there is a space between each word while its joining
print(p1)
lines = ['First line', 'Second line', 'Third line']
p2 = "\n".join(lines)
print(p2)
#format method : The format method allows us to place {} segments into a string and then have values added into those positions:
print("Hello, my name is {}, and I really enjoy {}. Have a nice day!".format('Keith', 'Python'))
print("Hello, my name is {0}, and I really enjoy {1}. Have a nice day! - {0}".format('Keith', 'Python'))

#if and else statements
#python by default uses four space identation for separation of a block

if "a"=="b":
    print("true")
else:
    print("false")

#multiple conditions: elif

if 5<=3:
    print("true-1")
elif 4<=4:
    print("true-2")
elif 2<=3:
    print("true-3")
else:
    print("true-4")

#pass statement: The pass statement is what is known as a null operation. Absolutely nothing happens when we execute a pass statement, but they are useful as a code placeholder:
if 1+1 == 2:
    print(True)
    pass #do nothing: place holder to provide context for future use
if 1-1 == 0:
    print(True)

#while loop
i = 0
while i <=4:
    i = i+1;
    print("i=",i)

#below is a infinte loop with while
#while True:
#    print("looping")

#for loop:
"""... for TEMP_VAR in SEQUENCE"""
#List with for loop 
colors = ["white",2,"yellow"]
for color in colors:
    print(color)
#tuples with for loop
point = (2.0,3,4.5)
for value in point:
    print(value)
#dict with for loop
dict_1 = {"white":1, "red":5, "yellow":4}
for key in dict_1:
    print(key)
for key,value in dict_1.items():
    print(key,value)
for letter in "hello":
    print(letter)

"""some more examples with nesting loops & conditionals"""

i=0
while i<=5:
    if i/2==2:
        print(True)
    elif i==2:
        print("2")
    i += 1

#continue and break
"""continue will cause to go directly to next iteration: skipping next statements for execution
break will break the iteration or flow when hit"""
colors = ["white","green","yellow","red","orange"]
for color in colors:
    if color=="yellow":
        continue
    elif color=="red":
        break
    print(color)

#range
"""Sometimes we want to iterate a set number of times, but we don't necessarily have a collection to work with. An easy way to achieve this is by creating a range object and iterating over it.
A range is an immutable sequence type that defines a start, a stop, and a step value. The values within the range start with the beginning value and are incremented until the last value in the range is reached. This allows for ranges to be used in place of sequential lists while taking less memory and including more items."""
my_range_1 = range(10)
print(my_range_1)
my_list_r1 = list(range(0,15))
print(my_list_r1)
#range can be used in the loops for self start, stop values as below
for _ in range(0,15):
    print("looping")


#List comprehensions
colors = ['red', 'blue', 'orange', 'green', 'yellow']
warm_colors = [color.upper() for color in colors if color in ['red', 'orange', 'yellow']]
print(warm_colors)

"""The biggest difference here is that we don't need to create an empty list and append to it. Whatever we place to the left of the for statement within the comprehension will be returned as part of the final list.
"""

"""
>>> colors = ['red', 'blue', 'orange', 'green', 'yellow']
>>> uppercase_colors = []
>>> for color in colors:
...     uppercase_colors.append(color.upper())
...
>>> uppercase_colors
['RED', 'BLUE', 'ORANGE', 'GREEN', 'YELLOW']
"""

#Functions:
"""
we can create functions in python using maning conventions lower case starting with a letter or underscore (_)
"""
def _add(n1,n2): # defining the function with two parameters
    result=n1+n2
    print(result)
    return result #return the result
    #If we don't explicitly declare a return value, then the result will be None

print(_add(2,3)) # calling the function with arguments

#Parameters vs Arguments
"""
When we're working with the definition of a function, then the variables defined in the function declaration are the "parameters." 
When we're calling the function, the data that we provide for each parameter is the "argument."
"""
def can_drive(age, driving_age=16): # defining parameters with Default arguments
    return age>=driving_age         # driving_age is the default argument
"""
Parameters with default arguments need to go at the end of the parameters list when defining the function so that positional arguments can still be used to call the function.
"""
print(can_drive(15))
print(can_drive(24))

#Recursion
#Recursion is the practice of calling a function from within itself
"""
Example:
Fibonacci Sequence (1, 1, 2, 3, 5, 8, etc.): In the Fibonacci sequence, the next number is always the sum of the previous two numbers in the sequence
mathematically: f(n) = f(n-2) + f(n-1)
"""

def fib(n):
    if n == 0:
        return n
    elif n == 1:
        return n
    return fib(n-2) + fib(n-1)

print(fib(19))

#scopes
def x_assgn():
    x_scope = 5
    return x_scope
print(x_assgn())

# print(x_scope) : this statement will print below error as the scopr of x_scope variable is only within the function
"""
Traceback (most recent call last):
  File "/Users/dinesh/dinesh-learnings/python-learning-2021/HelloWorld.py", line 368, in <module>
    print(x_scope)
NameError: name 'x_scope' is not defined
"""

#namehiding scope

y = 5 
def x_y_assgn(y):
    x = y
    return x

print(x_y_assgn(10))
print(y)

#lambdas
#anonymous functions
square_lambda = lambda num:num*num
print(square_lambda(2))

"""
Filter(). This is a Python inbuilt library that returns only those values that fit certain criteria. 
"""
#filter(function, iterable)
list_1 = [1,2,3,4,5,6,7,8,9]
p_l1 = list(filter(lambda x: x%2 ==0, list_1)) #filter for even numbers in a list using lambda function and iterating with list items
print(p_l1)

"""
map function
Map(). This is another inbuilt python library with the syntax map(function, iterable).
This returns a modified list where every value in the original list has been changed based on a function.
"""
s_l1 = list(map(lambda a: pow(a, 3), list_1)) # calculating cubes 
print(s_l1)


#!/usr/bin/env python3.6

# The above line makes the file executable with python3.6 given we chmod u+x file.py and execute it as ./file.py
# mainly useful while executing large script files

# This is a full line comment

from operator import floordiv, truediv #operator interface functions

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
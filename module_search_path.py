import sys
import platform

print(sys.path) #module search path
print("----------------")
print(sys.platform)
print("----------------")
print(dir(platform)) #platform package #The dir function returns a list of all of the variables and functions that the object encompasses
print(platform.python_version())
print(platform.node())
print(platform.uname())

print(dir(str))
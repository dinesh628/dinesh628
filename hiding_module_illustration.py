from helpers import *

name = "Keith Thompson"
print(f"Lowercase letters: {helpers.extract_lower(name)}") # this will error as in the hiding_module.py only uppercase func is allowed into all and lower func is hidden
print(f"Uppercase letters: {helpers.extract_upper(name)}")
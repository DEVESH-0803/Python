# modules: built in libraries that we can import and use in our code. 
# They are pre-written code that provides additional functionality to our programs. 
# We can use modules to perform specific tasks without having to write the code from scratch.

import math
import random as rdm # we can also give an alias to the module name for easier reference
import sys
from enum import Enum
# import cstm

# print(math.pi)
# choice = rdm.choice(['apple', 'banana', 'cherry'])
# print(choice)
# print(sys.version)

# # dir : directory of a module
# print(dir(math)) # to see all the functions and variables available in the math module

# # better way:
# for item in dir(math):
#         print(item)



## Custom module
# print(cstm.name)
# print(cstm.profession)
# cstm.skills()

# print(__name__)
# print(cstm.__name__)
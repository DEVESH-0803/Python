#While Loop : until cond. true

value = 0

# while(value<=10):
#     print(value)
#     value +=1 

#break statement
# while(value<=10):
#     print(value)
#     if value == 7:
#         break   
#     value +=1

##continue statement
## How not to use: (value afterwards cont statement)

# while(value<=10):
#     print(value)
#     if value == 7:
#         continue    # Explain continue...
#     value +=1

## Correct Way
##break statement
# while(value<=10):
#     value +=1
#     if value == 7:
#         continue  
#     print(value)
# else:
#     print(f'Value is now {value}')

##########################################################################################

## TRUTHY & FALSY VALUES
# In Python, every value can be evaluated as either True or False when used in a 
# condition (like in if, while, etc.).

# Truthy values: A value is truthy if it evaluates to True in a boolean context.
# Non-empty strings ('y', 'hello'), Non-zero numbers, Lists with items, True,etc. 

# Falsy values: A value is falsy if it evaluates to False in a boolean context.
# 0, "None", '' (empty string), False


# value = 1, False, "", "hello", 2, -1, [], ['hello', 2], 0



# question to ask??

value = True
count = 0

while value:
    count += 1
    print(count)
    if value == 5:
        break
    else:
        value = 0
        continue


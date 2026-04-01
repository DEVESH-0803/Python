# name = 'John' # Global scope variable
# count = 4

# def print_name(name):
#     color = 'Yellow' # Local scope variable
#     # count = 10
#     # count += 1 # error 
#     # however to use n modify global variable inside a function, we can use the global keyword
#     # global count
#     count += 1

#     print(count)
#     print(color)
#     print(name) 

# print_name('Jane')
# print(name)
# print(color)


# # calling function inside another function

# print_name('John The Don!')

# def another_function():
#     print('Hello from another function')
#     print_name('Amara')

# another_function()    

# defining a function inside another function

# def outer_function():

#     print('This is the outer function')
#     value = 17.63 # declared in parent fxn

#     def inner_function(num):
#         print('This is the inner function')
#         print(num)

#         # value += 10 # error use nonLocal keyword to modify
#         # nonlocal value
#         # value += 10
#         print(value)

#     inner_function(5)

# outer_function()
# inner_function() #Error

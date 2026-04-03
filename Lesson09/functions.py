# def hello():
#     print('Hello world!') #defined but no o/p cauz not called

# hello() # making a call to function.  
 

# Imp. : Function names can only be separated thro _ no Caps or spaces allowed.

###################################################################################################

# parametrized functions
def add_nums(num1, num2):  
    print(num1 + num2)


# add_nums(1)


# add_nums(4,5)
# add_nums(432,744)

###################################################################################################

# Reusable Function:  -> fx returns a value, can store n use acc.
def add_nums(num1, num2):
     return num1 + num2 

res = add_nums(5,4)
print(add_nums(5,4))

# result = add_nums(122,31)
# print(result*10)  

##############################################################################################

# Adding a check to fxn:
# def add_nums(num1, num2):
#     if (type(num1) is not int or type(num2) is not int):
#         return   
    
#     return num1 + num2 

# result = add_nums('12', 31)
# print(result)  

##############################################################################################

# Example with default values - what are default values(use if no values provided) n why(let's us call the funtion even w/o args)?
# def add_nums(num1=0, num2=0):     
#     if (type(num1) is not int or type(num2) is not int):
#         return   
#     return num1 + num2 

# result = add_nums()
# print(result)  

###############################################################################################

# Multiple arguments n we don't know

# def multi_items(*args):
#     print(args)            
#     print(type(args))

# multi_items(['1', 12, 32, (True, False, []), (), "Soham"])

#############################################################################

# Multiple args but with keys

# def multiple_items(**kwargs): #kwargs->keyswords arguments
#     print(kwargs)            
#     print(type(kwargs))  


# multiple_items(first = "Harsh", second = "Saini", third = "Hello") #-> only the key value pairs will be collected in kwargs, rest will be ignored.
# multiple_items('Hey', 'Hello', first = "Harsh", second = "Saini") #-> only the key value pairs will be collected in kwargs, rest will be ignored.
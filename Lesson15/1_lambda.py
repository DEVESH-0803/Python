# lambda expression are anonymous functions, meaning they do not have a name. 
# or a single expression that returns a value(we do not have to return explicitly). 

add_one = lambda x: x + 1
print(add_one(5))

square_num = lambda x: x ** 2
print(square_num(4))

add_nums = lambda x, y : x + y
# def add_nums(x, y): return x + y
print(add_nums(3, 5))

## USE CASE: a quick fxn (no name, one line) that we will use only once. 

def function_builder(x):
    return lambda num  : num + x

add_five = function_builder(5)
add_ten = function_builder(10)

print(add_five(3)) # num = 3, x = 5
print(add_ten(3)) 




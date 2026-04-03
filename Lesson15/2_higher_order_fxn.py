## Higher Order functions: functions that take in other functions as arguments or return a function.

# lambda x : x*x

numbers = [13, 7, 9, 4, 3] # can use tuples, sets, etc.


square_nums = map(lambda x : x*x, numbers) # map() takes a function as 1st arg n iterable as 2nd arg. 
print(list(square_nums)) # map() returns a map object, we can convert it to a list to see the results.

for num in square_nums:
    print(num)

# even_nums = filter(lambda x : x % 2 == 0, numbers) # filter() takes a function as 1st arg n iterable as 2nd arg.
#                                                    # filter() returns a only the elements that satisfy the condition in the lambda function.
# print(list(even_nums))

# reduce() = It takes 2 items at a time, applies a function, then keeps using the result with next item.
# from functools import reduce

# nums = [1, 2, 3, 4]
# result = reduce(lambda x, y: x + y, nums)
# print(result)

# nums = [1, 2, 3, 4]
# result = reduce(lambda x, y: x * y, nums)
# print(result)
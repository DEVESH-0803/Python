myTuple = tuple((12, 'David', True, 12, 32, 23.543))
# print(myTuple)
anotherTuple = (12, 'Hello', False, 'David', True, 12, 32, 23.543)
# print(anotherTuple)

#order n data can't be changed o/w just like lists in normal brackets

print(type(myTuple))
print(type(anotherTuple))

# if have to do something with tuples copy it to list
myList = list(myTuple)
print(myList)
print(type(myList))

# myList.append('Anjali')
# print(myList)

# myTuple = tuple(myList)
# print(myTuple)

#Unpacking a tuple
# one, *two, three = myTuple
# print(one)
# print(two)
# print(three)
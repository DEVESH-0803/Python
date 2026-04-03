users = ['Devesh', 'Satyarth', 'Shivam', 'Rohit', 'Rahul', "Rohit", "Mohit", "Katrina", 'ankit']
data = ['Ryan', 2, False, 4, 5, 99.32, [5,2,1,3] ]
empty_list = []
nums = [21,12,4,1,23,12,12,65]



# # checking if an element is present in the list or not
# print('Rohit' in users) 
# print("Sagar" in nums) 



# # adding an element to the list
# users.append('Ankit')
# print(users) 


# # inserting an element at a specific index
# users.insert(0, 'James') 
# users.insert(2, 'harshita')
# print(users) #appends adds an element at the end of the list, while insert allows you to specify the index where the element should be added.


# #Insert n Replace elements simultaneously
# print(users)

# users[2:2] = ['Ghania', 'John',"Jhonny"] 
# print(users)

# users[2:4] = ['Rahul', "Rohit", "Mohit", "Katrina"]
# print(users)

################################################################################################################



# # removing an element from the list
# users.remove('Rohit') # removes the first occurrence of 'Devesh'
# print(users)
# print("")


# #deleting 

#01. element at specific index
# del users[1]
# print(users)
# print("")



# #02. deleting whole data(list) with variable
# del data
# print(data) # this will raise an error because the list 'data' has been deleted

# data.clear()
# print(data)
# print("")


# # accessing elements of the list
# print(users[0]) 
# print(data[2])



# # checking index of a particular element
# print(data.index(False))
# print(users.index('Rohit'))
# print("")



# # slicing
# print(users[1:3])  
# print(users[-5:-2])
# print("")



# # length of the list
# print(len(users)) 
# print("")




# # concatenating two lists
# newlist = (users + data)
# print(newlist)
# print("")



# users += ['Daniela'] # adding a single element to the existing list
# print(users)
# print("")



# users.extend(['Katrina', 'Katrina']) # adding a list of elements to the existing list
# print(users)
# print("")




# # repeating a list
# repeatedlist = users * 3
# print(repeatedlist)
# print("")



# # sorting a list
numbers = [5, 2, 9, 1, 5, 6]
# data.sort()
# print(data)




# # sorting in descending order
# numbers.sort(reverse=True) # sorts the list in descending order
# print(numbers)
# print("")

# # #sorting w/o modifying actual list

# print(numbers)
# print(sorted(numbers, reverse = True))
# print(numbers)


# users += ['ankit']
# users += ['Zandu']
# users.sort()
# print(users)
# print("") 

# sorting the lowercase letters before uppercase letters
# users.sort(key=str.lower)  #key -> before sorting, transform each element using this function.”
# #                           #str.lower -> lower case
# print(users)


# # popping an element from the list
# popped_element = users.pop()
# print(popped_element) 
# val = print(users) 
# print(val)


# #Copying the actual list
# copy_list = data.copy()
copy_list = list(data)
print(copy_list)


# #using list constructor to create a list
new_list = list(('Hey', 'Hie','2',True, [], 32.23))
print(new_list)
#Dictionaries -> store data in key, value pairs

details = {
    'name' : 'Python',
    'language' : 'High Level'
}

details01 = dict(name = 'Python', language = 'High Level')

# print(details)
# print(details01)
# print(type(details01))
# print(type(details))
# print(len(details))


# #Access
# print(details['name'])
# print(details.get('language')) 

# #print all values
# print(details.values())

# #List all keys
# print(details.keys())

# #List all key/value pairs as tuples
# print(details.items())


# #Verify key existence
# print("name" in details)
# print("data types" in details)


# #Change values
# details['language'] = 'Interpreted Lang'
# print(details)
# details.update({'type': "dynamic"})
# print(details)

# #Remove
# details.pop("type")
# print(details)

# details['type'] = 'Interpreted' # adds another key:value pair
# print(details)

# print(details.popitem()) #removes n returns last pair
# print(details)

# #Delete and clear
# details01.clear()
# print(details01)

# details['new'] = 'data'
# print(details)
# del details['new']
# print(details)

# del details01
# #print(details01) -> ERROR


# #Copying
# #HOW NOT TO DO

# details02 = details
# print("BAD COPY!") #both points to same obj n change in one reflects in another(2 reference for 1 obj)

# print(details)
# print(details02)

# details02['type'] = 'Dynamic'
# print(details) #changed details01 but details also got 

# # CORRECT way to copy dicts.
# details01 = details.copy()
# print("Good Copy!")
# details01['type'] = 'Dynamic'
# print(details01)
# print(details)

# # or use dict constructor
# details03 = dict(details)
# print("Good Copy!")
# details03['type'] = 'Dynamic'
# print(details)


# #NESTED Dicts.

son = {
    "name" : "Rahul",
    "age" : "23"
   }
daughter = {
    "name" : "Saumya",
    "age" : "21",
    'name' : "Sneha"
}
parent = {
    "son" : son,
    "daughter" : daughter





    
}
print(daughter)
print(parent['daughter']["name"])





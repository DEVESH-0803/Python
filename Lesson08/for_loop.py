names = ['Ankit', 'David', 'Neha', 'Anjali']
# # for name in names:
# #     print(name) 

# city = 'Vishakhapatnam'
# for letter in city:
#     print(letter)

# using with break

# for name in names:
#     if name == 'Neha':
#         break
#     print(name)
    


# with Continue

# for name in names:
#     if name == 'Neha':
#         continue
#     print(name)

#range function

# for num in range(4):
#     print(num)

# for x in range(2,4):
#     print(x)

# # telling to add a no.
# for x in range(3,100, 5):
#     print(x)
# else:
#     print('Glad that\'s over')


# else with break (only executes if loop finishes completely)
# for name in names:
#     if name == 'Neha':
#         break
#     print(name)
# else:
#     print('Glad that\'s over')

# Nested Loop
names = ['Ankit', 'David', 'Neha', 'Anjali']
actions = ['codes', 'eats', 'sleeps']

# for name in names:
#     for action in actions:
#         print(f'{action} {name}') 

for action in actions:
    for name in names:
        print(f'{name}.')
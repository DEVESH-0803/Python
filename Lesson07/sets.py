nums = {1,2,3,4}
nums1 = set((1,2,3,4))
# print(nums)
# print(nums1)
# print(type(nums))
# print(len(nums))

# #No Duplicates allowed
# nums1 = {1,2,3,3,4,5,3}
# print(nums1)

# #True is a dupe of 1 n False is a dupe of 0
# newSet = {1,True, 32.23, False, 21, 0, 12}
# print(newSet)

# print(2 in nums)

# #can't access elem using index - unordered
# print(nums[2])

# #Adding a new element 
# nums.add(8)
# print(nums)


# #Adding elements from another set
# new_nums = {7,2,8,9,10}
# nums.update(new_nums)
# print(nums)

#u can use lists, tuples, dicts as well in update
# nums.update((3,4,654,45,36,25))
# print(nums)
# nums.update([3,4,654,45,36,25], [999,888,777,1,2,3,4])
# print(nums)
# nums.update({'key' : 12, 'second_key' : 32})
# print(nums)

# #Merge two set to create a set
one ={1,2,3,4}
two = {'hey', 'hello','literals', 1,2,4,5,6}

# myNewSet = one.union(two)
# print(myNewSet)

# #Keep only the duplicates
# one.intersection_update(two) #intersection_update() modifies one
# print(one)

# #Keep everything except duplicates
one ={1,2,3,4}
two = {'hey', 'hello','literals', 1,2,4,5,6}

one.symmetric_difference_update(two)
print(one)

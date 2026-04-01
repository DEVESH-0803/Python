def add_num(num):
    
    total = num + 5 
    print(total) 
    
    if num>=50:
       return 
    
    return add_num(total) 

add_num(3) 

# #######################################

# # adding expression to first return statement 

# def add_num(num):
#     if num>=50:
#        return num+5
#     total = num + 5
#     return add_num(total)

# final_value = add_num(3)
# print(final_value)

# ##############################################

# # not returning anything at the end

# def add_num(num):
#     if num>=50:
#        return num+5
#     total = num + 5
#     add_num(total)

# final_value = add_num(3)
# print(final_value)

##############################################

# not using condition 

# def add_num(num):
#     total = num + 5
#     return add_num(total)

# final_value = add_num(3)
# print(final_value)



    

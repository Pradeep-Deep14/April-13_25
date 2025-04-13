def append_item(lst):
    lst.append(4)
    return lst  #No need of return statement

my_list = [1, 2, 3]
append_item(my_list)
print(my_list)  # Output: [1, 2, 3, 4]
#with or without return statement, the output will be same
# The function modifies the list in place, so the original list is changed.
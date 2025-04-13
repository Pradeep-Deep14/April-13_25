my_list=['']
if my_list == True:
    print("The list is not empty")
else:
    print('The list is empty')

#comparing a list to true in python always returns false, so the above code will always print 'The list is empty'
# The correct way to check if a list is empty is to use the len() function
# or to use the not operator
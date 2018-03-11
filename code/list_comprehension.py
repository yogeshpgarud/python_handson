# Objecttive of the program is to understand how we can use list comprehension in order perform some additional
# tasks like reading list and preparing another list dynamically based on some criteria.

# input  - list containing number
# output - count occurances of the number in the list

input_data = [1, 2, 3, 4, 5]

# solution1 implementation

counter = 0
number = 2
for no in input_data:
    if number == no:
        counter += 1
print counter

# solution2 implementation -

init_value = 1
counter = sum([init_value for no in input_data if no == number])
print counter

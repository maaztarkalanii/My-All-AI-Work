# A tuple in Python is a collection of elements that
# is ordered and immutable (cannot be changed after creation).
# Tuples are used to store multiple values in a single variable


My_tuple = (20,30,40)
print(My_tuple)
# reading a specific index
print(My_tuple[2])

# My_tuple[2] = 30  it will show error 
 # error TypeError: 'tuple' object does not support item assignment
print(My_tuple)
# Tuple has only two methods index and count
# index show the that the value is stored on which location of tuple
print(My_tuple.index(20))
# Counts how many times a number appears in tuple 
print(My_tuple.count(20))


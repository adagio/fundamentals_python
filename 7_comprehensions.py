# List
# tuple is a list of immutable objects
# expression = ( (x+1) ** 2 for x in range(4))

print("Using tuple expression:")

squares_tuple = tuple( (x) ** 2 for x in range(4))
print(type(squares_tuple))
print(squares_tuple)
squares_tuple = tuple( [(x) ** 2 for x in range(4)] )
print(type(squares_tuple))
print(squares_tuple)

#declare a tuple
# squares_tuple = (1, 4, 9, 16)
another_tuple = (1, 4, 9, 16, 4)
print("Another tuple:")
print(another_tuple) # Output: (1, 4, 9, 16, 4)

# dictionary comprehension

# Using dictionary comprehension to create a dictionary of squares
squares_dict = {x: (x) ** 2 for x in range(0,7)}
#squares_dict = {x: (x) ** 2 for x in range(1,7)}
print("Using dictionary comprehension:")
print(squares_dict) # Output: {0: 1, 1: 4, 2: 9, 3: 16}
print(squares_dict[3])

# set is unordered collection of unique elements
# set is a dictionary without keys
# {expression for item in iterable if condition}
words = ['monitor1', 'monitor2', 'mouse', 'keyboard2']
lengths = {len(word) for word in words}
print("Using set comprehension:")
print(lengths)


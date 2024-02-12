# Creating a tuple
my_tuple = (1, 2, 3)

# Unpacking the tuple into separate variables
a, b, c = my_tuple

print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3



# Function returning a tuple
def get_coordinates():
    return 10, 20

# Tuple unpacking with function return value
x, y = get_coordinates()
print(x, y)  # Output: 10 20

# Multiple return values from a function
def multiple_return():
    return 'apple', 'banana', 'cherry'

fruit1, fruit2, fruit3 = multiple_return()
print(fruit1, fruit2, fruit3)  # Output: apple banana cherry

# Tuple unpacking when iterating over a sequence
coordinates = [(1, 2), (3, 4), (5, 6)]
for x, y in coordinates:
    print(f'X: {x}, Y: {y}')

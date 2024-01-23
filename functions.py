# Python Functions. Uses as listed.

"""
#Reusable Blocks of Code

def greet(name):
    print(f"Hello, {name}!")

      # Call the function
greet("Alice")
"""

"""
# Modularity: Functions promote modularity.

def calculate_area(radius):
    return 3.14 * radius**2

# Use the function in different parts of the program
circle_area = calculate_area(4)
print(f"Area of the circle: {circle_area}")
"""

"""
# Encapsulation

def perform_task():
    # Code details encapsulated within the function
    print("Performing a specific task")

# Call the function
perform_task()
"""

"""
# Parameterization

def multiply(a, b):
    return a * b

result = multiply(3, 4)
print(f"The result is: {result}")
"""

"""
# Return Values

def add_numbers(x, y):
    return x + y

result = add_numbers(10, 5)
print(f"The sum is: {result}")
"""
"""
# Code Reusability

def square(num):
    return num**2

# Reuse the function in different parts of the program
area1 = square(4)
area2 = square(6)

print(area1)
print(area2)
"""

"""
# Name Space

def namespace_example():
    local_variable = "Inside the function"
    print(local_variable)

# This would cause an error
# print(local_variable)

# Call the function
namespace_example()
"""

"""
# Abstraction

def calculate_something():
    # Assume this is a complex calculation
    return 42

def perform_complex_task():
    # Complex implementation details abstracted away
    result = calculate_something()
    return result

# Use the function without needing to know the details
result = perform_complex_task()
print(f"The result of the complex task is: {result}")
"""

"""
# Support for User-Defined Functions

def custom_function():
    print("This is a user-defined function")

# Call the custom function
custom_function()
"""

"""
# Arguments in Functions.

def my_function(first_name):
    print(first_name + " Iresa")

my_function("Marigi")
my_function("Manuel")
"""

"""
# Python also accepts function recursion, which means a defined function can call itself.
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(4)
"""

# Exercise

def fiz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return ('FizzBuzz')
    if input % 3 == 0:
        return ('Fizz')
    if input % 5 == 0:
        return ('Buzz')
    return input

print(fiz_buzz(11))
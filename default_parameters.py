# Python Default Parameters.

# Multiple Default Parameters

"""
def greet(name='there', message='Hi'):
    return f"{message} {name}"

greeting = greet()
print(greeting)
"""

"""
def greet_function(name = 'Manuel', message = 'How are you'):
    print(f'{message}, {name}?')

greet_function()                         # Returns the default values assigned above.
greet_function(name = 'Iresa')           # Returns the argument given.
"""

# The following calls the greet() function and passes the two arguments
"""
def greet(name, message='Hi'):
    return f"{message} {name}"


greeting = greet('John', 'Hello')
print(greeting)
"""
# The following calls the greet() function without passing the second argument
"""
def greet(name, message='Hi'):
    return f"{message} {name}"


greeting = greet('John')
print(greeting)
"""

# Keyword arguments
"""
def greet(name, age, city):
    print(f"Hello {name}! You are {age} years old and live in {city}.")

# Using positional arguments
greet("Alice", 25, "Wonderland")

# Using keyword arguments (order doesn't matter)
greet(age=30, name="Bob", city="Cityville")
"""

# An example of a function that calculates the net price after applying a discount to a given price. 
# We'll use keyword arguments to make the function more flexible.

def calculate_net_price(price, discount_rate=0.1):
    """
    Calculate the net price after applying a discount.

    Parameters:
    - price: The original price of the item.
    - discount_rate: The discount rate as a decimal (e.g., 0.1 for 10%).

    Returns:
    - net_price: The calculated net price after applying the discount.
    """
    discounted_amount = price * discount_rate
    net_price = price - discounted_amount
    return net_price

# Example usage with positional and keyword arguments
original_price = 100
discounted_price = calculate_net_price(original_price)
print(f"Original Price: ${original_price}, Net Price after 10% discount: ${discounted_price}")

# Example with a different discount rate using keyword argument
custom_discounted_price = calculate_net_price(original_price, discount_rate=0.2)
print(f"Net Price after 20% discount: ${custom_discounted_price}")

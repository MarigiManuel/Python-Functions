# Find more explanations on Pythontutorial.net

# Without recursive function
"""
def count_down(start):
    ''' Count down from a number  '''
    print(start)

count_down(3)
count_down(2)
count_down(1)
"""

# With a recursive function
"""
def count_down(start):
    ''' Count down from a number  '''
    print(start)

    # call the count_down if the next
    # number is greater than 0
    next = start - 1
    if next > 0:                         # This condition is necessary so the countdown is able to stop.
        count_down(next)

count_down(3)
"""
# Using a recursive function to calculate the sum of a sequence
# Suppose that you need to calculate a sum of a sequence e.g., from 1 to 100.
# A simple way to do this is to use a for loop with the range() function
"""
def seq_sum(n):
    total = 0
    for index in range(n + 1):
        total += index
    return total
    
result = seq_sum(100)
print(result)
"""

"""
def sum(n):
    if n > 0:
        return n + sum(n-1)
    return 0


result = sum(100)
print(result)
"""

# Challenge 1

# Write a recursive function to calculate the factorial of a non-negative integer. 
# The factorial of a number is the product of all positive integers up to that number. For example, the factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120. 
# Your function should take an integer as input and return its factorial.

def int_factorial(n):
    if n == 0 or n == 1:
        return
    else:
        return n * int_factorial(n - 1)
    
number = 6
result = int_factorial(number)
print(f'The factorial of {number} is: {result}')
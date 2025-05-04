"""
Syntax Error: Occurs when the rules governing the construction of valid statements in a language are violated, i.e., when a grammatical rule of the language is violated.
Example: Missing a required keyword, such as `def` when defining a function, causes a syntax error because Python expects specific keywords for certain operations.
"""

# Instructor Note: Missing `def` keyword before function name
calculate_area(length, width):
    return length * width

# Instructor Note: Missing `return` keyword in function body
def is_positive(number):
    number > 0

# Instructor Note: Missing `def` keyword before function name
print_message(message):
    print(message)
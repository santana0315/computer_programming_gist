"""
Syntax Error: Occurs when the rules governing the construction of valid statements in a language are violated, i.e., when a grammatical rule of the language is violated.
Example: Missing a required keyword, such as `def` when defining a function, causes a syntax error because Python expects specific keywords for certain operations.
"""

# Instructor Note: Incorrect indentation in function body (return statement not aligned with function block)
def calculate_area(length, width):
return length * width

# Instructor Note: Incorrect indentation in function body (if statement indented too far)
def is_even(number):
        if number % 2 == 0:
            return True
        return False

# Instructor Note: Incorrect indentation in loop body (print statement not aligned with for loop)
def print_squares(n):
    for i in range(n):
    print(i * i)
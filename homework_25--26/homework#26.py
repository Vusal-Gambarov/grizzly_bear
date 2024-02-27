# """
# - Functions -
# A. Create a function 'greet_user' that takes a name as an argument and 
# prints a greeting message with the provided name. The function should 
# have a default parameter of "User" for the name.

def greet_user(name = "User"):
    print(f"Hello, {name}!")
    
user_name = input("Enter your name\n>>")
greet_user(user_name)


# B. Create a function calculate_sum that calculates the sum of an 
# arbitrary number of integers passed as arguments. The function should use 
# the *args parameter to accept a variable number of arguments.

def calculate_sum(*args):
    return sum(args)

numbers = 1, 2, 3, 4, 5
number_sum = calculate_sum(*numbers)
print(number_sum)

# C. Create a function display_info that takes a person's information 
# (name, age, and city) as keyword arguments and prints the information.

def display_info(name, age, city):
    print(f"User info - name : {name}, age : {age}, birthplace : {city}.")
    
name = "Anar"
age = 25
birthplace = "Baku"

display_info(name=name, age=age, city=birthplace)

# D. Create a function make_sandwich that takes the type of sandwich, and 
# optional toppings and prints the details of the sandwich. The function 
# should have a default parameter for the sandwich type and use keyword 
# arguments for toppings.

def make_sandwich(*args, sandwich = "Chicken Wrap"):
    print(f"{sandwich} with:")
    for arg in args:
        print(arg)
    
toppings = "lettuce", "cheeese", "onions"
make_sandwich(*toppings)

# E. Create a function show_details that takes a person's name as a fixed 
# parameter, followed by an arbitrary number of hobbies using the *args 
# parameter. The function should print the person's name and their hobbies.

def show_details(name, *args):
    print(f"{name}'s hobbies are: {", ".join(args)}")
        
name = "Mark" 
hobbies = "reading", "collecting coins", "football"
show_details(name, *hobbies)


# F. Implement a function sort_numbers that takes a list of numbers as an 
# argument and returns a sorted list in ascending order. Use the * operator 
# to unpack the list.

def sort_numbers(*numbers):
    return sorted(numbers)

numbers = [34, 3, 27, 9, 14, 6, 4, 1]
sorted_numbers = sort_numbers(*numbers)
print(sorted_numbers)

# G. Create a function create_user that takes the user's name, age, and email 
# as keyword arguments and prints a message welcoming the user. Ensure to handle 
# missing or invalid email addresses.

import re

def create_user(name, age, email):
    if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Invalid or missing email address. Please provide a valid email.")
        return
    
    print(f"Welcome, {name}! You are {age} years old. We're glad to have you.")

name = input("Enter your name\n>>")
email = input("Enter your email\n>>")
age = int(input("Enter your age\n>>"))

create_user(name=name, age=age, email=email)


# H. Create a function generate_invoice that generates an invoice for a customer's 
# purchase. The function should take the customer's name and purchase amount as 
# required arguments, with an optional discount as a keyword argument. Calculate 
# the final amount after applying the discount if provided.

def generate_invoice(customer_name, purchase_amount, discount=None):
    discount_amount = purchase_amount * (discount / 100) if discount is not None else 0
    final_amount = purchase_amount - discount_amount

    print(f"Invoice for: {customer_name}\nPurchase Amount: {purchase_amount}")
    
    if discount is not None:
        print(f"Discount Applied: {discount}%\nDiscount Amount: {discount_amount}")

    print(f"Final Amount: {final_amount}")
    return final_amount

customer_name = "Vusal Gambarov"
purchase_amount = 100.0
discount_percentage = 10.0

final_amount = generate_invoice(customer_name, purchase_amount, discount=discount_percentage)


# I. Create a function create_circle that creates a circle with specified properties 
# (radius and color). Use keyword arguments to allow specifying these properties and 
# validate the input.






# J. Implement a function calculate_score that takes a student's scores in various 
# subjects as keyword arguments and calculates their total score. Use the ** operator 
# to handle an arbitrary number of subject scores.

def calculate_score(**subject_scores):
    total_score = sum(subject_scores.values())
    return total_score

math_score = 90
english_score = 85
science_score = 92

total = calculate_score(math=math_score, english=english_score, science=science_score)
print(f"Total Score: {total}")



# K. Write a function calculate_volume that calculates the volume of a cylinder using 
# its radius and height. Use keyword arguments for the radius and height.

import math

def calculate_volume(**kwargs):
    radius = kwargs.get('radius', 1.0)
    height = kwargs.get('height', 1.0)

    if not all(isinstance(val, (int, float)) and val > 0 for val in [radius, height]):
        raise ValueError("Radius and height must be positive numbers.")

    volume = math.pi * radius**2 * height
    return volume

try:
    cylinder_volume = calculate_volume(radius=3.0, height=5.0)
    print(f"Volume of the cylinder: {cylinder_volume:.2f} cubic units")
except ValueError as e:
    print(f"Error: {e}")



# L. Create a function print_person_info that takes a person's name as a positional 
# argument and their age and city as keyword arguments. Print the person's name, age, and city.

def person_info(name, age, city):
    print(f"User info -- name : {name}, age : {age}, city : {city}.")
    
person_info("Rick", age=25, city="New-York")


# M. Implement a function show_order_details that takes the order number as a positional argument, 
# followed by a dictionary of order items as keyword arguments. Print the order number and the 
# items in the order.

def show_order_details(order_number, **kwargs):
    print(f"Order number : {order_number}")
    for item, quantity in kwargs.items():
        print(f"Ordered item : {item}, amount : {quantity}")
        
order_no = 46849848
ordered_items = {
    "Steak burger": 3,
    "Chicken wrap": 1,
    "Falafel": 1   
}

show_order_details(order_no, **ordered_items)


# N. Write a function that checks whether the given pattern from the user is a substring of
# the 'Cybersecurity in Programming' phrase.

def check_substring(phrase, pattern):
    return pattern.lower() in phrase.lower()

phrase = "Cybersecurity in Programming"
pattern = input("Enter the word\n>>")

result = check_substring(phrase=phrase, pattern=pattern)

if result:
    print("Substring")
else:
    print("Not a substring")



# O. Write a function that raises all numbers from the passed list to the power of two.

def raise_to_power(*args):
    return [num**2 for num in args]

numbers = [2, 3, 4, 5]
result = raise_to_power(*numbers)

print("Original Numbers:", numbers)
print("Squared Numbers:", result)



# - Lambda Functions -
# A. Write a brief explanation of what a lambda function is and when it's useful.

"""
A lambda function in programming refers to an anonymous, inline function defined
using the lambda keyword. Unlike regular functions defined with the def keyword, 
lambda functions are typically used for short, simple operations and are often
employed in situations where a full function definition is unnecessary. 
"""

# B. Create a lambda function that adds two numbers and test it with example inputs.

add_numbers = lambda x, y: x + y
result = add_numbers(10, 15)
print(result)

# C. Create a lambda function that squares a given number and test it with example inputs.

square = lambda x: x**2
result = square(10)
print(result)

# D. Create a lambda function that takes three parameters (a, b, c) and calculates 'a x b + c'.

math_operation = lambda a, b, c: (a * b + c)
result = math_operation(3, 5, 7)
print(result)

# E. Create a lambda function that reverses a given string and test it with example inputs.

backwards = lambda x: "".join(reversed(x))
reversed_str = backwards("Hello World!")
print(reversed_str)

# F. Create a lambda function that capitalizes the first letter of a string and test it with 
# example inputs.

capitalize_first_letter = lambda x: x.capitalize()
result = capitalize_first_letter("ne var ne yox")
print(result)

# G. Create a lambda function that counts the number of vowels (a, e, i, o, u) in a given 
# string and test it with example inputs.
# H. Create a lambda function that counts the number of words in a given string and test it 
# with example inputs.


"""
Quiz.
1. What is a lambda function in Python?
    a) A named function defined using the lambda keyword.****
    b) An anonymous function defined using the def keyword.
    c) A function that can take multiple arguments.
    d) A function that returns multiple values.

2. Which of the following is a benefit of using a lambda function?
    a) It allows for complex logic and multiple statements.
    b) It can be assigned a name for reusability.
    c) It is ideal for simple, one-line operations.****
    d) It can accept an arbitrary number of arguments.

3. In Python, which type of argument requires the caller to provide a value when calling a function?
    a) Default argument
    b) Keyword argument
    c) Positional argument****
    d) Lambda argument

4. What will the following code output?
    def multiply(a, b=2):
        return a * b

    result = multiply(3)
    print(result)

    a) 6****
    b) 9
    c) 3
    d) Error

5. Which of the following is a valid usage of a lambda function?
    a) Sorting a list of integers****
    b) Creating a dictionary
    c) Defining a class
    d) Iterating over a list
    
6. In Python, what will the len() function return for the string "hello"?
    a) 5****
    b) 6
    c) 4
    d) 7

7. What is the purpose of a function in Python?
    a) To store variables.
    b) To perform a specific task or set of tasks.****
    c) To declare classes.
    d) To handle exceptions.

8. Which of the following is true about functions in Python?
    a) A function can only be defined using the def keyword.
    b) A function can return multiple values.****
    c) A function cannot call other functions.
    d) A function can only accept a single argument.

9. What is the output of the following code?
    def greet(name):
        return f"Hello, {name}!"

    message = greet("Alice")
    print(message)

    a) "Hello, Alice!"****
    b) "Hello, name!"
    c) Error
    d) "Hello, world!"

10. Which of the following statements about keyword arguments is true?
    a) Keyword arguments must always come before positional arguments.
    b) Keyword arguments are specified using the key keyword.
    c) Keyword arguments provide a default value if not provided by the caller.****
    d) Keyword arguments are mandatory.

11. What is the purpose of the *args parameter in a function definition?
    a) To specify keyword arguments.
    b) To specify default values for arguments.
    c) To allow the function to accept an arbitrary number of positional arguments.****
    d) To allow the function to accept an arbitrary number of keyword arguments.

12. In a lambda function, what does 'x' represent?
    a) The function itself.
    b) The argument being passed to the function.****
    c) The return value of the function.
    d) The number of arguments the function can accept.

13. What will the following code output?
    text = "hello lambda"
    reverse_text = (lambda x: x[::-1])(text)
    print(reverse_text)

    a) "adbmal olleh"****
    b) "ambda"
    c) "ah"
    d) Error

14. What is a default parameter in a function?
    a) A parameter that is automatically assigned a value if no value is provided by the caller.****
    b) A parameter that must always be specified by the caller.
    c) A parameter that has a fixed value and cannot be changed.
    d) A parameter that is only used for keyword arguments.

15. In which situation would using default parameters be most beneficial?
    a) When you want to ensure a parameter is always provided by the caller.
    b) When you want to assign a specific value to a parameter unless the caller provides a different value.****
    c) When you want to use a different function depending on the provided parameters.
    d) When you want to force the caller to use only keyword arguments.
    
16. What is the main difference between positional and keyword arguments in Python?
    a) Positional arguments are provided by specifying the argument value only, *****
    while keyword arguments are specified with the parameter name and value.
    b) Positional arguments are mandatory, while keyword arguments are optional.
    c) Positional arguments can be specified using the args keyword, while keyword 
    arguments use the kwargs keyword.
    d) Positional arguments can only be used for functions with a single parameter.
    
17. When should you use positional arguments over keyword arguments?
    a) When you want to provide arguments in a specific order.*****
    b) When you want to ensure that the caller always provides a value for that argument.
    c) When you want to allow the caller to provide arguments in any order.
    d) When you want to provide a default value for an argument.
"""
# """
# - Functions -
# A. Define a function greet_with_message that takes a username and a 
# message (with a default value of "Hello") as parameters and prints 
# the message along with the username.

def greet_with_message(name, message):
    print(f"{name}, {message}")
    
user_name = input("Enter your name>>")
greeting = "Good morning!"

greet_with_message(user_name, greeting)

# B. Write a function calculate_discount that calculates the discounted 
# price of an item based on the original price and a discount rate 
# (default to 10%). Return the discounted price.

def calculate_discount(price, discount):
    final_cost = price - (price * (discount / 100))
    return final_cost
try:
    retail_price = float(input("Enter the original price>>"))
    deduction = float(input("Enter the discount percentage>>"))
    
    total_amount = calculate_discount(retail_price, deduction)
    print(total_amount)
    
except ValueError:
    print("Enter valid numeric price and discount.")

# C. Create a function sum_all that takes any number of arguments using 
# the asterisk operator in the parameter definition and returns the sum 
# of all the arguments.

def sum_all(*numbers):
    return sum(numbers)
   
numbers = 34, 34, 34
result = sum_all(*numbers)
print(result)

# D. Write a function calculate_product that takes at least two arguments
# and calculates their product. Use the asterisk operator in the parameter 
# definition to handle multiple arguments.

def calculate_product(*args):
    product = 1
    for n in args:
        product *= n
        
    return product

result = calculate_product(2, 3, 4)
print(result)

# E. Write a function sum_of_numbers that takes a variable number of integers
# as parameters and returns their sum.

def sum_of_numbers(*args):
    return sum(args)

try:
    user_nums = input("Enter numbers separated by comma>>")
    numbers = [int(num) for num in user_nums.split(",") ]
    result = sum_of_numbers(*numbers)
    print(result)
    
except ValueError:
    print("Enter the numbers in valid format!")

# F. Create a function calculate_power that takes two parameters: a base number
# and an exponent, and returns the result of raising the base to the given exponent.

def calculate_power(a, b):
    return a**b
try:
    base_num = int(input("Enter the base number>>"))
    exponent = int(input("Enter the exponent>>"))
    result = calculate_power(base_num, exponent)
    print(f"Result is {result}")
except ValueError:
    print("Enter appropriate integers")

# G. Define a function named greet_user that takes a parameter username and prints 
# a greeting message like: "Hello, [username]!".

def greet_user(name):
    print(f"Hello {name}!")
    
user_name = input("Enter your name>>")
greet_user(user_name)

# H. Write a function called calculate_area that takes the radius of a circle as a 
# parameter and returns the area of the circle.

from math import pi


def calculate_area(r):
    area = pi * (r ** 2)
    return area

try:
    radius = float(input("Enter the radius of the circle>>"))
    circle_area = calculate_area(radius)
    print(circle_area)   
except ValueError:
    print("Please enter valid value for radius")

# I. Create a function average that takes a list of numbers as a parameter and calculates 
# the average of those numbers.

def average(item):
    average = sum(item) / len(item)
    return average

num_lst = [10, 10, 10, 10]

final_result = average(num_lst)
print(final_result)

# J. Implement a function maximum_number that takes a variable number of integers as 
# parameters and returns the largest number.

def maximum_number(*numbers):
    return max(numbers)

nums = 23, 65, 77, 100, 32
largest_num = maximum_number(*nums)
print(largest_num)

# K. Define a function greet_with_salutation that takes a username and a salutation 
# (with a default value of "Mr.") as parameters and prints a greeting using the provided salutation.

def greet_with_salutation(name, salut="Mr."):
    print(f"Good morning {salut} {name}")

while True:
    full_name = input("Enter your name and surname\n>> ").title()
    salutation = input("Choose the title (Mr., Mrs., or Ms.): ").capitalize()

    if salutation in ["Mr.", "Mrs.", "Ms."]:
        break
    else:
        print("Invalid salutation. Please choose from Mr., Mrs., or Ms.")

greet_with_salutation(name=full_name, salut=salutation)


# L. Write a function calculate_cost that calculates the total cost of purchasing a
# given quantity of items, considering a unit price and tax rate (default tax rate is 5%).


def calculate_cost(quantity, price, tax=0.05):
    return quantity * price * (1 + tax)

try:
    price = float(input("Enter the price of the product: "))
    quantity = float(input("Enter the quantity: "))

    tax_percent = float(input("Enter the tax amount: "))
    tax_num = tax_percent / 100

    final_amount = calculate_cost(quantity, price, tax_num)

    print(f"Total amount is {final_amount}")

except ValueError:
    print("Enter proper values to needed spaces!")

# M. Create a function concatenate_strings that takes a variable number of strings as parameters 
# and concatenates them into a single string, separated by spaces.

def concatenate_strings(*args):
    return " ".join(args)


user_str = "Hello", "World!"
combined_str = concatenate_strings(*user_str)
print(combined_str)

# N. Write a function calculate_sum_and_product that takes at least two numbers as arguments 
# and returns both their sum and product. Use the asterisk operator in the parameter definition 
# to handle multiple arguments.

from functools import reduce

def calculate_sum_and_product(*numbers):
    product = reduce(lambda x, y: x*y, numbers)
    print(f"Product of numbers : {product}")
    print(f"Sum of the numbers : {sum(numbers)}")
    
numbers = 1, 2, 3, 4, 5

calculate_sum_and_product(*numbers)

# O. Write a function find_max_min that takes a list of numbers as a parameter and returns both 
# the maximum and minimum numbers from the list. Use if statements to handle edge cases.

def find_max_min(numbers: list):
    max_value = max(numbers)
    min_value = min(numbers)
    
    return max_value, min_value

numbers = [3, 5, 12, 56, 101]

max_number, min_number = find_max_min(numbers)

print(f"Maximum value is {max_number}")
print(f"Minimum value is {min_number}")

# P. Create a function calculate_grade that takes a student's numerical score as a parameter and
# returns their corresponding letter grade based on the following scale:
# 90-100: 'A'
# 80-89: 'B'
# 70-79: 'C'
# 60-69: 'D'
# Below 60: 'F'
# Handle any invalid scores (less than 0 or greater than 100) by returning 'Invalid Score'.


def calculate_grade(score):
    if score > 100 or score < 0:
        print("Invalid score!")
        exit()
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
    
num_score = int(input("Enter your score between 0 and 100\n>>"))
letter_grade = calculate_grade(num_score)
print(f"Your grade is {letter_grade}.")



"""Bu ikinci bilmirem qaydalara ne derecede uygundu"""

def calculate_grade(score):
    if not 0 <= score <= 100:
        print("Invalid score")
        exit()
        
    return (
        "A" if score >= 90 else "B" if score >= 80 else 
        "C" if score >= 70 else "D" if score >= 60 else "F"
        )


num_score = int(input("Enter your score between 0 and 100:\n>> "))
letter_grade = calculate_grade(num_score)
print(f"Your grade is {letter_grade}.")


# Q. Write a function solve_quadratic that takes the coefficients of a quadratic equation 
# (a, b, c) as parameters and returns the real roots (if any) of the quadratic equation. 
# Use the quadratic formula.
"""Bu kod copy paste koddu. Men hara kvadrat tenlik hara"""
import math

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Check if the discriminant is non-negative for real roots
    if discriminant >= 0:
        # Calculate the two roots using the quadratic formula
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        
        # Return the real roots
        return root1, root2
    else:
        # If discriminant is negative, no real roots exist
        return None

# Example usage:
a = 1
b = -3
c = 2

roots = solve_quadratic(a, b, c)

if roots:
    print("Real roots:", roots)
else:
    print("No real roots exist.")


# R. Implement a function is_palindrome that takes a string as a parameter and returns True
# if the string is a palindrome (reads the same forwards and backwards), and False otherwise.

def check_palindrome(item: str):
    return item == item[::-1]

word = input("Enter the word you want to check:\n>>").strip().lower()

is_palindrome = check_palindrome(word)

if is_palindrome:
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")



# S. Create a function sort_numbers that takes three numbers as parameters and returns them in 
# ascending order as a tuple.

def sort_numbers(a, b, c):
    numbers = sorted((a, b, c))
    return tuple(numbers)
    
nums = sort_numbers(9, 8, 7)
print(nums)

# T. Write a function calculate_tax that takes an income amount and a tax rate as parameters 
# and calculates the tax amount. Return a tuple containing the tax amount and the net income 
# (income after tax).

def calculate_tax(income, tax):
    net_income = income - tax
    tax_rate = (tax / income) * 100
    
    return net_income, tax_rate

brutto_income = float(input("Enter your income before tax\n>>"))
tax_deduction = float(input("Enter the amount deducted as tax\n"))


result = calculate_tax(income=brutto_income, tax=tax_deduction)
print(result)


# U. Create a function calculate_discounted_price that takes the original price and a discount 
# percentage as parameters. Return a tuple containing the discounted price and the amount saved.

def calculate_discounted_price(original_price, discount_percent):
    saved_amount = (original_price / 100) * discount_percent
    discounted_price = original_price - saved_amount
    
    return discounted_price, saved_amount # tuple returned

try:
    price = float(input("Enter the price of the item\n>>"))
    discount = float(input("Enter the discount percentage\n>>"))
    end_price, saved_amount = calculate_discounted_price(price, discount)
    print(f"Price after discount is {end_price}. You saved {saved_amount} USD.")
    
except ValueError:
    print("Enter proper values for calculation")


"""
Quiz.
1. What does the following function do?
    def greet_user(username):
        print("Hello, " + username + "!")

    a) Greets the user with a customized message.****
    b) Prints "Hello, user!".
    c) Defines a function but doesn't execute any action.
    d) Raises an error due to an invalid function definition.

2. Which of the following functions best describes the calculations of the area of a circle?
    a) calculate_circle_area(radius)****
    b) compute_circle_area(diameter)
    c) get_circle_area(radius)
    d) calculate_area_circle(radius)

3. What is the purpose of a default parameter in a function?
    a) It ensures the function returns a default value.
    b) It allows the function to have optional parameters.****
    c) It restricts the function to accept a specific type of argument.
    d) It is used to specify the default return value of the function.

4. In Python, how do you pass a variable number of arguments to a function?
    a) Using lists as arguments
    b) Using tuples as arguments
    c) Using the asterisk (*) operator in the parameter definition****
    d) Using the exclamation mark (!) in the parameter definition

5. Which of the following functions best describes the calculations of the sum of a list of numbers?
    a) sum_list(numbers)
    b) calculate_sum(numbers)****
    c) add_numbers(*numbers)
    d) sum_all(*numbers)

6. What does the asterisk (*) operator do in the function definition?
    a) Multiplies the function's output by the provided argument.
    b) Allows the function to take a variable number of arguments.****
    c) Raises an error due to an invalid operator usage.
    d) Converts the argument to a string before passing it to the function.

7. Consider the following function:
    def greet_user(username="Guest"):
        print("Hello, " + username + "!")

    What is the default value for the username parameter in this function?
    a) "Guest"****
    b) "User"
    c) None
    d) "Hello"

8. In the following function, what happens if no value is provided for the message parameter?
    def greet_with_message(username, message="Hello"):
        print(message + ", " + username + "!")

    a) The function raises an error.
    b) The function uses the default value "Hello" for the message.****
    c) The function uses the default value "World" for the message.
    d) The function uses the default value "Hi" for the message.

9. Which of the following is a valid function definition using default parameters?
    a) def calculate_area(radius, pi=3.14159):****
    b) def calculate_area(pi=3.14159, radius):
    c) def calculate_area(radius=, pi=3.14159):
    d) def calculate_area(radius=3.14159, pi):

10. Consider the function below:
    def calculate_discount(price, discount_rate=0.1):
        return price * (1 - discount_rate)

    What is the default discount rate used if not provided?
    a) 10%****
    b) 20%
    c) 5%
    d) 15%

11. Given the function:
    def multiply(a, b=2):
        return a * b

    If we call multiply(5), what will be the result?
    a) 10****
    b) 5
    c) 7
    d) 15

12. In the following function definition, what does the * represent?
    def display_names(*names):
        for name in names:
            print(name)

    a) It denotes multiplication in the function.
    b) It allows passing a variable number of names as arguments.****
    c) It signifies that 'names' is a string.
    d) It raises an error in the function.

13. Given the function below:
    def greet_with_messages(*messages):
        for message in messages:
            print(message)

    If we call greet_with_messages("Hello", "Bonjour", "Hola"), how many messages will be printed?
    a) 3*****
    b) 2
    c) 1
    d) 0

14. Consider the function definition:
    def generate_pattern(symbol='*', count=5):
        return symbol * count

    If we call generate_pattern(count=3), what will be the result?
    a) '***'  <--------
    b) '***'  <--------
    c) '**'
    d) '*****'

15. You have a list of numbers: [12, 5, 78, 43, 67, 89, 45, 23]. What will the function find_max_min return for this list?
    a) (12, 5)
    b) (5, 89) Bu da ola biler
    c) (5, 12)
    d) (89, 5)  Bu da ola biler. Funksiya nece qurulub bilinmir

16. If the score provided to the function calculate_grade is 75, what will be the output of the function?
    a) 'C'
    b) 'B'          kod yoxdu
    c) 'D'
    d) 'F'     
   
17. For the quadratic equation with coefficients a=1, b=-5 and
c=6, what will the function solve_quadratic return?
    a) (-2, 3)
    b) (-3, 2)
    c) (2, 3)
    d) (-2, -3)

18. If the input string to the function is_palindrome is "radar", 
what will the function return?
    a) True****
    b) False
      
19. For the input numbers 5, 2, 8, what will be the output of the function sort_numbers?
    a) (2, 5, 8)****
    b) (8, 5, 2)
    c) (5, 2, 8)
    d) (2, 8, 5)

20. If the income is $5000 and the tax rate is 20%, what will be the output of 
the function calculate_tax?
    a) (1000, 4000)
    b) (4000, 1000)****
    c) (2000, 3000)
    d) (2500, 2500)

21. If the original price is $100 and the discount rate is 25%, what will be the 
output of the function calculate_discounted_price?
    a) (75.0, 25.0)****
    b) (25.0, 75.0)
    c) (100.0, 25.0)
    d) (75.0, 100.0)
"""
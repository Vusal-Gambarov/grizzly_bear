# """
# - Map -
# A. Create a function that takes a list of numbers and uses the map() function to 
# double each number in the list.

num_list = [1, 2, 3, 4, 5]
my_func = lambda x: x * 2
new_list = list(map(my_func, num_list))
print(new_list)

# B. Write a function that takes a list of temperatures in Celsius and uses map() 
# to convert them to Fahrenheit using the appropriate conversion formula.

celcius = [25, 17, 33, 21, 30]
func = lambda x: (x * 9/5) + 32
fahrenheit = list(map(func, celcius))
print(fahrenheit)

# C. Implement a function that takes a list of numbers and uses the map() function to 
# calculate the square root of each number.

from math import sqrt


numbers = [25, 49, 64, 36, 100]
func = lambda x: sqrt(x)
root_lst = list(map(func, numbers))
print(root_lst)

# D. Write a function that takes a list of names and uses map() to format them as "Hello, {name}!".

def modify_with_greeting(names):
    formatted_names = map(lambda n: f"Hello, {n}!", names)
    return list(formatted_names)


names = ["Vusal", "Tural", "Natiq"]
greet = modify_with_greeting(names)
for i in greet:
    print(i)

# E. Create a function that takes a list of numbers and uses the map() function to generate a 
# power series for each number, up to a specified exponent.

def generate_powered_numbers(numbers):
    pow_nums = list(map(lambda x: [x ** n for n in range(5)], numbers))
    return pow_nums

nums = [1, 2, 3, 4, 5]
modified_nums = generate_powered_numbers(nums)
print(modified_nums)

# F. Write a function that takes two lists of strings and uses map() to concatenate the elements 
# of the same index from both lists.

def concatenate_strings(names, surnames):
    full_names = map(lambda x, y: (x + " " + y) , names, surnames)
    return list(full_names)

names = ["Lale", "Roman", "Emil", "Nigar"]
surnames = ["Huseynova", "Musayev", "Recebov", "Refibeyli"]

combined_strings = concatenate_strings(names=names, surnames=surnames)
print(combined_strings)

# G. Create a function that takes a list of floats and uses the map() function to round each float 
# to a specified number of decimal places.

def round_floats(numbers, decimal_places):
    rounded_numbers = map(lambda x: round(x, decimal_places), numbers)
    # rounded_numbers = map(lambda x: "{:.2f}".format(x), numbers)
    return list(rounded_numbers)

decimal_places = 2
numbers = [3.1415, 5.679586, 8.65468, 6.68486]
result = round_floats(numbers=numbers, decimal_places=decimal_places)
print(result)


# H. Write a function that takes a list of prices and uses map() to apply a discount percentage to each price.

def apply_discount(prices, discount):
    discounted_price = map(lambda x: x - (x * discount), prices)
    return list(discounted_price)

prices = [100, 200, 300]
discount_percentage = 20 
discount = discount_percentage / 100

end_prices = apply_discount(prices, discount)
print(end_prices)

# I. Implement a function that takes a list of sentences and uses map() to encrypt each sentence using 
# a simple encryption algorithm.

def encrypt_sentence(sentence):
    encrypted = "".join(chr(ord(char) + 1) for char in sentence)
    return encrypted

def implement_encryption(sentence_list):
    encrypted_list = list(map(encrypt_sentence, sentence_list))
    return encrypted_list

sentences = ["Hello, world!", "This is a test sentence.", "Encryption example."]
encrypted_sentences = implement_encryption(sentences)

print("Original Sentences:", sentences)
print("Encrypted Sentences:", encrypted_sentences)

# J. Create a function that takes a list of words and uses map() to count the number of vowels in each word.

def count_vowels(words):
    vowels = ["a", "e", "o", "u", "i"]
    count = sum(1 for char in words if char.lower() in vowels)
    return count
       
words =["Python ", "Javascript", "Kotlin"]
vow_count = list(map(count_vowels, words))
print(vow_count)

# K. Write a function that takes a list of strings and uses map() to return a list of lengths for each string.

def calculate_word_lengths(words):
    word_lengths = list(map(len, words))
    # word_lengths = list(map(lambda x: len(x), words)) ------ ikinci variant
    return word_lengths

word_list = ["Python", "Django", "Flask"]
word_lengths = calculate_word_lengths(words=word_list)
print("Word Lengths:", word_lengths)


# - Filter -
# A. Create a function that takes a list of numbers and uses the filter() function to 
# return a new list containing only the even numbers.

def filter_even(numbers):
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    return even_numbers

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = filter_even(number_list)
print(even_nums)

# B. Write a function that takes a list of numbers and uses the filter() function to 
# return a new list containing only the prime numbers.

def is_prime(number):
    if number < 2:
        return False
    
    for n in range(2, int(number**0.5)+1):
        if number % n == 0:
            return False
    return True

def filter_prime_numbers(numbers):
    prime_nums = list(filter(is_prime, numbers))
    return prime_nums

numbers_list = [-1, 0, 2, 3, 5, 7, 11, 13, 19, 23, 4, 6, 8, 9]
prime_numbers = filter_prime_numbers(numbers_list)
print(prime_numbers)

# C. Implement a function that filters a list of strings to return a new tuple containing 
# only the words that are palindromes.

def is_palindrome(word):
    return word.lower() == word.lower()[::-1]

def filter_palindrome_words(words):
    filtered_words = tuple(filter(is_palindrome, words))
    return filtered_words

words = ["Civic", "madam", "Kayak", "Python", "Django"]
palindrome_words = filter_palindrome_words(words)
print(palindrome_words)

# D. Given a list of dictionaries representing employees and their salaries, use filter() 
# to create a new list of employees whose salary is above a specified threshold.

def filter_by_salary_threshold(employee):
    threshold = 1500
    return employee["salary"] > threshold

employees = [
    {"name": "Mark", "salary": 1800},
    {"name": "Jonas", "salary": 2200},
    {"name": "Sarah", "salary": 1300},
    {"name": "Aydan", "salary": 1350}
]

filtered_employees = list(filter(filter_by_salary_threshold, employees))
print(filtered_employees)


# E. Write a function that takes a list of file names and filters it to return a new list 
# containing only files with a specified file extension.

def filter_files(file_list, extension):
    selected_files = filter(lambda file: file.endswith(extension), file_list)
    return list(selected_files)

files = ["students.txt", "Invoice.pdf", "main.py", "test.py"]
desired_extension = ".py"

new_files_list = filter_files(files, desired_extension)
print(new_files_list)

# F. Create a function that takes a dictionary of student names and their corresponding grades, 
# and uses filter() to return a new dictionary containing only students who passed (grades above 
# a certain threshold).

def filter_passed_students(students, threshold):
    passed_students = filter(lambda item: item[1] >= threshold, students.items())
    return dict(passed_students)

students_grades = {
    "Alice": 80,
    "Bob": 65,
    "Nermin": 90,
    "Elcin": 55,
    "Lale": 75
}
threshold_grade = 70

passed_students = filter_passed_students(students_grades, threshold_grade)
print(passed_students)

# G. Implement a function that takes a mixed list of data types (integers, strings, floats) and 
# filters it to return separate lists for each data type.

def filter_data_types(items):
    int_numbers = list(filter(lambda x: isinstance(x, int), items))
    fl_numbers = list(filter(lambda x: isinstance(x, float), items))
    str_objects = list(filter(lambda x: isinstance(x, str), items))
    
    return int_numbers, fl_numbers, str_objects

mixed_list = [1, "hello", 3.14, "world", 42, 2.718]
integers, floats, strings = filter_data_types(mixed_list)
print(integers, floats, strings)



# H. Prompt the user to enter a condition, then use the filter() function to filter a given list 
# of numbers based on the user-provided condition.

condition = input("Define the condition for filtering(for example : x > 5)>>")
numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
try:
    filtered_numbers = list(filter(lambda x: eval(condition), numbers))
    print(filtered_numbers)
except NameError:
    print("Please enter proper values")

# I. Write a function that takes a list of strings and filters it to return a new list containing 
# only strings that contain a specific substring.

def filter_substring(words, substring):
    new_list = list(filter(lambda x: substring in x, words))
    return new_list

words = ["programming", "rafting", "book", "football"]
substring = "ing"

filtered_strings = filter_substring(words=words, substring=substring)
print(filtered_strings)

# J. Implement a function that takes a list of strings and filters it to return a new list containing 
# strings with a specified character appearing a certain number of times.

def filter_by_character_count(words, char, count):
    filtered_list = list(filter(lambda x: x.lower().count(char) >= count, words))
    return filtered_list

words = ["Banana", "Pinapple", "Pomegranate", "Cherry", "Alma"]
char = "a"
count = 2

new_list = filter_by_character_count(words, char, count)
print(new_list)


# K. Create a function that takes a list of integers and uses the filter() function to return a 
# new list containing only those numbers for which a specified mathematical function (e.g., square, 
# cube) yields a prime result.





# L. Write a function that takes a list of date objects and filters it to return a new list containing 
# dates within a specified range.


from datetime import datetime

def filter_dates(date_list, start_date, stop_date):
    filtered_dates = (list(filter(lambda date: start_date
                     <= date <= stop_date, date_list)))
    
    return filtered_dates
    
dates = [datetime(2024, 2, 24), datetime(2023, 12, 31), datetime(2024, 1, 1)]
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 2, 28)

filtered_dates = filter_dates(dates, start_date, end_date)
print(filtered_dates)


# M. Given a list of cities and their corresponding countries, use filter() to return a new list 
# containing cities from a specific country.

def filter_the_cities(cities_list, country):
    modified_list = list(filter(lambda city: city[1] == country, cities_list))
    return modified_list

cities = [
    ("New York", "USA"),
    ("Boston", "USA"),
    ("Tokyo", "Japan"),
    ("London", "UK"),
    ("Berlin", "Germany"),
    ("Los Angeles", "USA")   
]

target_country = "USA"
new_cities = filter_the_cities(cities, target_country)
print(new_cities)


# N. Create a function that takes a list of product objects and uses the filter() function to return a 
# new list containing only available products.

def filter_available_products(product_list):
    in_stock = list(filter(lambda product: product[1] > 0, product_list))
    return in_stock

products = [
    ("Iphone 15", 10),
    ("Playstation 5", 0),
    ("Galaxy S23", 4),
    ("MacBook Pro", 0)
]

filtered_items = filter_available_products(products)
print(filtered_items)

# O. Implement a function that takes a list and uses filter() to return a new list containing only 
# the unique elements.

def filter_unique_elements(numbers):
    filtered_list = list(filter(lambda x: numbers.count(x) == 1, numbers))
    return filtered_list

num_list = [1, 1, 3, 3, 6, 7, 7, 8, 10]
new_numbers = filter_unique_elements(num_list)
print(new_numbers)


# P. Write a function that takes a list of words and filters it to return a new list containing only 
# anagrams of a specified word.






# Q. Given a list of numeric data, use filter() to return a new list containing elements within a 
# specified range.


def filter_by_range(numbers, min_range, max_range):
    filtered_nums = list(filter(lambda x: min_range <= x <= max_range, numbers))
    return filtered_nums

numbers = [1, 5, 10, 12, 14, 18, 22]
low_limit = 10
up_limit = 20

range_numbers = filter_by_range(numbers, low_limit, up_limit)
print(range_numbers)

# R. Create a function that takes a list of strings and uses filter() to return a new list containing 
# only strings that match a specific regular expression.


def filter_by_substring(strings, substring):
    filtered_strings = list(filter(lambda x: substring in x, strings))
    
    return filtered_strings

string_list = ["apple", "banana", "cherry", "date", "kiwi", "orange"]
substring = "ban"

result = filter_by_substring(string_list, substring)
print(result)



# - Reversed -
# A. Write a function that takes a list of elements and uses the reversed() function to reverse the 
# order of elements in the list.

def reverse_the_order(items):
    return list(reversed(items))

names = ["Vusal", "Tural", "Natiq"]
names_reversed = reverse_the_order(names)
print(names_reversed)

# B. Create a function that takes a string and uses reversed() to reverse the characters in the string.

def reverse_characters(item):
    reversed_item = "".join(reversed(item))
    return reversed_item

name = "Vusal"
name_reversed = reverse_characters(name)
print(name_reversed)

# C. Implement a function that takes a tuple and uses reversed() to reverse the order of elements in the tuple.

def reverse_tuple_elements(items):
    return tuple(reversed(items))

items = (15, True, False, "Sunflower")
reversed_items = reverse_tuple_elements(items)
print(reversed_items)

# D. Write a function that takes a sentence and uses reversed() to reverse the order of words in the sentence.

def reverse_the_sentence(sentence):
    new_order = reversed(sentence.split())
    reversed_sentence = " ".join(new_order)
    
    return reversed_sentence

sentence = "Although coding is fun, it can be hard sometimes"
result = reverse_the_sentence(sentence)
print(result)


# E. Create a function that takes a dictionary and uses reversed() to reverse the order of keys and values.

def reverse_dictionary(students):
    reversed_data = dict(reversed(item) for item in students.items())
    return reversed_data

students = {
    "Lale": 25,
    "Roman": 23,
    "Tural": 29,
    "Nigar": 24
}

result = reverse_dictionary(students)
print(result)


# F. Implement a function that takes a linked list and uses reversed() to reverse the order of nodes in the linked list





# G. Write a function that takes a queue and uses reversed() to reverse the order of elements in the queue.




# H. Create a function that takes a stack and uses reversed() to reverse the order of elements in the stack.





# I. Implement a function that takes a list of elements and uses reversed() to reverse the elements at odd 
# indices, while keeping the elements at even indices unchanged.

def reverse_elements_at_odd_indices(input_list):
    reversed_odd_indices = list(reversed(input_list[1::2]))

    for i, reversed_element in enumerate(reversed_odd_indices):
        input_list[2*i + 1] = reversed_element

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original List:", my_list)
reverse_elements_at_odd_indices(my_list)
print("Modified List:", my_list)


# J. Write a function that takes a binary number as a string and uses reversed() to reverse the binary digits.

def reverse_binary(binary_str):
    binary_list = list(binary_str)
    reversed_binary_list = list(reversed(binary_list))
    reversed_binary_str = "".join(reversed_binary_list)

    return reversed_binary_str

binary_number = "1101101"
reversed_binary = reverse_binary(binary_number)
print("Original Binary: ", binary_number)
print("Reversed Binary: ", reversed_binary)



# K. Create a function that takes a 2D matrix and uses reversed() to reverse the rows of the matrix.

def reverse_matrix_rows(matrix):
    reversed_matrix = [list(reversed(row)) for row in matrix]

    return reversed_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

reversed_matrix = reverse_matrix_rows(matrix)

print("Original Matrix:")
for row in matrix:
    print(row)

print("\nReversed Matrix:")
for row in reversed_matrix:
    print(row)


# L. Implement a function that takes a string and uses reversed() to reverse the characters in each substring 
# separated by a specific delimiter.

def reverse_substrings(input_string, delimiter):
    substrings = input_string.split(delimiter)
    reversed_substrings = ["".join(reversed(substring)) for substring in substrings]
    result = delimiter.join(reversed_substrings)

    return result

input_str = "Hello,World!|Python,is,fun"
delimiter = "|"
result = reverse_substrings(input_str, delimiter)
print(result)



# - Sorted -
# A. Write a function that takes a list of numbers and uses the sorted() function to return a new list with 
# the numbers sorted in ascending order.

def ascending_order(number_list):
    number_list = sorted(number_list)
    return number_list

num_list = [3, 1, 9, 4, 11, 23, 5]
sorted_list = ascending_order(num_list)
print(sorted_list)


# B. Create a function that takes a list of numbers and uses the sorted() function to return a new list with 
# the numbers sorted in descending order.

def descending_order(numbers):
    numbers = sorted(numbers, reverse=True)
    return numbers

num_list = [3, 1, 9, 4, 11, 23, 5]
descending_list = descending_order(num_list)
print(descending_list)

# C. Implement a function that takes a list of strings and uses the sorted() function to return a new list 
# with the strings sorted by their lengths.

def sort_by_len(word_list):
    word_list = sorted(word_list, key=len)
    return word_list

words = ["apple", "strawberry", "banana", "kiwi"]
new_list = sort_by_len(words)
print(new_list)


# D. Write a function that takes a list of tuples and uses the sorted() function to return a new list with 
# the tuples sorted based on their second element.

def sort_tuples_by_second_element(tuple_list):
    sorted_list = sorted(tuple_list, key=lambda x: x[1])
    return sorted_list


original_list = [(1, 5), (3, 2), (2, 8), (4, 1)]
sorted_list = sort_tuples_by_second_element(original_list)

print("Original List:", original_list)
print("Sorted List:", sorted_list)

# E. Create a function that takes a dictionary and uses the sorted() function to return a new dictionary 
# with its items sorted by their values.

def sort_dictionary(data):
    data = sorted(data.items(), key=lambda x: x[1])
    return dict(data)

data = {
    "Leman": 35,
    "Leyla": 27,
    "Lale": 30
}

processed_data = sort_dictionary(data)
print(processed_data)


# F. Implement a function that takes a list of strings and uses the sorted() function to return a new list 
# with the strings sorted in a case-insensitive manner.

def case_insensitive_sort(str_lst):
    str_lst = sorted(str_lst, key=lambda x: x.lower())
    return str_lst

word_lst = ["Hello", "kid", "Semed", "logman"]
sorted_list = case_insensitive_sort(word_lst)
print(sorted_list)


# G. Write a function that takes a list of custom objects and uses the sorted() function to return a new list 
# with the objects sorted based on a specified attribute.



# H. Create a function that takes a list of date objects and uses the sorted() function to return a new list 
# with the dates sorted in chronological order.

from datetime import date

def sort_dates(dates):
    sorted_dates = sorted(dates, key=lambda x: x)
    return sorted_dates

date_list = [date(2023, 5, 15), date(2022, 12, 8), date(2024, 2, 21), date(2023, 1, 30)]
sorted_list = sort_dates(date_list)

print("Original dates:", date_list)
print("Sorted dates:", sorted_list)


# I. Implement a function that takes a list of lists and uses the sorted() function to return a new list with 
# the lists sorted based on the sum of their elements.

def sort_by_sum(matrix):
    new_list = sorted(matrix, key=lambda x: sum(x))
    return new_list
    

num_list = [
    [3, 7, 1],
    [8, 2, 5],
    [4, 6, 9],
    [2, 8, 3]
]

processed_list = sort_by_sum(num_list)
print(processed_list)



# J. Write a function that takes a list of integers and uses the sorted() function to return a new list with 
# the integers sorted based on the number of factors they have.

def count_factors(num):
    count = 0
    for n in range(1, num+1):
        if num % n == 0:
            count += 1
    return count

def sort_by_factors(numbers):
    sorted_list = sorted(numbers, key=lambda x: count_factors(x))
    return sorted_list

numbers = [12, 15, 3, 8, 9, 21]
sorted_numbers = sort_by_factors(numbers)
print(sorted_numbers)


# K. Create a function that takes a list of strings and uses the sorted() function to return a new list with 
# the strings sorted based on their last characters.

def sort_by_last_char(words):
    words = sorted(words, key=lambda x: x[-1])
    return words

word_list = ["carb", "civic", "banana", "sad"]
processed_list = sort_by_last_char(word_list)
print(processed_list)


# L. Implement a function that takes a list of dictionaries and uses the sorted() function to return a new list 
# with the dictionaries sorted based on their keys.

def sort_by_key(data):
    data = sorted(data.items(), key=lambda x: x[0])
    return dict(data)

cars = {
    "Volvo": "XC60",
    "Mercedes": "C Class",
    "Audi": "A6",
    "Toyota": "Camry"   
}

sorted_cars = sort_by_key(cars)
print(sorted_cars)


# M. Sort the following list of strings alphabetically by the second letter:
# string_list = ["Hello", "World", "Python", "Programming", "Example", "String", "List", "ChatGPT"]

def sort_by_second_char(item_list):
    item_list = sorted(item_list, key=lambda x: x[1])
    return item_list


string_list = ["Hello", "World", "Python", "Programming", "Example", "String", "List", "ChatGPT"]
sorted_lst = sort_by_second_char(string_list)
print(sorted_lst)



"""
Quiz.
1. What is the purpose of the filter() function in Python?
    A) To remove elements from an iterable based on a given condition****
    B) To sort elements in an iterable
    C) To modify elements in an iterable
    D) To combine elements in an iterable

2. Which of the following data types can the filter() function be applied to?
    A) Lists
    B) Strings
    C) Tuples
    D) All of the above*****

3. What does the filter() function return?
    A) A new iterable containing filtered elements*****
    B) The original iterable with filtered elements
    C) A list of filtered elements
    D) A tuple of filtered elements

4. Which parameter does the filter() function take?
    A) A filter function
    B) An iterable
    C) Both A and B****
    D) Neither A nor B

5. In the context of the filter() function, what does the filter function do?
    A) Defines the condition for filtering elements****
    B) Specifies the data type of the iterable
    C) Sorts the iterable elements
    D) Combines the iterable elements

6. Which of the following statements is true about the filter() function?
    A) The filter function can only return True or False
    B) The filter function can return any data type****
    C) The filter function must return a boolean
    D) The filter function is not required

7. What is the syntax for using the filter() function in Python?
    A) filter(condition, iterable)****
    B) filter(iterable, condition)
    C) filter(function, iterable)
    D) filter(iterable, function)

8. When using the filter() function, what happens if the filter function returns False for an element?
    A) The element is removed from the iterable****
    B) The element is included in the iterable
    C) An error is raised
    D) None of the above

9. Can the filter() function be used to filter elements based on multiple conditions?
    A) Yes****
    B) No

10. In Python 3, what does the filter() function return by default?
    A) A filter object****
    B) A list of filtered elements
    C) A tuple of filtered elements
    D) A set of filtered elements

11. What is the purpose of the map() function in Python?
    A) To apply a given function to each item in an iterable*****
    B) To filter elements from an iterable based on a given condition
    C) To sort elements in an iterable
    D) To combine elements in an iterable

12. Which of the following is an iterable that can be passed to the map() function?
    A) Lists
    B) Strings
    C) Tuples
    D) All of the above****

13. What does the map() function return?
    A) A new iterable containing transformed elements****
    B) The original iterable with transformed elements
    C) A list of transformed elements
    D) A tuple of transformed elements

14. What parameters does the map() function take?
    A) A mapping function and an iterable
    B) A single iterable
    C) A single mapping function
    D) A mapping function, followed by one or more iterables****

15. In the context of the map() function, what does the mapping function do?
    A) Defines the transformation to be applied to each element*****
    B) Specifies the data type of the iterable
    C) Sorts the iterable elements
    D) Combines the iterable elements

16. Which of the following is true about the map() function?
    A) The mapping function can return any data type****
    B) The mapping function must return a boolean
    C) The mapping function is not required
    D) The mapping function must return an integer

17. What is the syntax for using the map() function in Python?
    A) map(mapping_function, iterable)****
    B) map(iterable, mapping_function)
    C) map(function, iterable)
    D) map(iterable, function)    

18. When using the map() function, what happens if the mapping function returns None for an element?
    A) The element is removed from the iterable****
    B) The element remains unchanged in the iterable
    C) An error is raised
    D) None of the above

19. Can the map() function be used to transform elements from multiple iterables?
    A) Yes****
    B) No

20. In Python 3, what does the map() function return by default?
    A) A map object****
    B) A list of transformed elements
    C) A tuple of transformed elements
    D) A set of transformed elements

21. What is the purpose of the reversed() function in Python?
    A) To reverse the order of elements in an iterable****
    B) To sort elements in an iterable
    C) To remove elements from an iterable
    D) To concatenate elements in an iterable

22. Which of the following is an iterable that can be passed to the reversed() function?
    A) Lists
    B) Strings
    C) Tuples
    D) All of the above****

23. What does the reversed() function return?
    A) A new iterable containing reversed elements****
    B) The original iterable with reversed elements
    C) A list of reversed elements
    D) A tuple of reversed elements

24. What parameter does the reversed() function take?
    A) An iterable****
    B) A single element
    C) A number
    D) A mapping function

25. In the context of the reversed() function, what does "reversed elements" mean?
    A) The elements are in the opposite order****
    B) The elements are sorted in ascending order
    C) The elements are concatenated
    D) The elements are multiplied

26. Which of the following is true about the reversed() function?
    A) The reversed elements are returned as a list
    B) The reversed elements are returned as a tuple
    C) The reversed elements are returned as an iterator****
    D) The reversed elements are returned as a set

27. What is the syntax for using the reversed() function in Python?
    A) reversed(iterable)****
    B) iterable.reversed()
    C) reversed(function, iterable)
    D) reversed(iterable, function)

28. When using the reversed() function, can it be applied to strings?
    A) Yes****
    B) No

29. Can the reversed() function be used to reverse a dictionary?
    A) Yes
    B) No****

30. In Python 3, what does the reversed() function return by default?
    A) A reversed object*****
    B) A list of reversed elements
    C) A tuple of reversed elements
    D) A set of reversed elements

31. What is the purpose of the sorted() function in Python?
    A) To sort elements in an iterable and return a sorted list****
    B) To reverse the order of elements in an iterable
    C) To remove elements from an iterable
    D) To concatenate elements in an iterable

32. Which of the following is an iterable that can be passed to the sorted() function?
    A) Lists
    B) Strings
    C) Tuples
    D) All of the above****
    
33. What does the sorted() function return?
    A) A new iterable containing sorted elements
    B) The original iterable with sorted elements
    C) A list of sorted elements****
    D) A tuple of sorted elements

34. What parameters does the sorted() function take?
    A) An iterable****
    B) A single element
    C) A mapping function
    D) A mapping function and an iterable

35. In the context of the sorted() function, what does "sorted elements" mean?
    A) The elements are arranged in ascending order****
    B) The elements are arranged in descending order
    C) The elements are multiplied
    D) The elements are concatenated

36. Which of the following is true about the sorted() function?
    A) The sorted elements are returned as a tuple
    B) The sorted elements are returned as a set
    C) The sorted elements are returned as an iterator
    D) The sorted elements are returned as a list****

37. What is the syntax for using the sorted() function in Python?
    A) sorted(iterable)****
    B) iterable.sorted()
    C) sorted(function, iterable)
    D) sorted(iterable, function)

38. When using the sorted() function, can you specify a custom sorting order?
    A) Yes, by providing a custom sorting function****
    B) No, the sorting order is always ascending
    C) Yes, by providing a reverse parameter
    D) No, the sorting order is always descending

39. Can the sorted() function be used to sort a dictionary based on its keys or values?
    A) Yes****
    B) No

40. In Python 3, what does the sorted() function return by default?
    A) A list of sorted elements****
    B) A sorted object
    C) A tuple of sorted elements
    D) A set of sorted elements
"""
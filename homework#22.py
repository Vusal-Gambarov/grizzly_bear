# """
# - Zip (Parallel Iteration) & Enumerate (Counter) -
# A. Write a program that takes a list and uses the enumerate method to print each 
# element in the list along with its index. Use a suitable formatting for the output.

name_lst = ["John", "Lucas", "Scarlett", "Leyla"]

for idx, name in enumerate(name_lst):
    print(f"Index {idx}  {name}")

# B. Parallelly iterate over the following collections and print the corresponding
# pair values:
# students = ["Namig", "Zaur", "Murad", "Aysel"]
# gifts = ["Book", "Phone", "Car Model", "Bag"]

students = ["Namig", "Zaur", "Murad", "Aysel"]
gifts = ["Book", "Phone", "Car Model", "Bag"]

for student, gift in zip(students, gifts):
    print(f"{student} -- {gift}")

# C. Iterate over sequence of fruits and print the order of each fruit:

fruits = ["Avocado", "Banana", "Kiwi", "Mango"]
for order, fruit in enumerate(fruits, start=1):
    print(f"{order} - {fruit}")


# D. Write a program that takes two lists of equal lengths and uses the zip 
# method to create a list of tuples, where each tuple contains elements from both 
# lists at the corresponding index. Print the resulting list of tuples.

students = ["Namig", "Zaur", "Murad", "Aysel"]
gifts = ["Book", "Phone", "Car Model", "Bag"]

lst = list(zip(students, gifts))
print(lst)

# - Date & Time -
# A. Write a program that prints 'Running...' each 1.5 seconds. The program should
# be terminated after 5 executions of the print statement.

from time import sleep

for _ in range(5):
    sleep(1.5)
    print("Running...")

# B. Write a program that uses the datetime module to display the current date and 
# time in the format "YYYY-MM-DD HH:MM:SS". Print this information to the console.

from datetime import datetime

time = datetime.now()
current_time = time.strftime("%y-%m-%d  %H:%M:%S")
print(current_time)

# C. Write a program that takes a birthdate (year, month, day) and uses the datetime 
# module to calculate the age in years.

from datetime import datetime

current_date = datetime.now()
birthdate = datetime(1987, 10, 18)
age = (current_date.year - birthdate.year - 
       ((current_date.month, current_date.day) 
        < (birthdate.month, birthdate.day)))

print(age)

# D. Write a program calculate_elapsed_time(start_time, end_time) that takes two 
# datetime objects representing a start time and an end time. Calculate and return 
# the elapsed time in hours, minutes, and seconds.

import datetime

def calculate_elapsed_time(start_time, end_time):
    time_difference = end_time - start_time

    hours = time_difference.total_seconds() // 3600
    minutes = (time_difference.total_seconds() % 3600) // 60
    seconds = time_difference.total_seconds() % 60
    
    hours, minutes, seconds = int(hours), int(minutes), int(seconds)
    
    print((f"Elapsed time is {hours} hours, "
           f"{str(minutes).zfill(2)} minutes, "
           f"{str(seconds).zfill(2)} seconds."))

try:
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    start_time = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_time = datetime.datetime.now()
    
    calculate_elapsed_time(start_time, end_time)
    
except ValueError:
    print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")
    exit()

# E. Write a program that takes a year and a month (1-12) as arguments. Use the calendar 
# module to determine and return the number of days in that month.

import calendar

def get_days_in_month(year, month):
    if month < 1 or month > 12:
        return "Invalid month. Please enter a month between 1 and 12."

    days_in_month = calendar.monthrange(year, month)[1]

    return f"The number of days in {calendar.month_name[month]} {year} is {days_in_month}."


year_input = int(input("Enter the year: "))
month_input = int(input("Enter the month (1-12): "))

result = get_days_in_month(year_input, month_input)
print(result)

# F. Write a program that takes a birthdate (as a datetime object) and calculates the time 
# remaining until the next birthday in days, hours, and minutes. Make it in live-clock style.

from datetime import datetime, timedelta
import time

def calculate_time_until_birthday(birthdate):
    today = datetime.now()
    next_birthday = datetime(today.year, birthdate.month, birthdate.day)

    if today > next_birthday:
        next_birthday = datetime(today.year + 1, birthdate.month, birthdate.day)

    return next_birthday - today

def display_live_clock(time_until_birthday):
    while time_until_birthday.total_seconds() > 0:
        time_until_birthday -= timedelta(seconds=1)
        time.sleep(1)
        print(f"Time until next birthday: {time_until_birthday}", end="\r")


birthdate_input = input("Enter your birthdate in the format YYYY-MM-DD: ")
birthdate = datetime.strptime(birthdate_input, "%Y-%m-%d")

time_until_birthday = calculate_time_until_birthday(birthdate)
display_live_clock(time_until_birthday)

# G. Write a program that uses the time module to display the current time. However, 
# add a delay of 5 seconds using time.sleep(5) before displaying the time.

import time

def display_current_time_with_delay():
    print("Waiting for 5 seconds...")
    time.sleep(5)  
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"Current Time: {current_time}")

display_current_time_with_delay()

# H. Write a program that acts as a countdown timer. Prompt the user to enter a time 
# in seconds. Use time.sleep() to create a countdown from the specified time, displaying the 
# remaining seconds at each interval of 1 second.

import os
from time import sleep

def countdown_timer(start: int):
    for n in range(start, -1, -1):
        print(n)
        sleep(1)
        clear_console()

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    try:
        start_num = int(input("Enter the number to countdown>>"))
        if start_num <= 0:
            print("Please enter a positive integer greater than 0.")
        else:
            countdown_timer(start_num)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

main()

# I. Write a program that displays the current time every minute. Use a loop and time.sleep() 
# to achieve this. The program should display the time at each minute interval.

import time
from datetime import datetime

def display_current_time():
    while True:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Current Time: {current_time}")
        time.sleep(60)  


display_current_time()

# J. Write a program that displays a random message every 2 to 5 seconds. Use the random 
# module to select a random message from a predefined list and display it to the

import time
import random

lst = ["Hello", "How are you?", "How is it going?", "Coding is fun"]
iterations = 4

while iterations > 0:
    random_message = random.choice(lst)
    print(random_message)
    time.sleep(random.uniform(2, 5))
    iterations -= 1



# K. Write a program in style of "Squid Game". First, create a list of ten random numbers.
# Then, every 10 seconds remove (kill) the smallest value from the list.




num_list = [ ]

for _ in range(10):
    num_list.append(random.randint(1, 100))
    
print(num_list)

while len(num_list) > 1:
    num_list.remove(min(num_list))
    time.sleep(10)
    print(num_list)
    
    
    




# - Chat GPT's Homework -
# 1. Write a program that uses the zip method to create a new list of tuples,
# where each tuple contains elements from both lists at the corresponding 
# index.

students = ["Namig", "Zaur", "Murad", "Aysel"]
gifts = ["Book", "Phone", "Car Model", "Bag"]

combined_list = list(zip(students, gifts))
print(combined_list)

# 2. Write a program that takes two lists, keys and values and uses the zip 
# method to create a dictionary where the elements from the keys list are the 
# keys and the elements from the values list are the corresponding values. 

students = ["Namig", "Zaur", "Murad", "Aysel"]
gifts = ["Book", "Phone", "Car Model", "Bag"]

student_gift = { }

for key, value in zip(students, gifts):
    student_gift[key] = value
    
print(student_gift)

# 3. Write a program that takes an iterable and an optional starting index 
# (default is 0). Implement the functionality of enumerate using a loop, and 
# return a list of tuples where each tuple contains the index (starting from 
# the provided start) and the corresponding element from the iterable.

def idx_iterable(iterable):
    lst = [ ]
    for idx, item in enumerate(iterable):
        lst.append((idx, item))
    return lst
    
phrase = "Hello World!"

final_lst = idx_iterable(phrase)
print(final_lst)


# 4. Explain the difference between the time() method and the sleep() method 
# in the time module. Provide use cases for each.
"""
time() method returns the current time in seconds since the epoch (January 1, 1970, 00:00:00 UTC).
It is primarily used to measure the current time or to calculate the elapsed time between two events.

sleep() method is used to pause the execution of a program for a specified number of seconds.
It is helpful in introducing delays or creating timed intervals in a program.

"""

import time

current_time = time.time()
time.sleep(2)
print(current_time)





# 5. Describe the purpose and functionality of the strftime() method in the 
# datetime module. Provide an example of how to use it.
""" 
strftime() method in the datetime module in Python is used for formatting date and time objects
into strings based on a specified format. The name "strftime" stands for "string format time
"""

from datetime import datetime

current_datetime = datetime.now()
time = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

print(time)

# 6. Explain the significance of the epoch time (January 1, 1970) and how it's 
# related to the time() method in the time module.
""" 
The epoch time, also known as Unix time or POSIX time, is a system for tracking
time in computing. It represents the number of seconds that have elapsed since 
00:00:00 Coordinated Universal Time (UTC) on Thursday, January 1, 1970 (not counting leap seconds).
This specific moment is referred to as the "epoch."
"""

# 7. What is the purpose of the timedelta class in the datetime module? Provide 
# an example use case where timedelta can be helpful.
""" 

The timedelta class in the datetime module is used to represent a duration of time.
It allows you to perform arithmetic operations with datetime objects, such as addition or
subtraction, to manipulate and calculate differences between dates and times
"""
from datetime import datetime, timedelta

current_datetime = datetime.now()
seven_days_later = current_datetime + timedelta(days=7)

print(current_datetime)
print(seven_days_later)




"""
Quiz.
1. The datetime module in Python provides a class for manipulating dates 
and times. What is the name of this class?
    a) Datetime
    b) Date
    c) Time
    d) datetime****

2. Which method in the datetime module returns the current date and time?
    a) current()
    b) now()****
    c) today()
    d) get_current_datetime()

3. In the strftime method, what does %Y represent in the formatting string?
    a) Month (01-12)
    b) Year (e.g., 2023)****
    c) Day of the week (Monday-Sunday)
    d) Hour (00-23)

4. Which module in Python provides functionality to work with time-related 
operations such as measuring time intervals, and converting between different 
time representations?
    a) time
    b) datetime****
    c) timedelta
    d) timezone

5. Which method from the time module returns the current time in seconds since 
the epoch (January 1, 1970)?
    a) time()****
    b) ctime()
    c) strftime()
    d) gmtime()

6. In the time module, which method pauses the program's execution for the specified 
number of seconds?
    a) sleep()****
    b) wait()
    c) pause()
    d) delay()

7. Which method of the datetime class in the datetime module returns a formatted string 
representing the date and time?
    a) format()
    b) strftime()****
    c) to_string()
    d) get_formatted()

8. In the datetime module, what does the timedelta class represent?
    a) A duration expressing the difference between two date or time instances****
    b) A specific point in time
    c) A formatted date and time string
    d) A timezone offset

9. Which method of the timedelta class allows you to extract the number of days?
    a) days()****
    b) total_days()
    c) get_days()
    d) days_total()

10. To get the current date and time, which method would you use in the datetime module?
    a) datetime.now()****
    b) datetime.today()
    c) datetime.current()
    d) datetime.get_current()

11. In the strftime method, what does %d represent in the formatting string?
    a) Month (01-12)
    b) Year (e.g., 2023)
    c) Day of the month (01-31)****
    d) Hour (00-23)

12. In the strftime method, what does %H represent in the formatting string?
    a) Month (01-12)
    b) Year (e.g., 2023)
    c) Hour (00-23)****
    d) Minute (00-59)

13. In the strftime method, what does %M represent in the formatting string?
    a) Month (01-12)
    b) Year (e.g., 2023)
    c) Minute (00-59)*****
    d) Second (00-59)

14. Consider the following Python code snippet:
    import time

    start_time = time.time()
    time.sleep(3)
    end_time = time.time()

    print(f"Execution took {end_time - start_time} seconds.")

    What is the purpose of this code, and what will be the output when it is executed?
    a) This code measures the execution time of the time.sleep(3) statement *****
    and prints the elapsed time in seconds.
    b) This code creates a timer that prints "Execution took 3 seconds." 
    after waiting for 3 seconds.
    c) This code will throw an error because time.sleep() cannot be used 
    with a floating-point argument.
    d) This code will hang indefinitely without producing any output.
"""
# """
# - Kwargs -
# A. Create a function that accepts **kwargs and prints out all the key-value pairs passed as arguments.
def print_key_value_pairs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}--{value}")
        
print_key_value_pairs(name="Vusal", age=36, city="Baku")



# B. Write a function that accepts **kwargs containing numeric values and returns the sum of all the values.

def sum_numeric_values(**kwargs):
    total_sum = 0

    for value in kwargs.values():
        if isinstance(value, (int, float)):
            total_sum += value
    
    return total_sum

result = sum_numeric_values(apple=35, banana=40, kiwi=45)
print(result)



# C. Create a function that filters a dictionary based on the keys provided as **kwargs.

def filter_dict_by_keys(student_data, **kwargs):
    filtered_dict = dict(filter(lambda item: item[0] in kwargs, student_data.items()))
    return filtered_dict

student = {"name": "John",
           "age": 25,
           "city": "New York",
           "gender": "male"}

filtered_result = filter_dict_by_keys(student, name=True, age=True, country=True)

print(filtered_result)




# D. Write a function that validates input parameters using **kwargs. For example, ensure that a function 
# only accepts specific keyword arguments and raises an error if any invalid argument is passed.

def validate_person_info(**kwargs):
    allowed_arguments = {'name', 'age', 'is_student'}

    invalid_arguments = set(kwargs.keys()) - allowed_arguments
    if invalid_arguments:
        raise ValueError(f"Invalid arguments: {', '.join(str(arg) for arg in invalid_arguments)}")

    print("Validation successful! Proceeding with the function logic.")

try:
    validate_person_info(name='John Doe', age=25, is_student=True)
except ValueError as e:
    print(f"Error: {e}")

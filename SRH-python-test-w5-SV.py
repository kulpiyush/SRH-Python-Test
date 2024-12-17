# Big Data Programming: Pyhton Module Test
# Instructions ...
# Please consider good style & naming while developing the code when necessary,
#  such as Docstring, linting, etc. it is considered in the grading process!
# Use this file for the solution only. Jupyter notebook(.ipynb) not acceptable!
# Push the solution to a remote repo of name "SRH-Python-Test", and send me the link of the repo as DM
#  on Ms Teams for assessment.
# The duration of this test is 1 hour.

# Q1: What is the main difference between the list and Tuple?
# List:
# 1. Lists are mutable.
# 2. Lists are represented in '[]'.
# 3. Lists are slower compared to Tupels.
# 4. Uses more memory due to dynamnic in nature.
#5. Allows operation like append, remove e.t.c...

# Tuple
# 1. Tuple are mutable
# 2. Tuple are represented in '()'
# 3. Tuple are fater compared to Lists.
# 4. Tuple uses less memory compared to list.
# 5. Does not allow operations like append, remove e.t.c...


# Q2: why should list indexing be used Python?
# 1.  Indexing allows us to directly access specific elements in a list using their positions.
# Python uses zero-based indexing (first element at index 0).
# For e.g: list = [10, 20, 30, 40]
# 2. Eficient data retrivel:
# Using an index to access a list element is very fast , which makes it ideal for working with large datasets.
# 3. Iteration and Automation
#Indexing helps when iterating through a list, especially when specific conditions require certain positions.
# 4. Flexible Data Access
#With indexing, we can: Retrieve values,Replace values,Extract sublists, allowing for highly flexible data manipulation.



# Q3: You have two lists (string_list, values_list) below. Write a function of
#  a name count_car. The function returns a dictionary.
#  The expected return of the function should print out this dictionary:
#  {'Audi_Q5': 2, 'Honda_civic': 4, 'Mercedes_200E': 5, 'BMW_720': 7, 'VW_passat': 2}
string_list = ['Audi_Q5', 'Honda_civic', 'Mercedes_200E', 'Honda_civic',
               'BMW_720', 'VW_passat']

value_list = [2, 4, 5, 7, 2]

# Your code here ...
def count_car(string_list, value_list):
    car_count = {}  # Initialize an empty dictionary

    # Iterate over both lists simultaneously
    for car, value in zip(string_list, value_list):
        if car not in car_count:  # Only add the car if it’s not already in the dictionary
            car_count[car] = value

    return car_count

# Given lists
string_list = ['Audi_Q5', 'Honda_civic', 'Mercedes_200E', 'Honda_civic',
               'BMW_720', 'VW_passat']

value_list = [2, 4, 5, 7, 2]

# Call the function
result = count_car(string_list, value_list)

# Print the result
print(result)


# Q4: Write a function of a name double_even_numbers. The function squares the
#  even numbers only. Also, the function leaves the first element of the input
#  as is without getting squared regardless being even or odd number.
#  The function has one argument which is a numpy array of 100 elements of
#  integer type between 0-10.
#  The function returns an array. Use list comprehension in your answer.

# Your code here ...
import numpy as np

def double_even_numbers(arr):
    # Ensure input is a numpy array
    if not isinstance(arr, np.ndarray):
        raise ValueError("Input must be a numpy array.")
    
    # list comprehension to square even numbers, leave first element unchanged
    result = np.array([arr[0]] + [x**2 if x % 2 == 0 else x for x in arr[1:]])
    return result

# Example usage:
np.random.seed(42)  # Set seed for reproducibility
input_array = np.random.randint(0, 11, size=100)  # Random array of 100 integers between 0-10

output_array = double_even_numbers(input_array)
print("Input Array:", input_array)
print("Output Array:", output_array)


# Q5: Read "movies.csv" file, a file is provided. Create a function
#  returns only table of elements before 2000 with score 7 and above, then save
#  the elements in a new csv file with a name "dest_csv". 

# Your code here ...
import pandas as pd

def filter_and_save_movies(file_path, dest_csv):
    
    # Step 1: Read the CSV file
    df = pd.read_csv("/Users/piyushkulkarni/Downloads/movies.csv")

    # Step 2: Filter the DataFrame
    filtered_df = df[(df['year'] < 2000) & (df['score'] >= 7)]

    # Step 3: Save the filtered data to a new CSV file
    filtered_df.to_csv(dest_csv, index=False)

    # Step 4: Return the filtered DataFrame
    return filtered_df

# Example usage
input_file = "movies.csv"  # Input CSV file name
output_file = "dest_csv.csv"  # Output CSV file name

# Call the function
filtered_movies = filter_and_save_movies(input_file, output_file)

# Display the filtered movies
print(filtered_movies)


# Q6: Write a function of a name div_func. It returns the divsion of elements
#  in a list in reversed order. The function should pass the two lists below
#  without errors.

import random
random.seed(42)
short_list = [1, 0, 2, 2, 20]
long_list = [random.randrange(0, 10, 1) for i in range(15)]

# Your code here ...
import random

def div_func(input_list):
    result = []
    reversed_list = input_list[::-1]  # Reverse the input list
    
    # Loop through consecutive pairs of elements
    for i in range(len(reversed_list) - 1):
        numerator = reversed_list[i]
        denominator = reversed_list[i + 1]
        
        # Avoid division by zero
        if denominator != 0:
            result.append(numerator / denominator)
        else:
            result.append(None)  # Append None if division by zero occurs

    return result

# Generate lists
random.seed(42)
short_list = [1, 0, 2, 2, 20]
long_list = [random.randrange(0, 10, 1) for i in range(15)]

# Call the function
short_result = div_func(short_list)
long_result = div_func(long_list)

# Print results
print("Short List:", short_list)
print("Short List Division (Reversed):", short_result)

print("\nLong List:", long_list)
print("Long List Division (Reversed):", long_result)


# cd /Users/piyushkulkarni/projects/my-python-project
git init
git add example.py
git commit -m "Add example.py to the repository"
git remote add origin https://github.com/piyushkulkarni/my-python-project.git
git push -u origin master

"""
Write a python3 script with the above name which does the following:

Initialises a list which contains the FIRST NAME of all 21 people in this cohort.
Using the .append() function add Luke Benson to the list.
Print the 5th person in the list (this is a trick question, what is special about the way Python indexes?)
Print the number of Chris' in the cohort.
"""

# Here, we create a function to append our trainer's name to the list.

def trainer_append(trainer, name_list):
    return name_list.append(trainer_name)

# Define variables.

 # A list of first names within QAC DevOps cohort.
first_names = ['Jason','Josh', 'Steven', 'Jack', 'Wasim', 'Dom', 'Thembia', 'Jacob', 'Arsalan', 'Mowafak', 'Chris','Amanda', 'Javas', 'John','Chris', 'Ryan', 'Bradley', 'Clifford', 'Tobi', 'Sam','Ed']

# Here, we specify the result to find within our list.
nth_result_in_list = 5

# Here, we convert the nth result to the corresponding index position.
nth_index_pos = nth_result_in_list - 1

# Define a name to count within our list.
name_to_count = 'Chris'

# Define's our trainer's name.
trainer_name = 'Luke'

# Execute code and call functions.

# Prints the length of the first_names list.
print(f"There are {len(first_names)} students in our cohort.")

# Calls function to append trainer name to our list of first names.
print(f"Before we append our {trainer_name}'s name: {first_names}")
trainer_append(trainer_name, first_names)
print(f"After we append our {trainer_name}'s name: {first_names}")

# Prints the n'th result in our list of first names.
print(f"The {nth_result_in_list}th name in our list of QA first names is: {first_names[nth_index_pos]}!")

print(f"There are {first_names.count(name_to_count)} people called {name_to_count} in our cohort.")

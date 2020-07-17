# Write a while loop which asks for the names of 5 people.
# For each person prints their name, followed by the text "is awesome!"

# Define functions
def name_append(list):
    name_input = str(input("What is your first name: "))
    list.append(name_input)
    print(f'{name_input} is awesome!')


# Define variables
first_names = []
repeats = 5

# Execute code
while len(first_names) <= (repeats - 1):
    name_append(first_names)

'''
Create a new Python file and write a program that does the following:

Asks for an input from the user as a mark.
If the mark is greater that 85 print "distinction"
If the mark is between 65 and 85 "pass"
Anything else print "Fail"
Try to do it both with and without elif statements.
'''


# Define Functions
def grade_calculator(grade, higher_bound, lower_bound, distinction_grade, pass_grade):
    if grade > distinction_grade and grade <= higher_bound:
        return "Distinction"
    elif grade > pass_grade and grade < distinction_grade:
        return "Pass"
    elif grade < pass_grade:
        return "Fail"
    else:
        return "Please enter a valid grade!"


def user_output(grade, grade_response, lower_bound, higher_bound):
    if grade >= lower_bound and grade <= higher_bound:
        print(f'A grade of {grade} is a {grade_response}!')
    else:
        print(f'Please enter a grade between {lower_bound} and {higher_bound}!')


# Declare Variables
lower_bound = 0
higher_bound = 100
distinction_grade = 85
pass_grade = 65

# Takes user input and checks for errors
try:
    grade = int(input("Please enter your exam grade here: "))
except:
    print('Please enter a valid grade!')
    quit()

# Execute Code
grade_response = grade_calculator(grade, higher_bound, lower_bound, distinction_grade, pass_grade)
user_output(grade, grade_response, lower_bound, higher_bound)

"""

Task: In a new Python file, create a class of students.

It should contain the following attributes: name, age, and class with default value "student".

It should also contain a method which takes in 3 test scores and prints the students average test score.

"""


# Define Classes -----------------------------------------------------------------------------------------------------

class Student:

    def __init__(self, name, age, class_):
        self.name = name
        self.age = age
        self.class_ = class_
        self.gpa = "Not Set"

    def ave_test_score(self, score_list):
        gpa = sum(score_list) / len(score_list)
        self.gpa = gpa
        return gpa


# Declare Variables --------------------------------------------------------------------------------------------------

test_scores = [12, 14, 15]

# Execute Code -------------------------------------------------------------------------------------------------------

student = Student('Josh', 23, "Maths")
print(f"{student.name}'s average test score is: {student.ave_test_score(test_scores)}")
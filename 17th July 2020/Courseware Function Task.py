"""
Create a program that works out a grade,
 based on marks with the use of functions.
The program should give the students name and an ICT grade based on:
Homework(/25), Assessment(/50), Final Exam(/100).
"""


# Define Classes

class Exam:
    # Exam class models each exam, the name of the exam, it's minimum and maximum grades.

    def __init__(self, exam_name, grade_min, grade_max, exam_list='exam_list'):
        self.exam_name = exam_name
        self.grade_min = grade_min
        self.grade_max = grade_max

        # The following function appends the name of our new exam to exam_list.
        exam_list.append((self.exam_name, self.grade_min, self.grade_max))
        exam_name_list.append(self.exam_name)

        # The following function finds the index of exam_name, and creates a unique exam ID from that.
        self.exam_id = exam_list.index((self.exam_name, self.grade_min, self.grade_max))
        print(f"{self.exam_name} has an exam ID of: {self.exam_id}")


class Student:
    # Student class models the student, and their name.

    def __init__(self):
        self.first_name = input("What is the first name of your student: ")
        self.surname = input("What is the last name of your student: ")
        self.full_name = self.first_name + " " + self.surname

        # append the name of our new student to the student list.
        student_list.append(self.full_name)
        print(f"{self.full_name}'s student ID is: {student_list.index(self.full_name)}")


class TestResult:
    # testresult class models the result of each test. Upon initialisation, we require a number of checks to find the
    # values of student_id and exam_id.

    def __init__(self):

        print(f"The current exams are: {exam_name_list}")
        self.exam_name = input("Enter the name of a specific examination: ")  # Ask for the specific exam.

        if self.exam_name in exam_name_list:  # Check exam name with list of exams to see if it actually exists.

            self.exam_id = exam_name_list.index(self.exam_name)
            print(f'{self.exam_name} is an exam! Moving on.')

        else:
            print(f"Please create a {self.exam_name} Exam object before creating a test result. Breaking loop.")
            return

        self.student_id = int(input("Please enter a student ID: "))  # Check to out if the student_id is valid.

        # Student.id is the index position of student in Student.student_list.

        if 0 <= self.student_id < len(student_list):
            self.student_name = student_list[self.student_id]  # Returns the name of the student.

            print(f'The name of the student is {self.student_name}') # Maybe add a yes/no check here?

        else:
            print('This student ID does not exist. Please check your student\'s ID and try again.')
            return

        print(f"The lowest achievable mark is: {exam_list[self.exam_id][1]}")
        print(f"The highest achievable mark is: {exam_list[self.exam_id][2]}")

        self.score = int(input(f"Please enter {self.student_name}'s the test score: "))

        # Checks to see if the exam score is equal to number of marks.

        if exam_list[self.exam_id][1] < self.score < exam_list[self.exam_id][2]:

            self.percent = 100 * self.score / (exam_list[self.exam_id][1] - exam_list[self.exam_id][2]) # Calculates Percent

            print(f"An exam score of {self.score} has been added to {self.student_name}'s {self.exam_name} record.")
            all_results.append((self.score, self.student_id, (self.exam_id, self.exam_name)))  # Appends our new result to a list of all_results.
        else:
            print("This is not a valid examination score. Please retry.")
            return


# Define Functions

# Define Procedures

# Define List Variables # --------------------------------------------------------------------------------------------

# A list of all the exam instances which exist in our program.
exam_name_list = []
exam_list = []

# A list of all of the students who exist in the program.
student_list = []

# A list of every result, with the corresponding score, student_id, and exam_id.
all_results = []

# Enter the pass and distinction grades, in percent (out of 100). # --------------------------------------------------

pass_percent = 60
distinction_percent = 85

# Create your exams here (name, min, max) # --------------------------------------------------------------------------

homework = Exam('homework', 0, 25, exam_list)
assessment = Exam('assessment', 0, 50, exam_list)
final_grade = Exam('finals', 0, 100, exam_list)

# Create your students here # ----------------------------------------------------------------------------------------

s_josh = Student()
s_sam = Student()
s_chris = Student()
s_thembia = Student()

# Checks to see the contents of each list # --------------------------------------------------------------------------

for i in range(3):
    TestResult()

# print(exam_list)
# print(all_results) - (Grade, Student, Exam ID, Exam Name)

'''
def grade_calculator(exam_variable, student_variable):
    
    if distinction <= student_percent <= 100:
        return "Distinction"
    elif passing <= student_percent <= distinction:
        return "Passing Grade"
    elif 0 <= student_percent <= passing:
        return "Fail"
    else:
        print("There has been an error!")
        quit()






def user_output(name, topic, percent, grade):
    print(f"{name[0]} {name[1]}'s {topic} percentage mark is: {percent}%, which is a {grade}!")





homework_percent = grade_percent(homework.grade_max, homework.grade_min, student_homework)
homework_grade = grade_calculator(pass_percent, distinction_percent, homework_percent)

assessment_percent = grade_percent(assessment_grade_max, assessment_grade_min, student_assessment)
assessment_grade = grade_calculator(pass_percent, distinction_percent, assessment_percent)

final_exam_percent = grade_percent(final_exam_grade_max, final_exam_grade_min, student_final_exam)
final_exam_grade = grade_calculator(pass_percent, distinction_percent, final_exam_percent)

student_total_raw_marks = student_homework + student_assessment + student_final_exam
total_marks = homework_grade_max + assessment_grade_max + final_exam_grade_max
min_marks = final_exam_grade_min + assessment_grade_min + homework_grade_min

total_percent = round(grade_percent(total_marks, min_marks, student_total_raw_marks))
total_grade = grade_calculator(pass_percent, distinction_percent, total_percent)

# Execute Code

user_output(student_full_name,topic1_name,homework_percent,homework_grade)
'''

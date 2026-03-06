# This module contains functions to process student data.
from student_data import students
from filters import filter_students_by_major
def format_student_data(student):
    return f"ID: {student[0]} | Name: {student[1]} | Major: {student[2]}"
    

def display_students(student_list):
    for student in student_list:
        print(format_student_data(student))

display_students(students)
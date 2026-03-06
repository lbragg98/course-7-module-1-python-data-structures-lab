# This module contains functions for filtering student data.
from student_data import students

def filter_students_by_major(student_list, major):
    return [student for student in students if students [2] == major]

cs_students = filter_students_by_major("Computer Science")

for student in cs_students:
    print(student)
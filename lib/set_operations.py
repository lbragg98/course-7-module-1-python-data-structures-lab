# This module contains operations related to sets.
from student_data import students


def unique_majors(student_list):
    return {student[2] for student in student_list} 
# simple dict from list
# new_dict = {key_value: value for key_value in list}
from random import randint
students = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_grades = {student: randint(1,100) for student in students}
print(students_grades)

# simple dict from dict
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}
approved_students = {student:grade for student, grade in students_grades.items() if grade >= 60}
print(approved_students)
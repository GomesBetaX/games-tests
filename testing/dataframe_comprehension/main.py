import pandas

student_dict = {
    "student": ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"],
    "score": [10, 20, 30, 40, 50, 60],
}

students_data_frame = pandas.DataFrame(student_dict)

# loop through row of a data frame
for (index, row) in students_data_frame.iterrows():
    print(row.score)
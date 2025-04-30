import pandas

student_dict = {
    "student": ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"],
    "score": [1, 2, 3, 4, 5, 6],
}

students_data_frame = pandas.DataFrame(student_dict)

# loop through row of a data frame
for (index, row) in students_data_frame.iterrows():
    print(row.score)
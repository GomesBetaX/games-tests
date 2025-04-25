# import csv

# data = []
# with open("./weather_data.csv", "r") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("./weather_data.csv")
# get avg temp
print(data["temp"].mean())

# print max temp row
highest_temp = data["temp"].max()
print(data[data.temp == highest_temp])

# get
monday = data[data.day == "Monday"]
temp = monday.temp[0]
temp_f = round((temp * (9/5)) + 32, 2)
print(temp_f)
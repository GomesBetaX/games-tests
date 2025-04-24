import pandas

# read the csv using pandas
data = pandas.read_csv("./squirrel/squirrel_data.csv")

# get a variable to store only the colors column
data_colors = data["Primary Fur Color"]

# get the colors and counts them
gray = data_colors[data_colors == "Gray"].count()
cinnamon = data_colors[data_colors == "Cinnamon"].count()
black = data_colors[data_colors == "Black"].count()

# creates a dataframe with the colors and amounts
squirrel_count = pandas.DataFrame({
    "fur color": ["Gray", "Red", "Black"],
    "count": [gray, cinnamon, black]
})

# write to a csv file
squirrel_count.to_csv("./squirrel/squirrel_count.csv")
import pandas

data = pandas.read_csv("./squirrel/squirrel_data.csv")
data_colors = data["Primary Fur Color"]
gray = data_colors[data_colors == "Gray"].count()
cinnamon = data_colors[data_colors == "Cinnamon"].count()
black = data_colors[data_colors == "Black"].count()

squirrel_count = pandas.DataFrame({
    "fur color": ["Gray", "Red", "Black"],
    "count": [gray, cinnamon, black]
})

squirrel_count.to_csv("./squirrel/squirrel_count.csv")
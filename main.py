import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_color_data = squirrel_data[squirrel_data["Primary Fur Color"].notnull()]

fur_colors = fur_color_data["Primary Fur Color"].unique()

squirrels_dict = {
    "Fur color": fur_colors.tolist(),
    "Count": []
}
for color in fur_colors:
    squirrels_dict["Count"].append(len(fur_color_data[fur_color_data["Primary Fur Color"] == color]))

squirrel_df = pandas.DataFrame(squirrels_dict)
squirrel_df.to_csv("squirrels_count_by_fur_color.csv")

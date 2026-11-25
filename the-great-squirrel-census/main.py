import pandas as pd

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20261125.csv")
grey_squirrels_count = len(df[df["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(df[df["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(df[df["Primary Fur Color"] == "Black"])

squirrel_data = {
    'Fur Color': df["Primary Fur Color"].unique().dropna(),
    'Count':[grey_squirrels_count,cinnamon_squirrels_count,black_squirrels_count]
}

data = pd.DataFrame(squirrel_data)
data.to_csv("squirrel_data.csv")
import pandas as pd

df = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240522.csv')

count = df['Primary Fur Color'].value_counts()
color = df['Primary Fur Color'].dropna().unique()


new_dict = {'Fur Color' : color, 'Count' : count.to_list()}

new_df = pd.DataFrame(new_dict)
new_df.to_csv("squirrel_count.csv")
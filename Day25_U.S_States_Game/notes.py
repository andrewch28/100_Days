# #First task
# with open("weather_data.csv") as file:
#     data = file.readlines()

# #Second Task

# import csv
# temperatures = []


# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     for row in data:
#         if row[1].isnumeric():
#             temperatures.append(int(row[1]))
#
# print(temperatures)

# #Pandas
import pandas as pd

df = pd.read_csv("weather_data.csv")
# print(type(df))
# print(type(df["temp"]))

# df_dict = df.to_dict()
# print(df_dict)
#
# temp_list = df["temp"].to_list()
# average = sum(temp_list) / len(temp_list)
# print(round(average, 2))
#
# print(df['temp'].max())

# #Getting Data in columns
# print(df['condition'])
# print(df.condition)

# # Getting Data in rows
# # print(df[df['day'] == 'Monday'])
# max_temp = df['temp'].max()
# print(df[df['temp'] == max_temp]['condition'])


# monday_temp = df[df['day'] == 'Monday']
# F = monday_temp['temp'] *9/5 + 32
# print(F)

# #Create a DataFrame from scratch
# data_dict = {
#     'students' : ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }
#
# df = pd.DataFrame(data_dict)
# print(df)
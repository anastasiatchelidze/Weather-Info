import pandas as pd

data = pd.read_csv("weather_data.csv")
temp_list = data["temp"].to_list()  # making list from the column of DataFrame

temp_average = data["temp"].mean()
print("The average of this week's temperature is {:.2f}".format(temp_average))  # formatting the value to display it only with 2 decimal points

max_temp = data["temp"].max()
print(f"The maximum this week's temperature is {max_temp}")

monday = data[data.day == "Monday"]
print("Monday's temperature in Fahrenheit: ", (monday.temp * 1.8) + 32, sep="\n")
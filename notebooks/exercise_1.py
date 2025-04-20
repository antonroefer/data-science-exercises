import pandas as pd
from scipy.stats import ttest_ind

# Load the CSV file
file_path = "C:/Users/anton/Documents/Studium/Data Science/data-science-exercises/data/external/wetter.csv"
data = pd.read_csv(file_path)

# Calculate the overall average temperature
overall_avg_temp = data["Temperatur"].mean()
print(f"Overall Average Temperature: {round(overall_avg_temp, 2)} °C")

# Calculate the average temperatures for each month
data["month"] = pd.to_datetime(data["Datum"]).dt.month
monthly_avg_temp = data.groupby("month")["Temperatur"].mean()
monthly_avg_temp_rounded = monthly_avg_temp.round(2)

# Map month numbers to month names
month_names = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}
monthly_avg_temp_dict = {
    month_names[month]: f"{temp} °C" for month, temp in monthly_avg_temp_rounded.items()
}
print(f"Monthly Average Temperatures: {monthly_avg_temp_dict}")

# Compare July (7) and May (5) average temperatures for statistical significance
july_avg_temp = monthly_avg_temp.loc[7]
may_avg_temp = monthly_avg_temp.loc[5]

if not pd.isna(july_avg_temp) and not pd.isna(may_avg_temp):
    print(f"July Average Temperature: {july_avg_temp:.2f} °C")
    print(f"May Average Temperature: {may_avg_temp:.2f} °C")
    percentage_difference = ((july_avg_temp - may_avg_temp) / may_avg_temp) * 100
    print(
        f"The percentage difference between July and May average temperatures is {percentage_difference:.2f}%."
    )
else:
    print(
        "Average temperature data for July or May is not available for percentage difference calculation."
    )

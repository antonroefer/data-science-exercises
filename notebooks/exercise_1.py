import pandas as pd
from scipy.stats import ttest_ind

# Load the CSV file
file_path = "./../data/external/wetter.csv"
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
for month, temp in monthly_avg_temp_dict.items():
    print(f"{month}: {temp}")

# Compare July (7) and May (5) average temperatures for statistical significance using t-test
july_temps = data[data["month"] == 7]["Temperatur"]
may_temps = data[data["month"] == 5]["Temperatur"]

if not july_temps.empty and not may_temps.empty:
    t_stat, p_value = ttest_ind(july_temps, may_temps, equal_var=False)
    print(f"T-statistic: {t_stat:.2f}, P-value: {p_value:.4f}")
    if p_value < 0.05:
        print(
            "The difference in average temperatures between July and May is statistically significant."
        )
    else:
        print(
            "The difference in average temperatures between July and May is not statistically significant."
        )
else:
    print("Temperature data for July or May is not available for t-test calculation.")

import pandas as pd

# Load the wetter.csv file
file_path = "data/external/wetter.csv"
wetter_data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(wetter_data.head())

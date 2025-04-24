import pandas as pd

# Load the wetter.csv file
wetter_file_path = "./../data/external/wetter.csv"
wetter_data = pd.read_csv(wetter_file_path)

# Load the kiwo.csv file
kiwo_file_path = "./../data/external/kiwo.csv"
kiwo_data = pd.read_csv(kiwo_file_path)

# Load the umsatzdaten.csv file
umsatzdaten_file_path = "./../data/external/umsatzdaten_gekuerzt.csv"
umsatzdaten_data = pd.read_csv(umsatzdaten_file_path)

# Display the first few rows of the dataset
print(wetter_data.head())
print(kiwo_data.head())
print(umsatzdaten_data.head())

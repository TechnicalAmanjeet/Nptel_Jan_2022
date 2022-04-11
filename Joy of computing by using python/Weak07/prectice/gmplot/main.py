import time

import gmplot
import csv
import pandas as pd

# method 1 to read csv file.
with open("./long_lat.csv", 'r') as file:
    reader = csv.reader(file)
    for data in reader:
        # print(data)
        pass

# method 2 to read csv file
file1 = pd.read_csv("long_lat.csv")
numpy_array = file1.to_numpy()
longitude = []
latitude = []

for item in numpy_array:
    longitude.append(item[0])
    latitude.append(item[0])



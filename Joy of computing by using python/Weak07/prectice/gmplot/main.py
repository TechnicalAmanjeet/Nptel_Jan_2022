import time

import gmplot
import csv
import pandas as pd

# # method 1 to read csv file.
# with open("./long_lat.csv", 'r') as file:
#     reader = csv.reader(file)
#     for data in reader:
#         # print(data)
#         pass
#
# # method 2 to read csv file
# file1 = pd.read_csv("long_lat.csv")
# numpy_array = file1.to_numpy()
# longitude = []
# latitude = []
#
# for item in numpy_array:
#     longitude.append(item[0])
#     latitude.append(item[0])


gmap = gmplot.GoogleMapPlotter(28.356, 76.456, 15)

gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s"
with open("./long_lat.csv", 'r') as file:
    reader = csv.reader(file)
    temp = 0
    times = 0

    for row in reader:
        try:
            lat = float(row[0])
            long = float(row[1])
        except:
            continue

        if temp == 0:
            gmap.marker(lat, long, "blue")
            temp = 1
        else:
            gmap.marker(lat, long, "yellow")

        times += 1
        if times == 500:
            break

gmap.marker(lat, long, "red")
gmap.draw("mymap.html")



from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import csv

## Initialize the map with robinson projection
map = Basemap(projection='robin', lat_0=0, lon_0=9.1)
#vmap.drawcoastlines()
map.fillcontinents(color='lightsteelblue', lake_color=None)

## Read the coodinates.csv file to draw the planetlab node locations
with open('coordinates.csv', 'rb') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	for row in csvreader:
		lat = float(row[2])
		lon = float(row[3])
		print lat, lon
		x, y = map(lon, lat)
		map.plot(x, y, marker='o', fillstyle='full', markersize=5, color='sandybrown')

## Read the coordinates of all Google datacenters' locations.
with open('GCE.csv', 'rb') as gcefile:
	csvreader = csv.reader(gcefile, delimiter=',')
	for row in csvreader:
		lat = float(row[1])
		lon = float(row[2])
		print row
		x, y = map(lon, lat)
		map.plot(x, y, marker='s', fillstyle='full', markersize=10, color='maroon')


plt.savefig("nodes.png", bbox_inches="tight")
plt.show()

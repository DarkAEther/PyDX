from math import *
import requests
citlist = set()
internal = []
#numofcities = int(input("Input number of cities: "))
lats = []
longs = []
for i in range(2):
	citlist.add(input("Enter city name, please be accurate: "))

i = 0
for item in citlist:
	
	querystring = 'address='+item
	response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?'+querystring)
	respjsonpayload = response.json()
	data = str(respjsonpayload['results'][0]['geometry']['location'])
	
	for item in data.split(','):
		internal.append(item.split())
	
	lat = float(internal[0+i][1])
	long = internal[1+i][1]
	long = float(long[:len(long)-1])
	lats.append(lat)
	longs.append(long)
	i = 2

#calculate distance using HAVERSINE equation

R = 6371e3
dellats = radians((lats[1]-lats[0])/2)

dellongs = radians((longs[1]-longs[0])/2)

a = (sin(dellats))**2 + cos(radians(lats[0])) * cos(radians(lats[1])) * (sin(dellongs))**2

c = 2 * atan2(sqrt(a),sqrt(1-a))

d = R * c
print("{0} is {1}kms away from {2}".format(list(citlist)[0],format(d/1000,'.2f'),list(citlist)[1]))
#print("% error compared to google: {0}".format())

# Create a program to find Distance between two geographical coordinate using Haversine formula

'''
a = sin²(diff_lat/2) + cos(lat1).cos(lt2).sin²(diff_long/2)
c = 2.atan2(√a, √(1-a))
d = R.c

where,

ΔlatDifference = lat1 - lat2 (difference of latitude)

ΔlonDifference = lon1 - lon2 (difference of longitude)

R is radius of earth i.e 6371 KM or 3961 miles

and d is the distance computed between two points.
1Deg × π/180 = 0.01745Rad

'''
from math import cos, sin, asin, sqrt, pi

source = (12.314477, 76.646728)
destination = (26.174387004022226, 91.70286580517384)

# Calling the lat and long and coonverting degrees to radians
lat1 = source[0]*(pi/180)
lat2 = destination[0]*(pi/180)

long1 = source[1]*(pi/180)
long2 = destination[1]*(pi/180)

# Findig difference between latitude and longitude
dLat = lat2 - lat1
dLong = long2 - long1

# Applying Haversine formula
a = sin(dLat/2)**2 + cos(lat1) * cos(lat2) * sin(dLong/2)**2
c = 2 * asin(sqrt(a))
r = 6371 # Earth radius in Kilometer
# Calculating distance
distance = r * c

print(distance)



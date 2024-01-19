# Module to convert lat and long to utm

# pip install utm

import utm

lat = float(input('Enter latitude: '))
long = float(input('Enter longitude: '))
if lat > 0:
    zone = 'N'
else:
    zone = 'S'
output = utm.from_latlon(lat,long)
print(f'Easting is {output[0]}')
print(f'Northing is {output[1]}')
print(f'Zone is {output[2]}{zone}')
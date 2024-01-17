# Write a code to find utm zone of lat/long value
# utm = 31+long/6

latitude = 12.3456
longitude = 76.9893
if longitude > 0 and latitude > 0:
    print('North and Eastern hemisphere')
    utmGrid = 'N'
elif longitude > 0 and latitude < 0:
    print('South and Eastern hemisphere')
    utmGrid = 'S'
elif longitude < 0  and latitude > 0:
    print('North and Western hemisphere')
    utmGrid = 'N'
elif longitude < 0 and latitude <0 :
    print('South and Western hemisphere')
    utmGrid = 'S'
elif longitude == 0 and latitude == 0:
    print('Primemeridian and Equator intersecting point')
else:
    print('Invalid input')

zone = 31 + (longitude/6)
print(f'UTM zone {int(zone//1)}{utmGrid}')

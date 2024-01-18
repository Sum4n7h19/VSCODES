# Write a program to print all key, value pairs in a dictionary

# Copied a dictionar form geojson.io
point = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          76.69196982581445,
          12.420901771497341
        ],
        "type": "Point"
      }
    }
  ]
}

for key in point:
    print(key, point[key])



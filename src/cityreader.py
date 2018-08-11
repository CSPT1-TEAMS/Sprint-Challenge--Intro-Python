# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.
import csv

class City:
    def __init__(self, name, lat, long):
        self.name = name
        self.lat = lat
        self.long = long

# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# Use Python's built-in "csv" module to read this file so that each record is
# imported into a City instance. (You're free to add more attributes to the City
# class if you wish, but this is not necessary.) Google "python 3 csv" for
# references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.

with open('cities.csv') as file:
    reader = csv.DictReader(file)
    cities = [
        City(row['city'], row['lat'], row['lng'])
        for row in reader
    ]

# Print the list of cities (name, lat, lon), 1 record per line.

for city in cities:
    print(city.name, city.lat, city.long)

# *** STRETCH GOAL! ***
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Output the cities that fall
# within this square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)
def find_location(cities):
    inpt = input('\nEnter first coordinates: ').split()
    lat1, lon1 = float(inpt[0]), float(inpt[1])

    inpt2 = input('Enter second coordinates: ').split()
    lat2, lon2 = float(inpt2[0]), float(inpt2[1])

    for city in cities:
        latitude = float(city.lat)
        longitude = float(city.long)

        if (latitude <= lat1 and longitude <= lon1) and (latitude >= lat2 and longitude >= lon2):
            print(f"{city.name}: ({city.lat}, {city.long})")

find_location(cities)
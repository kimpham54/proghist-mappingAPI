import os, csv, sys, geopy
import pandas
from geopy.geocoders import Nominatim, GoogleV3
# geopy 1.10.0, pandas 0.16.2
# this script is used to geocode one column in a csv file.  you need to modify the input file (census_borough.csv) and Area_Name column


def main():
	io = pandas.read_csv('census_borough.csv', index_col=False, header=0, sep=",")
	name = io['Area_Name']
	geolocator = Nominatim()
	# geolocator = GoogleV3()
	# io['city_coord'] = io['Area_Name'].apply(geolocator.geocode).apply(lambda x: (x.latitude, x.longitude))
	io['latitude'] = io['Area_Name'].apply(geolocator.geocode).apply(lambda x: (x.latitude))
	io['longitude'] = io['Area_Name'].apply(geolocator.geocode).apply(lambda x: (x.longitude))
	io.to_csv('geocoding-output-single.csv')

if __name__ == '__main__':
  main()
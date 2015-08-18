import os, csv, sys, geopy
import pandas
from geopy.geocoders import Nominatim, GoogleV3
# geopy 1.10.0, pandas 0.16.2
# this script is used to geocode two columns (potentially more if you want to modify), taking arguments from the command line
# $ python geocoder-sys-helpercolumn.py onerow.csv Area_Name Country

inputfile=str(sys.argv[1])
namecolumn=str(sys.argv[2])
helpercolumn=str(sys.argv[3])

def main():
	io = pandas.read_csv(inputfile, index_col=False, header=0, sep=",")
	name = io[namecolumn]


	geolocator = Nominatim()
	# geolocator = GoogleV3()
	# io['city_coord'] = io['Area_Name'].apply(geolocator.geocode).apply(lambda x: (x.latitude, x.longitude))
	io['helper'] = io[namecolumn].map(str) + " " + io[helpercolumn]
	io['latitude'] = io['helper'].apply(geolocator.geocode).apply(lambda x: (x.latitude))
	io['longitude'] = io['helper'].apply(geolocator.geocode).apply(lambda x: (x.longitude))
	io.to_csv('geocoding-output-helper.csv')

if __name__ == '__main__':
  main()


import os, csv, sys, geopy
import pandas
from geopy.geocoders import Nominatim, GoogleV3
# geopy 1.10.0, pandas 0.16.2
# this script is used to geocode one column, taking arguments from the command line
# $ python geocoder-sys-singlecolumn.py onerow.csv Area_Name

inputfile=str(sys.argv[1])
namecolumn=str(sys.argv[2])

def main():
	io = pandas.read_csv(inputfile, index_col=False, header=0, sep=",")
	name = io[namecolumn]
	# geolocator = Nominatim()
	geolocator = GoogleV3()
	
	io['latitude'] = io[namecolumn].apply(geolocator.geocode).apply(lambda x: (x.latitude))
	io['longitude'] = io[namecolumn].apply(geolocator.geocode).apply(lambda x: (x.longitude))
	io.to_csv('geocoding-output-single.csv')

if __name__ == '__main__':
  main()


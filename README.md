# Visualizing Data with Web Maps

### Learning Objectives
In this lesson, you will learn how to create a web map based on that data.  By the end of this lesson, you will be able to:
* Manipulate tabular data progammatically to extract geonames and create location-based data, 
* Convert tabular data into a meaningful geographic data structure
* Understand and apply the basic concepts of web mapping to design your own web map

### Getting Started

Optional: If you wish to follow along with pre-made scripts you can download them from https://github.com/kimpham54/proghist-mappingAPI

To set up your working environment:
1. Create a directory that you will work from  
2. Import your folder in a text editor such as [TextWrangler](http://www.barebones.com/products/textwrangler/) for OS X, [Notepad++](https://notepad-plus-plus.org/) for Windows, or [Sublime Text](http://www.sublimetext.com/).

### Getting Data: Download the csv
We're going to start with a plain CSV data file and create a web map from it[1]. **Why the footnotes: Should we just incorporate them into the main text of the lesson?**

The original data file can be downloaded here: https://github.com/Robinlovelace/Creating-maps-in-R/blob/master/data/census-historic-population-borough.csv.  The original source of this data is from the Greater London Authority London Datastore website: http://data.london.gov.uk/dataset/historic-census-population

### Geocode the placenames: in the CSV using Geopy, Pandas

Now that we have data, the next step is sometimes the hardest part: we need to figure out what to do with it.  In this case, we know what our end goal is: to make a web map with this data. You can work backwards from here to figure out what steps you need to take to achieve your goal.  

Web maps typically represent locations and features from geographic data formats like geoJSON and KML. Every location in a grographic data file can be considered to have geometry (such as points, lines, polygons) as well as additional properties. Web maps typically understand locations as a series of coordinates. In our data file, we have a list of placenames in our CSV data (the Area Name column), but no coordinates. What we want to do then is to somehow generate coordinates from these locations. This process is called geocoding.

So here is our first problem to solve:  how can we geocode placenames?[2]

To clarify, we need to figure out how to gather coordinates for a location for each row of a CSV file in order to display these locations on a web map.  

There's a simple way to do this: you can look up a coordinate online in Google Maps and put each coordinate in your spreadsheet manually.  But, if you had 5000 points the task becomes a little bit more daunting. If you're faced with a repetitive task, it might be worthwhile approach it programmatically.  

If you're familiar with _Programming Historian_, you might have already noticed that there there are many lessons available on how to use Python.  Python is a great beginner programming language because it is easy to read and happens to be used a lot in GIS applications to optimize workflows.  One of the biggest advantages to Python is the impressive amount of libraries which act like pluggable tools to use for many different tasks.  Knowing that this is a good programmatic approach, we're now going to build a Python script that will automate geocode every address for us.

[Geopy](https://github.com/geopy/geopy) is a Python library that gives you access to the various geocoding APIs.  Geopy makes it easy for Python developers to locate the coordinates of addresses, cities, countries, and landmarks across the globe using third-party geocoders and other data sources. Geopy includes geocoders built by OpenStreetMap Nominatim, ESRI ArcGIS, Google Geocoding API (V3), Baidu Maps, Bing Maps API, Yahoo! PlaceFinder, Yandex, IGN France, GeoNames, NaviData, OpenMapQuest, What3Words, OpenCage, SmartyStreets, geocoder.us, and GeocodeFarm geocoder services. 

[Pandas](http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe) is another python library that we will use.  It's very popular library amongst scientists and mathmaticians to manipulate and analyse data.

If you've [already installed Python](http://programminghistorian.org/lessons/introduction-and-installation), open your [command line (using this lesson as a guideline if necessary)](http://programminghistorian.org/lessons/intro-to-bash) and install the Geopy and Pandas libraries:

*Mac only? *

**Hi Kim - is this for Mac only? Do you know how you'd get this working on Windows? Also, more importantly, they will probably need to use sudo to get the following two pip installs to work? Should we tweak to note?**

```bash
pip install numpy
pip install python-dateutil
pip install pytz
pip install geopy
pip install pandas
```

You may need to upgrade them if you encounter an error when using Python (i.e. an ImportError). In order to do so, the following command works:

```bash
pip install python --uprade
```

Repeat for the other dependencies.

Open your text editor and save your blank document as a python script (name it geocoder.py).  

For the first part of your Python script, you will want to import your data:

**Ian: Can you explain what these commands do? Just one sentence per code block, just walking them through what each line does - i.e. you're importing commands, and then you're reading the CSV - what's index_col and header=0 sep="," - if they're using slightly differently formatted documents, with different seperators, how could they tweak it?**

```python

import os, csv, sys, geopy
import pandas
from geopy.geocoders import Nominatim, GoogleV3
# The versions that I'm using with this script are geopy 1.10.0, pandas 0.16.2
```

Then you want to create a function that reads your input CSV:

```python

def main():
	io = pandas.read_csv('census-historic-population-borough.csv', index_col=False, header=0, sep=",")
```

Next, select the geolocator you want to use.  Here I'm creating two geolocators: Open Street Map's Nominatim and Google's Geocoding API.  You can choose from a list found in [the geopy documentation](http://geopy.readthedocs.org/):

```python
	geolocator = Nominatim()
	# geolocator = GoogleV3()
    # uncomment the geolocator you want to use 
```

Finally, using pandas you want to create a column in your spreadsheet called 'latitude'.  The script will read the existing 'Area_Name' data column, run the geolocator, and generate a latitude coordinate in that column.  The same transformation will occur in the 'longitude' column.  Once this is finished it will ouput a new CSV file with those two columns:

```python
	io['latitude'] = io['Area_Name'].apply(geolocator.geocode).apply(lambda x: (x.latitude))
	io['longitude'] = io['Area_Name'].apply(geolocator.geocode).apply(lambda x: (x.longitude))
	io.to_csv('geocoding-output.csv')
```

To finish off your code, it's good practice to make your python modular, that way you can plug it in and out of other applications (should you want to use this script as part of another program):

```python
if __name__ == '__main__':
  main()
```

Do you have a script ready? Good.  Run the script from your command line by typing: 

```bash
python geocoder.py
```

It takes a few seconds and may take longer depending on the geolocator you use. Once the script finishes running, you should have coordinates for every Area Name.

**Notes:**
If you run it too many times because you get a timeout error, like this if you use the googlev3:
```bash
'The given key has gone over the requests limit in the 24'
geopy.exc.GeocoderQuotaExceeded: The given key has gone over the requests limit in the 24 hour period or has submitted too many requests in too short a period of time.
```

### Making GeoJSON

Now that you have a spreadsheet full of coordinate data, we can convert the CSV spreadsheet into a format that web maps like, like GeoJSON.  GeoJSON is a web mapping standard of JSON data.  There are a couple of ways to make GeoJSON

1. The easiest, recommended way is to use a UI tool developed by Mapbox: http://geojson.io.  All you have to do is click and drag your csv file into the data window (the right side of the screen, next to the map), and it will automatically format your data into GeoJSON for you[6]. You can select the 'GeoJSON' option under 'Save.'

**Ian: Want to do put a screenshot here?**

2. To do it programmatically, you can use ogr2ogr.  You'll need to install GDAL[7], a commonly used GIS library that is frequently used to automate processes in python.  If you want to batch convert 500 CSV files into GeoJSON, this will be the way to go. [8]

**Using ogr2ogr (Skip this part if you are using geojson.io)**

Once you have GDAL installed, set the path:

*Mac only?*

```bash
export PATH=/Library/Frameworks/GDAL.framework/Programs:$PATH
```

**Create a VRT file**

**Ian: make explicit to skip this section too if you used geojson.io?**

VRT is an XML-based template that is used to convert non geographic data into a geographic data format without creating intermediate files.  Make sure that OGRVRTLayer, SrcDataSource have the same name as your filename (census_geocoded.vrt).  Indicate all of the properties based on the column name such as the population values for every census to include your geojson. This is what your VRT file will look like:


```xml
<OGRVRTDataSource>
    <OGRVRTLayer name="census_geocoded">
        <SrcDataSource>census_geocoded.csv</SrcDataSource>
        <GeometryType>wkbPoint</GeometryType>
        <LayerSRS>WGS84</LayerSRS>
        <GeometryField encoding="PointFromColumns" x="longitude" y="latitude"/>
        <Field name="ID" src="ID" type="String"/>
        <Field name="Area_Name" src="Area_Name" type="String"/>
        <Field name="Area_Code" src="Area_Code" type="String"/>
        <Field name="Pop_1801" src="Pop_1801" type="Integer"/>
		<Field name="Pop_1811" src="Pop_1811" type="Integer"/>
		<Field name="Pop_1821" src="Pop_1821" type="Integer"/>
	<!-- etc...not all of the columns are included here -->
		<Field name="Pop_1971" src="Pop_1971" type="Integer"/>
		<Field name="Pop_1981" src="Pop_1981" type="Integer"/>
		<Field name="Pop_1991" src="Pop_1991" type="Integer"/>
		<Field name="Pop_2001" src="Pop_2001" type="Integer"/>
    </OGRVRTLayer>
</OGRVRTDataSource>
```

**Run the command to output your geojson**

```bash
ogr2ogr -f GeoJSON output.geojson census_geocoded.vrt
```

Your GeoJSON output should look something like this:

```json
{
"type": "FeatureCollection",
"crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
                                                                                
"features": [
{ "type": "Feature", "properties": { "ID": "1000", "Area_Name": "City of London", "Area_Code": "00AA", "Pop_1801": 129000, "Pop_1811": 121000, "Pop_1821": 125000, "Pop_1831": 123000, "Pop_1841": 124000, "Pop_1851": 128000, "Pop_1861": 112000, "Pop_1871": 75000, "Pop_1881": 51000, "Pop_1891": 38000, "Pop_1901": 27000, "Pop_1911": 20000, "Pop_1921": 14000, "Pop_1931": 11000, "Pop_1939": 9000, "Pop_1951": 5000, "Pop_1961": 4767, "Pop_1971": 4000, "Pop_1981": 5864, "Pop_1991": 4230, "Pop_2001": 7181 }, "geometry": { "type": "Point", "coordinates": [ -0.1277583, 51.5073509 ] } },
{ "type": "Feature", "properties": { "ID": "1001", "Area_Name": "Barking and Dagenham", "Area_Code": "00AB", "Pop_1801": 3000, "Pop_1811": 4000, "Pop_1821": 5000, "Pop_1831": 6000, "Pop_1841": 7000, "Pop_1851": 8000, "Pop_1861": 8000, "Pop_1871": 10000, "Pop_1881": 13000, "Pop_1891": 19000, "Pop_1901": 27000, "Pop_1911": 39000, "Pop_1921": 44000, "Pop_1931": 138000, "Pop_1939": 184000, "Pop_1951": 189000, "Pop_1961": 177092, "Pop_1971": 161000, "Pop_1981": 149786, "Pop_1991": 140728, "Pop_2001": 163944 }, "geometry": { "type": "Point", "coordinates": [ 0.1293497, 51.5464828 ] } },
```
Test this data out in http://geojson.io.  You should see points generated in the preview window.  That's your data!

To prepare it for Leaflet web map, you'll need to manipulate the geojson and turn it into a js data file.  Add a "var boroughs = " to the beginning of your GeoJSON data file. To do so, open it up in the text editor of your choice.

**Ian: var boroughs or var countries - the example below is a bit different. Can you explain what it's doing? Why do we need to do this? How could they do this for other collections?**
```js
var countries = {
"type": "FeatureCollection",
"crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
                                                                                
"features": [
{ "type": "Feature", "properties": { "ID": "1000", "Area_Name": "City of London", "Area_Code": "00AA", "Pop_1801": 129000, "Pop_1811": 121000, "Pop_1821": 125000, "Pop_1831": 123000, "Pop_1841": 124000, "Pop_1851": 128000, "Pop_1861": 112000, "Pop_1871": 75000, "Pop_1881": 51000, "Pop_1891": 38000, "Pop_1901": 27000, "Pop_1911": 20000, "Pop_1921": 14000, "Pop_1931": 11000, "Pop_1939": 9000, "Pop_1951": 5000, "Pop_1961": 4767, "Pop_1971": 4000, "Pop_1981": 5864, "Pop_1991": 4230, "Pop_2001": 7181 }, "geometry": { "type": "Point", "coordinates": [ -0.1277583, 51.5073509 ] } },
{ "type": "Feature", "properties": { "ID": "1001", "Area_Name": "Barking and Dagenham", "Area_Code": "00AB", "Pop_1801": 3000, "Pop_1811": 4000, "Pop_1821": 5000, "Pop_1831": 6000, "Pop_1841": 7000, "Pop_1851": 8000, "Pop_1861": 8000, "Pop_1871": 10000, "Pop_1881": 13000, "Pop_1891": 19000, "Pop_1901": 27000, "Pop_1911": 39000, "Pop_1921": 44000, "Pop_1931": 138000, "Pop_1939": 184000, "Pop_1951": 189000, "Pop_1961": 177092, "Pop_1971": 161000, "Pop_1981": 149786, "Pop_1991": 140728, "Pop_2001": 163944 }, "geometry": { "type": "Point", "coordinates": [ 0.1293497, 51.5464828 ] } },

```
 Now save this GeoJSON as 'census.js'.

### You finally have GeoJSON...but

If you've tested your GeoJSON data, you might notice that not every point is geolocated correctly.  We know that every area name is a borough of London, but points appear all over United Kingdom, and some aren't located even in the country.

To make the results more accurate, you should include an additional column called 'Country' and put 'United Kingdom' in every row of your data. For even greater accuracy add 'City' and put 'London' in every row of your data to provide additional context for your data.  Now change your python script to combine the Area Name and City column to geocode your data:

**Ian: screenshot of an example of this? I wasn't quite sure where this new column shoudl go.**

```python
    io['helper'] = io['Area_Name'].map(str) + " " + io['Country']
	io['latitude'] = io['helper'].apply(geolocator.geocode).apply(lambda x: (x.latitude))
	io['longitude'] = io['helper'].apply(geolocator.geocode).apply(lambda x: (x.longitude))
```

Turn your data into GeoJSON and test it out in GeoJSON.io.  Does it look better now?  Good!

## I now have good GeoJSON data.  Lets make a map!

Setup a server to test our maps. If you're in your working directory, from the command line, run 

*Mac only*

```
python -m SimpleHTTPServer
```
In your browser go to localhost:8000 and you should see the files you've been working with so far. 

Now in your text editor open a new document and save it as an html file (mymap.html).  If you want to do a quick test, copy and paste the text below, refresh your localhost:8000 and open the html file in your browser.

**Ian: What do they need to change to make this work on their machine? i.e. just change the 'census.js' line. And maybe brief note what SimpleHTTPServer is.**

```html
<!DOCTYPE html>
<head>
<link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.6.4/leaflet.css" />
<!--[if lte IE 8]>
    <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.6.4/leaflet.ie.css" />
<![endif]-->
 
<script src="http://cdn.leafletjs.com/leaflet-0.6.4/leaflet.js"></script>
<script src="census.js" type="text/javascript"></script>
<style>
#map {
	width:960px;
	height:500px;
}
</style>
</head>
 
<body>
	<div id="map"></div>
<script>
window.onload = function () {
 	var map = L.map('map').setView([0.0,-10.0], 2);
 	
	L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
		attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
	}).addTo(map);

	var countryStyle = {
		'color': "#000",
		'weight': 2,
		'opacity': 0.6
	};
	
	function popup(feature, layer) {
		if (feature.properties && feature.properties.Area_Name) {
			layer.bindPopup(feature.properties.Area_Name);
		}
	}
	
	L.geoJson(boroughs, {
		onEachFeature: popup,
		style: countryStyle
	}).addTo(map);
};
</script>
</body>
</html>


```

Do you see a map now?  Good! If not, you can troubleshoot by inspecting the browser, or by going back and retracing your steps.


### OK WHAT did I just make?

You made a web map!  Web maps use map tiles, which are pixel based images (rasters) of maps that contain geographical data. This means that each pixel of a map tile has been georeferenced, or assigned a coordinate based on the location that they represent.  When you zoom in and out of a web map, you are getting a whole new set of tiles to display at each zoom level. [9] GeoJSON (which you are now familiar with) is a widely used data standard for web mapping.  In our example, we are using an open-source Javascript library called Leaflet[10] to help us build our web map.  With frameworks like Leaflet or Google Maps Javascript API, you're not building a map completely from scratch, rather, you're using pre-written functions and controls that helps you customize your own map in code.

Lets go through what each part of the code is doing.  

```html
<!DOCTYPE html>
<head>
<link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.6.4/leaflet.css" />
<!--[if lte IE 8]>
    <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.6.4/leaflet.ie.css" />
<![endif]-->
 
<script src="http://cdn.leafletjs.com/leaflet-0.6.4/leaflet.js"></script>
<script src="census.js" type="text/javascript"></script>
<style>
#map {
	width:960px;
	height:500px;
}
</style>
</head>
```

The above code is the first section, or header of your html document, you're linking to the external javascript library and css stylesheets provided by leaflet.  You're also linking to your data file, 'census.js'.  There's also a bit of CSS styling here to specify the size of your map.

```html
<body>
	<div id="map"></div>
```
Then, you're declaring the body and where you want the map to go on your page.

```html
<script>
window.onload = function () {
 	var map = L.map('map').setView([0.0,-10.0], 2);	
```

Javascript provides the functionality. Here you're specifying the map to load and setting the viewport for your map.  The viewport coordinates '[0.0,-10.0], 2' means that you're setting the centre of the map to be 0.0, -10.0 and at a zoom level of 2.

```javascript
	L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
		attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
	}).addTo(map);

	var countryStyle = {
		'color': "#000",
		'weight': 2,
		'opacity': 0.6
	};
```
You're creating a layer here for your basemap.  The basemap is the tiles provided by OpenStreetMap that provides places, streetnames found on maps.  The layer is added to the map. 

```javascript
	function popup(feature, layer) {
		if (feature.properties && feature.properties.Area_Name) {
			layer.bindPopup(feature.properties.Area_Name);
		}
	}

```
Each point of data is represented by an icon.  Now, we're adding a popup to each point of data.  When you click on an icon, it will display the name of the data point.

```javascript

	L.geoJson(boroughs, {
		onEachFeature: popup,
		style: countryStyle
	}).addTo(map);
};

```

```html
</script>
</body>
</html>
```

This is your very first web map!  Now lets play around with it.

### Left to write:
- Exercises, add screenshots
- More information about geolocators and comparing them

Exercise 1
change the viewport to [0.0,-10.0], 2

Exercise 2
add the 1981 population property to each marker popup

Exercise 3
change the data source to stations.geojson

Exercise 4
add a mapbox tileset/basemap layer

Exercise 5
add your own custom icon




[1] If you're following along in Github, this is step 1: https://github.com/kimpham54/proghist-mappingAPI/tree/master/step1-csv

[2]If you're following along in Github: https://github.com/kimpham54/proghist-mappingAPI/tree/master/step2-geocode

[3] https://github.com/geopy/geopy

[4] http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe

[5] http://geopy.readthedocs.org

[6] http://www.nypl.org/blog/2015/01/05/web-maps-primer?utm_campaign=SocialFlow&utm_source=facebook.com&utm_medium=referral

[7] http://www.kyngchaos.com/software/frameworks

[8] If you're following along in Github: https://github.com/kimpham54/proghist-mappingAPI/tree/master/step3-vrt

[9] If you're following along in Github: https://github.com/kimpham54/proghist-mappingAPI/tree/master/step4-webmap

[10] http://leafletjs.com/reference.html



### Next part of the lesson

Mapbox, Cartodb, stamen, so many other plugins you can use with leaflet
popup of info for points
time based data
county boundaries instead of points - you'd need to do a spatial join.  easier with GIS, maybe we can do it with Python. https://github.com/martinjc/UK-GeoJSON, https://gist.github.com/kimpham54/2ecf1ad08de64c2d6a8e




3. run the geocoding api to generate lat/long coordinates, then write the coordinates to file - but how do you do that while keeping the original attribute data?  use Python script - read the CSV column you want to geocode (Area Name), add a hint like UK maybe, then output a new file the new CSV columns lat and lng - name columns according to convention that geojson likes

4. Create geoJSON from your CSV: ogr2ogr -f "GeoJSON" output.json census-historic-population-borough.csv
- Talk about the many different options, and why this may not be the best option
geojson.io, geojson lint
- for more commands, look at this cheat sheet: https://github.com/dwtkns/gdal-cheat-sheet


http://fredgibbs.net/tutorials/tutorial/extract-geocode-placenames-from-text-file/

Note: python's csv module doesn't like the formatting of a Mac-generated CSV (e.g. using Microsoft Excel on a Mac), to get around this issue, upload the csv to google drive and export from there

4b. use the geojson and run the geocoding api - good for small points but there's  a request limit here
API mashup: Google's Javascript API with the Geocoding API https://jsfiddle.net/kimpham54/qy4s0ghy/1/geocoding API
- original source: http://jsfiddle.net/P2QhE/
- Still need to modify this, avoid using jquery? have it read geojson attribute rather than entire file

5. 

###Check these out 
https://github.com/dwtkns/gdal-cheat-sheet
http://gis.stackexchange.com/questions/140219/what-are-some-ways-to-convert-a-csv-file-to-geojson-while-preserving-data-types

vrt files geojson
https://github.com/gavinr/csv-to-geojson


http://policeanalyst.com/using-the-google-geocoding-api-in-excel/
google my maps geocodes, doesn't give you lat/long though
http://sendai.hmdc.harvard.edu/cga_website_files/Geocoding/Instructions_for_using_the_Goolge_API_for_Work_Geocoder.pdf
http://fredgibbs.net/tutorials/tutorial/extract-geocode-placenames-from-text-file/
http://ask.metafilter.com/142871/Columnoriented-CSV-in-Python
http://geojson.org/geojson-spec.html#id2
http://ogre.adc4gis.com/
https://github.com/gavinr/csv-to-geojson
https://github.com/mapbox/csv2geojson
http://gis.stackexchange.com/questions/140219/what-are-some-ways-to-convert-a-csv-file-to-geojson-while-preserving-data-types
http://www.shanelynn.ie/massive-geocoding-with-r-and-google-maps/

http://gis.stackexchange.com/questions/15052/how-to-avoid-google-map-geocode-limit

https://developers.google.com/maps/tutorials/fundamentals/adding-a-google-map

https://procomun.wordpress.com/2013/09/20/r-geojson-and-github/
https://danieljhocking.wordpress.com/2013/09/21/json-geojson-bash-and-r/







## Data Preparation

- Start with CSV and want to translate it into geoJSON.
- Often a lot of the work in creating a map is preparing the data. Talk about google maps and different data sources they accept.


1. Obtain csv data from github -
2. There are many ways to get to this data.  You can do it offline, or you can host it on a place like Google Docs.  Open data in google docs and use their Google Docs API:
  https://spreadsheets.google.com/feeds/list/1GN0DuxNn7xpkGNnFDWP4-5mdYs1XJqoSt1G2fDwu1SA/1/public/values?alt=json
  API changes
  put into JSONLINT.com and you can see it structured
3. now you have JSON.  now to turn it into geoJSON.  geojson.io
https://docs.google.com/spreadsheets/d/1GN0DuxNn7xpkGNnFDWP4-5mdYs1XJqoSt1G2fDwu1SA/pub?gid=1761435061&single=true&output=csv
https://docs.google.com/spreadsheets/d/1GN0DuxNn7xpkGNnFDWP4-5mdYs1XJqoSt1G2fDwu1SA/edit?usp=sharing


## Obtaining an API Key
1. For our purposes you can use their own key (will not allow you to do everything or make too many requests)

2. Instructions on how to get your own key are here: https://developers.google.com/console/help/new/?hl=en_US#api-keys
https://developers.google.com/maps/documentation/javascript/examples/map-simple
https://developers.google.com/console/help/new/?hl=en_US#installed-applications
Use a browser key.  Keys should not be shared with other individuals.  In fact, google will charge you if it’s accessed too many times.  if you want to monitor usage and for later development

Start your page
The map is built on a webpage.  You can work on it by starting up a simple webserver.
Start with an empty document.  Open up a text editor.  

Plotting Data
lat and long
plotting coordinates from a CSV file vs API
want address instead use geocoder


```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```
 
```python
s = "Python syntax highlighting"
print s
```
 
```
No language indicated, so no syntax highlighting. 
But let's throw in a <b>tag</b>.
```
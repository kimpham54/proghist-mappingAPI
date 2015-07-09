# Google Maps Tutorial


1. Obtain data from github https://github.com/Robinlovelace/Creating-maps-in-R/blob/master/data/census-historic-population-borough.csv

2. Install gdal https://trac.osgeo.org/gdal/wiki/DownloadingGdalBinaries
- run in terminal:
export PATH=/Library/Frameworks/GDAL.framework/Programs:$PATH

3. Create geoJSON from your CSV: ogr2ogr -f "GeoJSON" output.json census-historic-population-borough.csv
- Talk about the many different options, and why this may not be the best option
geojson.io, geojson lint

4. API mashup: Google's Javascript API with the Geocoding API https://jsfiddle.net/kimpham54/qy4s0ghy/1/geocoding API
- original source: http://jsfiddle.net/P2QhE/
- Still need to transform this into non jquery, into a way to read geojson attribute rather than entire file




## Data Preparation

- Start with CSV and want to translate it into geoJSON.
- Often a lot of the work in creating a map is preparing the data. Talk about google maps and different data sources they accept.


1. Obtain csv data from github -
2. There are many ways to get to this data.  You can do it offline, or you can host it on a place like Google Docs.  Open data in google docs and use their Google Docs API:
  https://spreadsheets.google.com/feeds/list/1GN0DuxNn7xpkGNnFDWP4-5mdYs1XJqoSt1G2fDwu1SA/1/public/values?alt=json
  API changes
  put into JSONLINT.com and you can see it structured
3. now you have JSON.  now to turn it into geoJSON.  geojson.io



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





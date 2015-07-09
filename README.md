# Google Maps Tutorial
## Data Preparation

- Start with CSV and want to translate it into geoJSON.
- Often a lot of the work in creating a map is preparing the data. Talk about google maps and different data sources they accept.


1. Obtain csv data from github -
2. There are many ways to get to this data.  You can do it offline, or you can host it on a place like Google Docs.  Open data in google docs and use their Google Docs API:
  https://spreadsheets.google.com/feeds/list/1GN0DuxNn7xpkGNnFDWP4-5mdYs1XJqoSt1G2fDwu1SA/1/public/values?alt=json
  API changes
  put into JSONLINT.com and you can see it structured
3. now you have JSON.  now to turn it into geoJSON.  geojson.io

avoid using too many libraries
without using PHP and manually creating geojson
without having a backend
without using GIS


## Obtaining an API Key
1. For our purposes you can use their own key (will not allow you to do everything)

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



future proofing by using java script libraries - other people will maintain, it's not just you
part of a community that is more vigilant

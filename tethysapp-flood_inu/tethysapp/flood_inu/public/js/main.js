

var mymap = L.map('mapid').setView([19.037027, 101.799377], 7);

const basemap = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
maxZoom: 18,
id: 'mapbox/streets-v11',
tileSize: 512,
zoomOffset: -1,
accessToken: 'pk.eyJ1Ijoic2tkODYyIiwiYSI6ImNrZGhudjQydzEydjYyenQxZnQ3MzFvMWQifQ.wyoJjHhopkiAZyGSeQY8ow'
});


var tonlesap = L.tileLayer.wms("http://127.0.0.1:7000/thredds/wms/testAll/20110101.nc", {
    layers: 'extents',
    format: 'image/png',
    transparent: true,
    crossOrigin: false,         opacity: 1,         BGCOLOR: '0x000000',         styles: 'boxfill/rainbow',         colorscalerange: '-20,0',

}).addTo(mymap);

var control = L.control.layers({"Mapbox Basemap Layer": basemap}, {"Layer from thredds": tonlesap}).addTo(mymap); 

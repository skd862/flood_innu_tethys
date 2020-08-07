function getNewLayer(date) {
    // you probably want to replace this url for thredds with a custom setting (refer to hackathon workshop)
    // keep the + date + ".nc" part, just replace the first part of the url with a custom setting value
    return L.tileLayer.wms("http://0.0.0.0:7000/thredds/wms/thredds-demo/" + date + ".nc", {
        layers: 'extents',  // this may not be the name of the variable you end up using in all the netcdfs
        format: 'image/png',  // DO NOT switch this to jpeg, kml, etc
        transparent: true,  // DO NOT change this
        crossOrigin: false,  // DO NOT change this
        opacity: 1,  // the data which gets colored over the map appears with an opacity of 100%
        BGCOLOR: '0x000000',  // this makes the places where the layer has no data appear invisible/transparent
        styles: 'boxfill/rainbow',  // there are many coloring options and you can use custom ones
        colorscalerange: '-20,0',  // This may need some fine tuning
    }).addTo(mymap)
}
function generateControlsBox() {
    return L.control.layers({"Open Street Map (Mapbox)": basemap}, {"Layer from thredds": tonlesap}).addTo(mymap);
}

var mymap = L.map('mapid').setView([19.037027, 101.799377], 7);

const basemap = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1Ijoic2tkODYyIiwiYSI6ImNrZGhudjQydzEydjYyenQxZnQ3MzFvMWQifQ.wyoJjHhopkiAZyGSeQY8ow'
}).addTo(mymap);

const datePicker = $("#date");
let tonlesap = getNewLayer("20110101");
let control = generateControlsBox();

// How to make the layer change when the user picks a new date
// When the user picks a new date (in code speak: when the date picker value is changed)
$("#submit_date").click(function() {
    // first we want to remove the layer that is already on the map
    mymap.removeLayer(tonlesap);
    control.removeLayer(tonlesap);
    mymap.removeControl(control);

    // then we want to request a new layer- to do that we need to know what the selected date is
    let newDate = datePicker.val().split("/")
    console.log('adding new layer for date ' + newDate[2] + newDate[0] + newDate[1])
    tonlesap = getNewLayer(newDate[2] + newDate[0] + newDate[1])

    // last we can update the controls menu for the map layers
    control = generateControlsBox();
})
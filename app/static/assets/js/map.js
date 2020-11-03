var map = L.map('mapid').setView([-34.9187, -57.956], 13);


L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoiZ2FzdG9uZ2luZXN0ZXQiLCJhIjoiY2toMTc5cTEzMGdtZzJyb3dicmh2MzN2YiJ9.lT2Tq_6BTzjaVtvn7N2lRw'
}).addTo(map);



var marker = L.marker([-34.9187, -57.956],{draggable:true}).addTo(map);

function onMapClick(e) {
    marker
        .setLatLng(e.latlng)
}

const addSearchControl = () => {
    L.control.scale().addTo(map);
    let searchControl = new L.esri.Controls.Geosearch().addTo(map);
    
    let results = new L.LayerGroup().addTo(map);

    searchControl.on('results',(data) => {
        results.clearLayers();

        if(data.results.length > 0) {
            addMarker(data.results[0].latlng);
        };
    });
};

map.on('click', onMapClick);

window.onload = () => {
    initializeMap('mapid');
}
let map;
let marker;

const initializeMap =  (selector) => {
    mapboxgl.accessToken = 'pk.eyJ1IjoiZ2FzdG9uZ2luZXN0ZXQiLCJhIjoiY2toMTc5cTEzMGdtZzJyb3dicmh2MzN2YiJ9.lT2Tq_6BTzjaVtvn7N2lRw';
    map = new mapboxgl.Map({
        container: selector,
        style: 'mapbox://styles/mapbox/streets-v11',
        //primero la longitud despues latitud (si no , te lleva al mar)
        center: [-57.956, -34.9187],
        zoom: 13
        });
         
        map.addControl(
            new MapboxGeocoder({
            accessToken: mapboxgl.accessToken,
            mapboxgl: mapboxgl
            })
            );

    map.on('click', onMapClick);

};

function onMapClick(e) {
    addMarker(e.latlng);
};


const addMarker =  ({lat , lng}) => {
    if(marker) marker.remove();
    
    marker = L.marker([lat, lng],{draggable:true}).addTo(map);
};



const submitHandler = (event) => {
    if (!marker) {
        event.preventDefault();
        alert('Debes seleccionar una ubicación en el mapa.')
    }
    else {
        latlng = marker.getLatLng();
        document.getElementById('lat').setAttribute('vsalue',latlng.lat)
        document.getElementById('lng').setAttribute('value',latlng.lng)
    }
};


window.onload = () => {
    initializeMap('mapid');
};
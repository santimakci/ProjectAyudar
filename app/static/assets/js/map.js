let map;
let marker;
let geocoder;

const initializeMap = (selector) => {
    mapboxgl.accessToken = 'pk.eyJ1IjoiZ2FzdG9uZ2luZXN0ZXQiLCJhIjoiY2toMTc5cTEzMGdtZzJyb3dicmh2MzN2YiJ9.lT2Tq_6BTzjaVtvn7N2lRw';
    map = new mapboxgl.Map({
        container: selector,
        style: 'mapbox://styles/mapbox/streets-v11',
        //primero la longitud despues latitud (si no , te lleva al mar)
        center: [-57.956, -34.9187],
        zoom: 13
    });


    geocoder = map.addControl(
        new MapboxGeocoder({
            accessToken: mapboxgl.accessToken,
            mapboxgl: mapboxgl,
            placeholder: 'Buscar..',
            marker: false
        })
    );

    map.on('click', onMapClick);
};

const initializeView = ({
    lng,
    lat
}) => {

    marker = new mapboxgl.Marker({
            draggable: false
        })
        .setLngLat([lng, lat])
        .addTo(map);

    map.off('click', onMapClick);
};


function onMapClick(e) {
    addMarker(e.lngLat);
};


const addMarker = ({
    lng,
    lat
}) => {
    if (marker) marker.remove();

    marker = new mapboxgl.Marker({
            draggable: true
        })
        .setLngLat([lng, lat])
        .addTo(map);
};


const submitHandler = (event) => {
    if (!marker) {
        event.preventDefault();
        alert('Debes seleccionar una ubicación en el mapa.')
    } else {
        latlng = marker.getLngLat();
        document.getElementById('lat').setAttribute('value', latlng.lat)
        document.getElementById('lng').setAttribute('value', latlng.lng)
    }
};



initializeMap('mapid');
lat = document.getElementById('lat').getAttribute('value');
lng = document.getElementById('lng').getAttribute('value');
if (lat != null && lng != null) {
    if (document.getElementById('lat').disabled = !true) {
        addMarker({
            lng,
            lat
        });
    } else {
        initializeView({
            lng,
            lat
        });
    }
    map.setCenter({
        lng,
        lat
    })
}
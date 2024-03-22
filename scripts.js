window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-RBBQN6B0EM');

mapboxgl.accessToken = 'pk.eyJ1Ijoia2FsYWthciIsImEiOiJjaW4yNHBvMDMwYjZrdXBra29qYmxnOGM5In0.4Lh20IMXH60mscRm5EKuNw';
// Create the map
const map = new mapboxgl.Map({
	container: 'map',
	style: 'mapbox://styles/kalakar/clgnvvub2007301qn2ym83hwn',
	center: [78.194226, 22.372645],
	zoom: 2,
	minZoom: 3.5, // note the camel-case
});
// Add marker labels for each location 
var url = "baithakji.json"
map.on('load', function() {
	// Add a GeoJSON source containing place coordinates and information.
	map.addSource('geojson', {
		'type': 'geojson',
		'data': 'https://nirja-desai.github.io/kalakar.github.io/geo_json_final.geojson',
		// 'data': url,
		cluster: true,
		clusterMaxZoom: 8, // Max zoom to cluster points on
		clusterRadius: 23 // Radius of each cluster when clustering points (defaults to 50)
	});
	map.addLayer({
		'id': 'poi-labels',
		'type': 'symbol',
		'source': 'geojson',

		'layout': {
			'text-field': ['get', 'name'],
			'text-variable-anchor': ['top'],
			'text-radial-offset': 1.5,
			'text-justify': 'auto',
			// 'icon-image': 'bhagvat.svg'
			'icon-image': ['concat', ['get', 'icon'], '-15'],
			'text-font': ["Lato Bold"],
			'text-transform': "uppercase"

		},

		"paint": {
			"text-color": "#264163",
			"text-halo-width": 1.5,
			"text-halo-color": "#EFE9D8"
		}
	});
});

////////////////////////
///// RASTER LAYER /////
////////////////////////

// Function to toggle image visibility
function toggleImage() {
	var imageLayer = map.getLayer('raster-tileset-layer');
	if (imageLayer) {
		map.setLayoutProperty('raster-tileset-layer', 'visibility', document.getElementById('toggleCheckbox').checked ? 'visible' : 'none');
		map.setLayoutProperty('poi-labels', 'visibility', document.getElementById('toggleCheckbox').checked ? 'none' : 'visible');
		var markerContainer = document.getElementById('map');
    	markerContainer.classList.toggle('hidden-markers');
	}
}

// Add the raster image as an overlay layer
map.on('load', function() {
	map.addSource('raster-tileset-source', {
		'type': 'raster',
		'url': 'mapbox://kalakar.26577fae'
	});

	map.addLayer({
		'id': 'raster-tileset-layer',
		'type': 'raster',
        'source': 'raster-tileset-source',
		'layout': {
            'visibility': 'none' // Set visibility to 'none' initially
		}
	});
});

// Get the geoJSON data again from the github page and load it in as JSON
// so that it can be used by the marker and popup functions
fetch('https://nirja-desai.github.io/kalakar.github.io/geo_json_final.geojson')
	.then(function(response) {
		return response.json();
	})
	.then(function(data) {
		// Do something with the GeoJSON data
		for (const feature of data.features) {
			// create a HTML element for each feature
			const el = document.createElement('div');
			// get description for each feature
			const name = feature.properties.name
			const description = feature.properties.description
			const image = "./images/" + feature.properties.image
			// get the correspnding market based on gupt property
			if (feature.properties.gupt) {
				el.className = 'marker_gupt';
			} else {
				el.className = 'marker';
			}
			// make a marker for each feature and add it to the map
			new mapboxgl.Marker(el).setLngLat(feature.geometry.coordinates)
				// .setLngLat(feature.properties.name)
				.setPopup(new mapboxgl.Popup({
						offset: 25
					}) // add popups
					.setHTML(`
                      <h3>${name}</h3>
                      <img src=${image} style="width: 100%; height: auto;">
                      <p>${description}<p>
                      `)).addTo(map);
		}
	});
// add markers to map
// import * as data from './geo_json_final.json';
// const geo_test = data;

//////////////////////
//COLLAPSABLE BUTTON//
//////////////////////

// Function to toggle collapsible content
// function toggleCollapsible() {
// 	var content = document.querySelector('.content');
//     if (content.style.display === "none") {
//         content.style.display = "block";
//     } else {
//         content.style.display = "none";
//     }
// }

console.log("Script loaded!"); // Debugging statement

var coll = document.getElementsByClassName("collapsible");
console.log("Number of buttons found:", coll.length); // Debugging statement

var coll = document.getElementsByClassName("collapsible");
var i;
for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var content = this.parentNode.querySelector(".content");
		console.log(content);
        if (content.style.maxHeight) {
            content.style.maxHeight = null;
        } else {
            content.style.maxHeight = content.scrollHeight + "px";
        }
    });
}

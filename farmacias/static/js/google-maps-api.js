var map;

console.log({{ pharmacy.lat|tojson }});

function initMap() {
	map = new google.maps.Map(document.getElementById('map'), {
		center: {lat: -34.6188773, lng: -68.3251669},
		/*center: { lat: lat, lng: lng },*/
		zoom: 15
	});
}

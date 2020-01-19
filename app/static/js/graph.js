
function initMap() {
  var directionsService = new google.maps.DirectionsService();
  var directionsRenderer = new google.maps.DirectionsRenderer();
  var cycleRenderer = new google.maps.DirectionsRenderer();
  var transitRenderer = new google.maps.DirectionsRenderer();

  var davis = new google.maps.LatLng(38.5569785, -121.778473,12.63);
  var mapOptions = {
    zoom:7,
    center: davis
  }
  var map = new google.maps.Map(document.getElementById('map'), mapOptions);
  directionsRenderer.setMap(map);
  cycleRenderer.setMap(map);
  transitRenderer.setMap(map);

  var onChangeHandler = function() {
          calcRoute(directionsService, directionsRenderer, cycleRenderer, transitRenderer);
        };
  document.getElementById('mode').addEventListener('change', onChangeHandler);

}

function calcRoute(directionsService, directionsRenderer) {
  var start = "UC Davis";
  var end = "Davis DMV";

  //var travelModes = ["DRIVING", "BICYCLING", "TRANSIT"];
  var travelMode = document.getElementById('mode').value;
    var request = {
      origin: start,
      destination: end,
      travelMode: travelMode
    };
    directionsService.route(request, function(result, status) {
    if (status == 'OK') {
      directionsRenderer.setDirections(result);
    }
  });

}
    //<script async defer
    //</script>
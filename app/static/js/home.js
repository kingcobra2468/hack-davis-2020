var start_pos = document.getElementById('searchTextField1');
var destination_pos = document.getElementById('searchTextField2');

function initialize() {

    new google.maps.places.Autocomplete(start_pos);
    new google.maps.places.Autocomplete(destination_pos);
}
    
$('body').bind('beforeunload',function(){
    document.getElementById("addr_form").reset();
 });

google.maps.event.addDomListener(window, 'load', initialize);
function geocodeAddress() {
    var pref = document.getElementById('id_pref').value;
    var city = document.getElementById('id_city').value;
    var street_address = document.getElementById('id_street_address').value;
    console.log(pref);
    console.log(city);
    console.log(street_address);
    address = pref + city + street_address;
    console.log(address);


    var geocoder = new google.maps.Geocoder();
    geocoder.geocode( { 'address': address}, function(results, status) {
      if (status == 'OK') {
      //   map.setCenter(results[0].geometry.location);
        // var marker = new google.maps.Marker({
        //     map: map,
        //     position: results[0].geometry.location
        // });
        var lat = results[0].geometry.location.lat()
        var lng = results[0].geometry.location.lng()
        document.getElementById('id_lat').value = trim_num(lat)
        document.getElementById('id_lng').value = trim_num(lng)
      } else {
        alert('Geocode was not successful for the following reason: ' + status);
      }
    });
}


function trim_num(x) {
    return Number.parseFloat(x).toFixed(7);
}
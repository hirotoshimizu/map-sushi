var map;

var marker = [],
    infoWindow = [];

function get_latlng(callback) {
  navigator.geolocation.getCurrentPosition(
    function(pos){
      callback(pos.coords.latitude, pos.coords.longitude);
    },
    function(err){
      var errorMessage="現在地の取得ができないため「東京駅」近辺の店舗情報を表示しております。"
      alert(errorMessage);
      callback(35.68140, 139.76710);
    }
  );
}

$(window).on('load', function(){
  get_latlng(initMap);
})

function initMap(gmap_lat, gmap_lng) {
  const mapLatLng  = {lat:gmap_lat, lng: gmap_lng};
  map = new google.maps.Map(document.getElementById("map"), {
    zoom: 10,
    center: mapLatLng,
    mapId: "d10bd85f6c1c7af3",
    mapTypeControl: false,
  });

  google.maps.event.addListenerOnce(map, 'bounds_changed', function(){
    update_shops();
  });
  
  google.maps.event.addListener(map, 'dragend', function(){
    update_shops();
  });

  map.addListener('zoom_changed', () =>{
    update_shops();
  });
  
}

function delete_marker() {
  for (var i = 0; i < marker.length; i++) {
      marker[i].setMap(null);
      infoWindow[i].setMap(null);
  }
  marker = [];
  infoWindow = [];
}

function search(param) {
  var data = '';
  $('input[name="rating"]:checked').each(function(){
    param+=(data==""?"":"&")+"&rating="+encodeURIComponent($(this).val());
  });
  search_ajax(param);
}

$(function(){
  $('input[name="rating"]').change(function() {
    update_shops();
  });
});

var cordinate = '';
function update_shops() {
  pos = map.getBounds();
  latlng = map.getCenter();
  north = pos.getNorthEast().lat();
  south = pos.getSouthWest().lat()
  east = pos.getNorthEast().lng()
  west = pos.getSouthWest().lng()
  search(
    cordinate = "north=" + north + "&south=" + south + "&east=" + east + "&west=" + west
  )
}

function update_marker(restaurants){
  if (typeof restaurants ==  "object"){
    for(var i in restaurants){
      var restaurant = restaurants[i];
      const ratingSwitch = {
        'THREE': '三つ星',
        'TWO': '二つ星',
        'ONE': '一つ星',
        'BIB': 'ビブグルマン',
        'TMP': 'ミシュランプレート'
      }
      marker[i] = new google.maps.Marker({
          title: restaurant['name'],
          position: new google.maps.LatLng(restaurant['lat'], restaurant['lng']),
          map: map,
      });
      var markerContent = "";
      markerContent += "<div class=\"marker-detail\">\n";
      markerContent += "<a target='_blank' href='" + restaurant['id'] + "'>\n";
      markerContent += "<div class=\"shop\">\n";
      markerContent += "<h4>" + restaurant['name'] + "</h4>\n";
      markerContent += "<p>" + ratingSwitch[restaurant['rating']] + "</p>\n";
      markerContent += "<p>" + restaurant['price'] + "</p>\n";
      markerContent += "</div>\n";
      markerContent += "</a>\n";
      markerContent += "</div>\n";
      infoWindow[i] = new google.maps.InfoWindow({
        content: markerContent,
      });
      markerEvent(i);
    }	
  }
}

function markerEvent(i) {
	marker[i].addListener('click', function() {
		hideAllInfoWindows(map);
		infoWindow[i].open(map, marker[i]);
    map.panTo(this.getPosition());
	});
}

function hideAllInfoWindows(map) {
	infoWindow.forEach(function(thisInfo) {
		thisInfo.close()
	});
}

function search_ajax(param) {
  $.ajax({
    type: 'GET',
    url: '/api/',
    data: param,
    success: function(data){
      delete_marker();
      update_marker(data);
    },
    dataType: 'json'
  });
}

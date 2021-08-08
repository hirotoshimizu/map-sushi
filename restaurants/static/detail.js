
// id を取得
const pathname = location.pathname

// let result = pathname.match(/([^\/.]+)/g);
const restaurant_id = pathname.replace( /\//g , "" ) ;


function _search_ajax(){
    var result = $.ajax({
        type: 'GET',
        url: "/api/"+ restaurant_id +"/",
        async: false
    }).responseText;
    return result;
}

var result_parse = JSON.parse(_search_ajax());

var gmap_lat = Number(result_parse['lat']);
var gmap_lng = Number(result_parse['lng']);


// 取得したデータを基に地図にピンを打って返却
function initMap() {
    const mapLatLng  = {lat: gmap_lat, lng: gmap_lng};
    map = new google.maps.Map(document.getElementById("map"), {
      zoom: 17,
      center: mapLatLng,
      mapId: "d10bd85f6c1c7af3",
      mapTypeControl: false,
    });
    new google.maps.Marker({
        position: mapLatLng,
        map,
    });
  }

$(window).on('load', function(){
  initMap(gmap_lat, gmap_lng)
})

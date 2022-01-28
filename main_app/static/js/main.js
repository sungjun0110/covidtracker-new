let map;
let infoWindow = new google.maps.InfoWindow();
DJANGO_STATIC_URL = '{{ STATIC_URL }}'
state = '{{ states }}'

$(document).ready(function() {
    let tt = $('#test')
    $('#test').on('change', function(){
        console.log($(this).val());
    })
})
// function initMap() {
//     map = new google.maps.Map(document.getElementById("map"), {
//         center: { lat: 40, lng: -97 },
//         zoom: 4,
//         minZoom:2,
//         maxZoom:7,
//     });

//     let markers = ['static/images/1.png']
//     // let marker = markers[0];

//     function marker(n){
//         // if (n > 0 && n < 10) return markers[0];
//         // else if (n > 10 && n < 100) return markers[1];
//         // else if (n > 100 && n < 1000) return markers[2];
//         // else if (n > 100 && n < 1000) return markers[3];
//         // else return markers[4];
//         return markers[0];
//     }

    

//     function initMarker(n) {
//         marker = new google.maps.Marker({
//             position: {lat: parseFloat(world_case_detail[i]["lat"]), lng: parseFloat(world_case_detail[i]["lng"])},
//             title: world_case_detail[i][0],
//             icon: markers[n],
//             map:map
//         });
//     }
// }

function initMap(){
    // Map options
    var options = {
      zoom: 4,
      center: { lat: 39, lng: -97 },
      minZoom: 4,
      maxZoom: 7,
    }

    // New map
    map = new google.maps.Map(document.getElementById('map'), options);

    const marker = new google.maps.Marker({
        position: { lat: 39, lng: -97 },
        map: map,
    })

    const infowindow = new google.maps.InfoWindow({
        content: DJANGO_STATIC_URL,
    });
    
    google.maps.event.addListener(marker, "click", () => {
        infowindow.open(map, marker);
    });
}
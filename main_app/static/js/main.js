let map;
function initMap(){
    // Map options
    var options = {
      zoom: 3,
      center: { lat: 39, lng: -97 },
      minZoom: 3,
      maxZoom: 7,
    }

    let covidTable = $('#covid-table tbody');
    let rawTable = covidTable.html();
    let tableData = rawTable.split('<td>').join('').split('</td>');
    tableData = tableData.slice(0, tableData.length - 1);
    let states = [];
    for (let i = 0; i < tableData.length; i++) {
        if (i % 5 === 0) {
            states.push([tableData[i]]);
        } else {
            states[states.length - 1].push(tableData[i]);
        }
    }

    // New map
    map = new google.maps.Map(document.getElementById('map'), options);

    const markers = [];
    states.forEach(state => {
        markers.push(new google.maps.Marker({
            position: { lat: Number(state[3]), lng: Number(state[4]) },
            map: map,
        }));
    });

    markers.forEach((marker, i) => {
        const infowindow = new google.maps.InfoWindow({
            content: `<p><b>${states[i][0]}</b></p><p>Confiremd: ${states[i][1]}</p>\n<p>Deaths: ${states[i][2]}</p>`,
        });

        google.maps.event.addListener(marker, "click", () => {
            infowindow.open(map, marker);
        });
    })
}

function moveTo(pos) {
      map.setZoom(6);
      map.panTo({ lat: pos[0], lng: pos[1] });
}

$('#covid-table tbody tr').click(function (){
    moveTo([Number($(this).children()[3].innerHTML), Number($(this).children()[4].innerHTML)]);
});
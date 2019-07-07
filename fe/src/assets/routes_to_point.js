import l from '../../../data/mst.json'

ymaps.ready(function () {

  /**
   * The coordinates to build a route to.
   * For example, set the coordinates of your office.
   */
  var targetCoords = [55.752, 37.616];

  // Initializing the map.
  var myMap = new ymaps.Map('map', {
    center: targetCoords,
    zoom: 3
  }, {
      // Limiting the number of search results.
      searchControlResults: 1,

      // Disabling autocentering at the found addresses.
      searchControlNoCentering: true,

      // Allowing buttons to have the necessary length.
      buttonMaxWidth: 150
    });




  for (var i = 0; i < l.length; i++) {
    var currentRoute = new ymaps.multiRouter.MultiRoute({

      referencePoints: [l[i]['city1']['coord'], l[i]['city2']['coord']],
      params: { routingMode: 'auto' }
    }, {
        wayPointStartIconLayout: "#",
        wayPointFinishIconLayout: "#",
      });
    var routeLine = new ymaps.GeoObject({
      geometry: {
        type: "LineString",
        coordinates: [
          l[i]['city1']['coord'],
          l[i]['city2']['coord']
        ]
      },
    }, {
        draggable: false,
        strokeColor: "#FFFF00",
        strokeWidth: 5
      });
    myMap.geoObjects.add(currentRoute)
    myMap.geoObjects.add(routeLine)
  }
});

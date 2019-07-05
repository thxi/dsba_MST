import l from '../../../data/mst_boruvka.json'

ymaps.ready(function () {

    /**
     * The coordinates to build a route to.
     * For example, set the coordinates of your office.
     */
    var targetCoords = [55.752, 37.616],

        // Initializing the map.
        myMap = new ymaps.Map('map', {
            center: targetCoords,
            zoom: 11
        }, {
                // Limiting the number of search results.
                searchControlResults: 1,

                // Disabling autocentering at the found addresses.
                searchControlNoCentering: true,

                // Allowing buttons to have the necessary length.
                buttonMaxWidth: 150
            });


    // var targetPoint = new ymaps.Placemark([61, 75], { iconContent: 'S' }, { preset: 'islands#redStretchyIcon' })
    // myMap.geoObjects.add(targetPoint)

    var currentRoute = new ymaps.multiRouter.MultiRoute({
        referencePoints: [[55.752, 37.616], [61, 75]],
        params: { routingMode: 'auto' }
    }, {
            boundsAutoApply: true
        })
    myMap.geoObjects.add(currentRoute)
    var currentRoute = new ymaps.multiRouter.MultiRoute({
        referencePoints: [[43, 131], [61, 75]],
        params: { routingMode: 'auto' }
    }, {
            boundsAutoApply: true
        })
    myMap.geoObjects.add(currentRoute)

    for (var i = 0; i < l.length; i++) {
        var currentRoute = new ymaps.multiRouter.MultiRoute({

            referencePoints: [l[i]['city1']['coord'], l[i]['city2']['coord']],
            params: { routingMode: 'auto' }
        }, {
                boundsAutoApply: true
            })
        myMap.geoObjects.add(currentRoute)
    }
});

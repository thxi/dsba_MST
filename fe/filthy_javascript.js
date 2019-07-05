var targetPoint = new ymaps.Placemark([61, 75], { iconContent: 'S' }, { preset: 'islands#redStretchyIcon' })
myMap.geoObjects.add(targetPoint)

var currentRoute = new ymaps.multiRouter.MultiRoute({
  referencePoints: [[55.752, 37.616], [61, 75]],
  params: { routingMode: 'auto' }
}, {
    boundsAutoApply: true
  })
myMap.geoObjects.add(currentRoute)

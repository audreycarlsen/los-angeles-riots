document.addEventListener( "DOMContentLoaded", function() {
  document.removeEventListener( "DOMContentLoaded", arguments.callee, false );

  var map = L.map('map', {
    scrollWheelZoom: false
  }).setView([34.055, -118.15], 9);

  var mapquestLayer = new L.TileLayer('http://{s}.mqcdn.com/tiles/1.0.0/map/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: 'Data, imagery and map information provided by <a href="http://open.mapquest.co.uk" target="_blank">MapQuest</a>,<a href="http://www.openstreetmap.org/" target="_blank">OpenStreetMap</a> and contributors.',
    subdomains: ['otile1','otile2','otile3','otile4']
  });

  map.addLayer(mapquestLayer);

  var data = {
    "type": "FeatureCollection",
    "features": victims_array
  };

  var dataLayer = L.geoJson(data, {
    onEachFeature: function(feature, layer) {
      layer.bindPopup("<a href='#dialog_" + feature.properties.id + "'>" + feature.properties.full_name +"</a>");
    }
  });

  map.addLayer(dataLayer);
});
// Store our API endpoint inside queryUrl
var queryUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";

// Perform a GET request to the query URL
d3.json(queryUrl, function(data) {
   
    //console.log(data);
// Once we get a response, send the data.features object to the createFeatures function
    createFeatures(data.features);
    console.log(data.features);
    
    
});

 // Define function to create the circle radius based on the magnitude
 function radiusSize(magnitude) {
  return magnitude * 20000;
}

// Define function to set the circle color based on the depth
function circleColor(depth) {
  if (depth < 10) {
    return "#a3f600"
  }
  else if (depth < 30) {
    return "#dcf400"
  }
  else if (depth < 50) {
    return "#f7db11"
  }
  else if (depth < 70) {
    return "#fdb72a"
  }
  else if (depth < 90) {
    return "#fca65d"
  }
  else {
    return "#ff5f65"
  }
}

function createFeatures(earthquakeData) {

    // Define a function we want to run once for each feature in the features array
    // Give each feature a popup describing the place and time of the earthquake
    function onEachFeature(feature, layer) {
      layer.bindPopup("<h3>" + feature.properties.place +"</h3><hr><p>" + feature.properties.mag +"<br>"+ feature.geometry.coordinates + "</p>");
    }
  
    // Create a GeoJSON layer containing the features array on the earthquakeData object
    // Run the onEachFeature function once for each piece of data in the array
    var earthquakes = L.geoJSON(earthquakeData, {
      pointToLayer: function(earthquakeData, latlng) {
        return L.circle(latlng, {
          radius: radiusSize(earthquakeData.properties.mag),
          color: circleColor(earthquakeData.geometry.coordinates[2]), 
          fillOpacity: 1, 
          stroke: true
        });
      },
      
      onEachFeature: onEachFeature
    });
  
    // Sending our earthquakes layer to the createMap function
    createMap(earthquakes);
  }
  
  function createMap(earthquakes) {

    // Define streetmap and darkmap layers
    var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
      attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
      tileSize: 512,
      maxZoom: 18,
      zoomOffset: -1,
      id: "mapbox/light-v10",
      accessToken: API_KEY
    });
  
  
    // Define a baseMaps object to hold our base layers
    var baseMaps = {
      "Light Map": lightmap
    };
  
    // Create overlay object to hold our overlay layer
    var overlayMaps = {
      Earthquakes: earthquakes
    };
  
    // Create our map, giving it the streetmap and earthquakes layers to display on load
    var myMap = L.map("map", {
      center: [
        37.09, -95.71
      ],
      zoom: 5,
      layers: [lightmap, earthquakes]
    });
  
    // Create a layer control
    // Pass in our baseMaps and overlayMaps
    // Add the layer control to the map
    L.control.layers(baseMaps, overlayMaps, {
      collapsed: false
    }).addTo(myMap);

// color function to be used when creating the legend
function getColor(d) {
  return d > 90? '#ff5f65' :
         d > 70 ? '#fca65d' :
         d > 50 ? '#fdb72a' :
         d > 30  ? '#f7db11' :
         d > 10  ? '#dcf400' :
                  '#a3f600';
}

     // Add legend to the map
var legend = L.control({ position: "bottomright" });
  
legend.onAdd = function (map) {
  
      var div = L.DomUtil.create("div", "info legend");
          mags = [0, 10, 30, 50, 70, 90];
          labels = [];
  
      // loop through our density intervals and generate a label with a colored square for each interval
      for (var i = 0; i < mags.length; i++) {
          div.innerHTML +=
          labels.push(
              '<i style="background:' + getColor(mags[i] + 1) + '"></i> ' +
              mags[i] + (mags[i + 1] ? '&ndash;' + mags[i + 1] + '<br>' : '+'));
      }
        div.innerHTML = labels.join('<br>');
      return div;
};
  
legend.addTo(myMap);
}
  
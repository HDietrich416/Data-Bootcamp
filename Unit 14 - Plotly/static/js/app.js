
function Charts(sample) {
    d3.json("samples.json").then(data => {
        var samples = data.samples;
        var filterArray = samples.filter(sampleObject => sampleObject.id == sample);
        var result = filterArray[0];
        var sample_values = result.sample_values;
        var otu_ids = result.otu_ids;
        var otu_labels = result.otu_labels;      

    //Bar Chart

       var trace1 = {

            x: sample_values.slice(0,10).reverse(), 
            y: otu_ids.slice(0,10).map(otuID => `OTU ${otuID}`).reverse(), 
            text: otu_labels.slice(0,10), 
            marker: {
                color: 'blue'},
                type:"bar",
                orientation: "h",
        };

        var sample_data = [trace1];

        var layout = {
            title: "Top 10 OTU",
            yaxis:{
                tickmode:"linear",
            },
            margin: {
                l: 100,
                r: 100,
                t: 100,
                b: 30
            }
        };
    
    Plotly.newPlot("bar", sample_data, layout);

    //Bubble Chart
        var trace2 = {
            x: otu_ids,
            y: sample_values,
            text: otu_labels,
            mode: 'markers',
            marker: {
            size: sample_values,
            color: otu_ids,
            colorscale:"Electric"
            }
        };
        var data = [trace2];
        var layout = {
            title: 'Bacteria Cultures per Sample',
            showlegend: false,
            hovermode: 'closest',
            xaxis: {title:"OTU (Operational Taxonomic Unit) ID " +sample},
            font: { color: "#49a81d", family: "Arial, Helvetica, sans-serif" },
            margin: {t:30}
        };
        Plotly.newPlot('bubble', data, layout); 


    });
    };
    Charts();

  
function init(){
    var selector = d3.select("#selDataset");
    
    d3.json("samples.json").then((data) =>{
        jsData = data;
        var subjectID = data.names;
        subjectID.forEach((ID) => {
            selector
            .append('option')
            .text(ID)
            .property('value', ID);
        });
    const firstbutton = subjectID[0];
    Charts(firstbutton);
          });
}

function optionChanged(newSample) {
    Charts(newSample);
   
}

init();

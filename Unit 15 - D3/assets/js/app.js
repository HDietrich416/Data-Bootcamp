    // SVG wrapper dimensions are determined by the current width and
    // height of the browser window.
    var svgWidth = 800;
    var svgHeight = 560;
  
    var margin = {
      top: 50,
      bottom: 50,
      right: 50,
      left: 50
    };
  
    var height = svgHeight - margin.top - margin.bottom;
    var width = svgWidth - margin.left - margin.right;
  
    // Append SVG element
    var svg = d3.select("#scatter")
      .append("svg")
      .attr("height", svgHeight)
      .attr("width", svgWidth);
  
    // Append group element
    var chartGroup = svg.append("g")
      .attr("transform", `translate(${margin.left}, ${margin.top})`);
  
    // Read CSV
    d3.csv("assets/data/data.csv").then(function(censusData) {
  
        console.log(censusData)
        
      // parse data
      censusData.forEach(function(data) {
        data.poverty = +data.poverty;
        data.healthcare = +data.healthcare;
        data.state = data.abbr;
      });
  
      // create scales
      var xLinearScale = d3.scaleLinear()
        .domain([8, (d3.max(censusData, d => d.poverty)+2)])
        .range([0, width]);
  
      var yLinearScale = d3.scaleLinear()
        .domain([4, (d3.max(censusData, d => d.healthcare)+2)])
        .range([height, 0]);
  
      // create axes
      var xAxis = d3.axisBottom(xLinearScale);
      var yAxis = d3.axisLeft(yLinearScale);
  
      // append axes
      chartGroup.append("g")
        .attr("transform", `translate(0, ${height})`)
        .call(xAxis);
  
      chartGroup.append("g")
        .call(yAxis);
  
      // append circles
      var circlesGroup = chartGroup.selectAll("circle")
        .data(censusData)
        .enter()
        .append("circle")
        .attr("cx", d => xLinearScale(d.poverty))
        .attr("cy", d => yLinearScale(d.healthcare))
        .attr("r", "9")
        .classed("stateCircle", true)
        .attr("stroke-width", "1");

    // State abbreviations
    chartGroup.selectAll("text")
      .data(censusData)
      .enter()
      .append("text")
      .attr("x", (d,i) => xLinearScale(d.poverty))
      .attr("y", d => (yLinearScale(d.healthcare-0.18)))
      .classed("stateText", true)
      .text(d => d.state);
      
        
    // Create axes labels
    chartGroup.append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 0 - margin.left)
      .attr("x", 0 - (height / 2))
      .attr("dy", "1em")
      .attr("class", "axisText")
      .text("Lacks Healthcare (%)");


    chartGroup.append("text")
      .attr("transform", `translate(${width / 2}, ${height + margin.top -10})`)
      .attr("class", "axisText")
      .text("In Poverty (%)");
    
    

  
    }).catch(function(error) {
      console.log(error);
    });




  
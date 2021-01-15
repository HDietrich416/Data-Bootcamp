// from data.js
var tableData = data;

// Select the button

var button = d3.select("#filter-btn")

// Select the form

var form = d3.select("form");

// Select the table body

var tableBody = d3.select("tbody")

// Create event handles

button.on("click", runEnter);
form.on("submit", runEnter);

// Complete the event handler for the form
function runEnter() {

    // Prevent the page from refreshing
    d3.event.preventDefault();

    // Select the input element 
    var inputDate = d3.select("#datetime");

    // Get the value property of the input element
    var inputValue = inputDate.property("value");

    // Filter data based on input date
    var filteredData = tableData.filter(data => data.datetime === inputValue);

    // Clear table body of previous filter

    tableBody.html(" ");
    
    //Loop through filtered data and add to table data

    filteredData.forEach(function(item) {

        var row = tableBody.append("tr");

        Object.entries(item).forEach(function([key, value]){
            var cell = row.append("td");
            cell.text(value);


        });

    });

};
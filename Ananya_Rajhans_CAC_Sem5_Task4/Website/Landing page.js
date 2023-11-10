var trace1 = {
  x: ['All Races/Ethnicities', 'White', 'Black', 'Hispanic', 'Asian'],
  y: [821, 899, 704, 642, 1024],
  mode: 'markers',
  name: '2019 Female Earnings (in $)',
  marker: {
    size: [10, 20, 30, 40, 50],  // You can adjust the marker sizes as needed
    color: 'blue'  // Assigning blue color to female data points
  }
};

var trace2 = {
  x: ['All Races/Ethnicities', 'White', 'Black', 'Hispanic', 'Asian'],
  y: [1007, 1147, 769, 747, 1336],
  mode: 'markers',
  name: '2019 Male Earnings (in $)',
  marker: {
    size: [10, 20, 30, 40, 50],  // You can adjust the marker sizes as needed
    color: 'red'  // Assigning red color to male data points
  }
};

var data = [trace1, trace2];

var layout = {
  title: '2019 Earnings by Racial/Ethnic Background',
  height: 600,
  width: 600
};

Plotly.newPlot('myDiv', data, layout);
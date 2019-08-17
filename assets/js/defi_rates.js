// Declaration of dynamic properties

function getPercent(value) {
  return Math.round( value * 10000 ) / 100 + '%';
}

var providersViewModel = function() {
  var self = this;

  self.providersDAI  = ko.observableArray([]);
  self.providersUSDC = ko.observableArray([]);
  self.weekData      = ko.observableArray([]);

  self.averageDAI = ko.computed(function() {
    var sum = 0;
    for(var i=0; i< self.weekData().length - 1; i++) {
      sum+=self.weekData()[i];
    }
    return Math.round(sum * 100/ self.weekData().length) / 100 + "%";
  });

  self.averageUSDC = ko.observable();
}

var viewModel = new providersViewModel()

ko.applyBindings(viewModel);

// Populate viewmodel

var xhr = new XMLHttpRequest();
xhr.open("GET", window.requestURL + "/getLendingData", true)

xhr.onreadystatechange = function () {
  if(xhr.status == 200 && xhr.readyState == 4) {
    var providers = JSON.parse(xhr.responseText);
    viewModel.providersDAI(providers.sortedProvidersDAI);
    viewModel.providersUSDC(providers.sortedProvidersUSDC);
  }
}

xhr.send();

var xhr2 = new XMLHttpRequest();
xhr2.open("GET", window.requestURL + "/getDataForWeek", true);

xhr2.onreadystatechange = function() {
  if(xhr2.status == 200 && xhr2.readyState == 4) {
    var monthNames = ["January", "February", "March", "April", "May", "June",
      "July", "August", "September", "October", "November", "December"
    ];
    var weekData = JSON.parse(xhr2.responseText);
    var sumOfUSDC = 0;
    var filteredData = weekData.map(function(day) {
      sumOfUSDC += day.sumOfUSDC;
      return Math.round(day.sumOfDAI * 10000)/100;
    })
    
    viewModel.averageUSDC(getPercent(sumOfUSDC/weekData.length));

    viewModel.weekData(filteredData)

    myChart.data.labels = weekData.map(function(day) {
      var date = new Date(day.date);
      
      return monthNames[date.getMonth()] + " " + date.getUTCDate();
    })

    myChart.data.datasets.map(function(dataset) {
      if(dataset.label == 'DeFi lending') {
        dataset.data = filteredData
      }
    })
    myChart.update();
  }
}
xhr2.send();


// chart
var monthNames = ["January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December"
];

var ctx = document.getElementById('rate_graphs').getContext('2d');
document.getElementById('rate_graphs').style.backgroundColor = 'rgb(255,255,255)';

var myChart = new Chart(ctx, {
  type: 'line',
  data: {
      labels: Array(7).fill(''),
      datasets: [{
          label: 'DeFi lending',
          data: Array(7).fill(0),
          backgroundColor: "#8F68FC",
          fill: false,
          borderColor: "#8F68FC",
          borderWidth: 4,
      },
      {
        label: 'Interest rate on balances',
        fill: false,
        data: Array(7).fill(0.03),
        backgroundColor: "#BCBCED",
        borderColor: "#BCBCED",
        borderWidth: 4,
        borderDash: [5, 5]
      },
      {
        label: 'Vanguard CDs',
        fill: false,
        data: Array(7).fill(2.4),
        backgroundColor: "#ADEFF2",
        borderColor: "#ADEFF2",
        borderWidth: 4,
        borderDash: [5, 5]
      },
      {
        label: 'Vanguard Real Estate ETF',
        fill: false,
        data: Array(7).fill(4.03),
        backgroundColor: "#BBEE67",
        borderColor: "#BBEE67",
        borderWidth: 4,
        borderDash: [5, 5]
      },{
        label: 'SPDR Bloomberg Barclays High Yield Bond ETF',
        fill: false,
        data: Array(7).fill(5.6),
        backgroundColor: "#FFDFBA",
        borderColor: "#FFDFBA",
        borderWidth: 4,
        borderDash: [5, 5]
      }]
  },
  options: {
    legend: {
      display: false
    },
    scales: {
        xAxes: [{
          gridLines: {
            display: false
          }
        }],
        yAxes: [{
            ticks: {
                beginAtZero: true
            }
        }]
    },
    tooltips: {
      callbacks: {
        label: function(tooltipItem, data) {
          return data['datasets'][tooltipItem['datasetIndex']].label + ': ' + data['datasets'][tooltipItem['datasetIndex']]['data'][tooltipItem['index']] + '%';
        }
      }
    }
  }
});
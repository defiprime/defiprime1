// Declaration of dynamic properties

function getPercent(value) {
  return Math.round(value * 10000) / 100 + '%';
}

const api = "https://defiportfolio-backend.herokuapp.com/api/v1";
const markets = ["compound_v2", "fulcrum", "dydx"];
const tokens = ["dai", "sai", "usdc"];
const requestParams = markets.flatMap(market => {
  return tokens.map(token => { market: market, token: token })
});

const timePeriods = [
  {
    id: 0,
    getStartDate: () => new Date() - 1000 * 60 * 60 * 24,
    text: "24 Hours"
  },
  {
    id: 1,
    getStartDate: () => new Date() - 1000 * 60 * 60 * 24 * 7,
    text: "1 Week"
  },
  {
    id: 2,
    getStartDate: () => new Date() - 1000 * 60 * 60 * 24 * 30,
    text: "1 Month"
  },
  {
    id: 3,
    getStartDate: () => new Date(0).getTime(),
    text: "All-time"
  }];

function get(url) {
  return new Promise(function (resolve, reject) {
    var req = new XMLHttpRequest();
    req.open('GET', url);
    req.onload = function () {
      if (req.status == 200) {
        resolve(req.response);
      }
      else {
        reject(Error(req.statusText));
      }
    };
    req.onerror = function () {
      reject(Error("Network Error"));
    };
    req.send();
  });
}

const fromTimestampToLabel = (jsTimestamp, activePeriodButton) => {
  jsTimestamp *= 1000;
  switch (activePeriodButton) {
    case 0:
      return new Date(jsTimestamp).toLocaleTimeString('en-us', { timeStyle: "short" });
    case 1:
      return new Date(jsTimestamp).toLocaleDateString('en-us', { dateStyle: "short", timeStyle: "short" });
    case 2:
      return new Date(jsTimestamp).toLocaleString('en-us', { day: "2-digit", month: "short" });
    case 3:
      return new Date(jsTimestamp).toLocaleString('en-us', { day: "2-digit", month: "short" });
    default: return new Date(jsTimestamp)
  }
}

const onTimeScaleChange = (e) => {
  e.preventDefault();
  var timePeriodId = e.currentTarget.dataset.startDate;
  var startDate = timePeriods.filter(period => period.id == timePeriodId)
  GetData(startDate).then(responses => {
    var daiDataset = GetDaiDataset(responses);
    var saiDataset = GetSaiDataset(responses);
    var usdcDataset = GetUsdcDataset(responses);

    window.myChart.labels = responses[0].data.chart.map(chartItem => fromTimestampToLabel(chartItem.timestamp, timePeriodId));
    window.myChart.data.dataset = [daiDataset, saiDataset, usdcDataset,
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
      }, {
        label: 'SPDR Bloomberg Barclays High Yield Bond ETF',
        fill: false,
        data: Array(7).fill(5.6),
        backgroundColor: "#FFDFBA",
        borderColor: "#FFDFBA",
        borderWidth: 4,
        borderDash: [5, 5]
      }]
    window.myChart.update();
  });
}

const init = () => {
  var ctx = document.getElementById('rate_graphs').getContext('2d');
  document.getElementById('rate_graphs').style.backgroundColor = 'rgb(255,255,255)';
  
  GetData().then(responses => {
    var daiDataset = GetDaiDataset(responses);
    var saiDataset = GetSaiDataset(responses);
    var usdcDataset = GetUsdcDataset(responses);
    var lendingRates = {
      dai: GetLendingRates(responses, "dai"),
      sai: GetLendingRates(responses, "sai"),
      usdc: GetLendingRates(responses, "usdc"),
    };
    renderLendingRates(lendingRates)
    var labels = responses[0].data.chart.map(chartItem => fromTimestampToLabel(chartItem.timestamp, 0));

    window.myChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: labels,
        datasets: [daiDataset, saiDataset, usdcDataset,
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
          }, {
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
            label: function (tooltipItem, data) {
              return data['datasets'][tooltipItem['datasetIndex']].label + ': ' + data['datasets'][tooltipItem['datasetIndex']]['data'][tooltipItem['index']] + '%';
            }
          }
        }
      }
    });

  });
};

const renderLendingRates = (lendingRates) => {

};

const GetData = (startDate) => {
  if (!startDate) {
    startDate = new Date() * 1000;
  }
  startDate = parseInt((startDate / 1000).toFixed(0));
  var requests = requestParams.map(param => get(`${api}/${market}/${token}?start_date=${startDate}`));
  Promise.all(requests)
    .then(values => {
      return response = values.map((value, index) => {
        return {
          market: requestParams[index].market,
          token: requestParams[index].token,
          data: value
        }
      });
    });
}

const GetLendingRates = (responses, token) => {
  var data = responses.filter(item => item.token === token);
  var compound_v2 = data.filter(item => item.market === "compound_v2");
  var fulcrum = data.filter(item => item.market === "fulcrum");
  var dydx = data.filter(item => item.market === "dydx");

  return {
    compound_v2: {
      supply_rate: compound_v2.supply_rate,
      supply_30d_apr: compound_v2.supply_30d_apr,
    },
    fulcrum: {
      supply_rate: fulcrum.supply_rate,
      supply_30d_apr: fulcrum.supply_30d_apr,
    },
    dydx: {
      supply_rate: dydx.supply_rate,
      supply_30d_apr: dydx.supply_30d_apr,
    },
    mean: (compound_v2.supply_rate + fulcrum.supply_rate + dydx.supply_rate) / 3
  }

}

const GetDaiDataset = (responses) => {
  let daiData = responses.filter(item => item.token === "dai");
  return {
    label: 'DAI lending',
    data: GetArraysMean(daiData.map(item => item.data.chart.map(chartItem => chartItem.supply_rate))),
    backgroundColor: "#8F68FC",
    fill: false,
    borderColor: "#8F68FC",
    borderWidth: 4,
  }
};

const GetSaiDataset = (responses) => {
  let saiData = responses.filter(item => item.token === "sai");
  return {
    label: 'SAI lending',
    data: GetArraysMean(saiData.map(item => item.data.chart.map(chartItem => chartItem.supply_rate))),
    backgroundColor: "#8F68FC",
    fill: false,
    borderColor: "#8F68FC",
    borderWidth: 4,
  }
};

const GetUsdcDataset = (responses) => {
  let usdcData = responses.filter(item => item.token === "usdc");
  return {
    label: 'USDC lending',
    data: GetArraysMean(usdcData.map(item => item.data.chart.map(chartItem => chartItem.supply_rate))),
    backgroundColor: "#8F68FC",
    fill: false,
    borderColor: "#8F68FC",
    borderWidth: 4,
  }
};

const GetArraysMean = (arrays) => {
  let result = [];

  //Rounding to nearest whole number.
  for (var i = 0; i < arrays[0].length; i++) {
    var num = 0;
    //still assuming all arrays have the same amount of numbers
    for (var j = 0; j < arrays.length; j++) {
      num += arrays[j][i];
    }
    result.push(Math.round(num / arrays.length));
  }

  return result
}

window.addEventListener("load", function (e) {
  init();
  document.querySelectorAll(".time-period").addEventListener("click", onTimeScaleChange);
});
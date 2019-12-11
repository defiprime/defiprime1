const api = "https://defiportfolio-backend.herokuapp.com/api/v1";
const old_api = "https://api-rates.defiprime.com";

const markets = ["compound_v2", "fulcrum", "dydx"];
const tokens = ["dai", "sai", "usdc"];

const GetConstDatasetsWithTimescale = (period, points, startDate, endDate) => {
  var timePeriod = timePeriods.find(item => item.id === period);
  if (!startDate)
    startDate = timePeriod.getStartDate();
  if (!endDate)
    endDate = moment();
  var delta = parseInt((endDate - startDate) / (points - 1));
  return constDatasets.map((dataset) => {
    var value = dataset.data;
    var result = Object.assign({}, dataset);
    result.data = Array(points).fill(0).map((item, index) => {
      return {
        x: moment(startDate + (index * delta)),
        y: value
      }
    })
    return result;
  })
};

const constDatasets = [{
  label: 'Interest rate on balances',
  fill: false,
  data: 0.03,
  backgroundColor: "#BCBCED",
  borderColor: "#BCBCED",
  borderWidth: 4,
  borderDash: [5, 5]
},
{
  label: 'Vanguard CDs',
  fill: false,
  data: 2.4,
  backgroundColor: "#ADEFF2",
  borderColor: "#ADEFF2",
  borderWidth: 4,
  borderDash: [5, 5]
},
{
  label: 'Vanguard Real Estate ETF',
  fill: false,
  data: 4.03,
  backgroundColor: "#BBEE67",
  borderColor: "#BBEE67",
  borderWidth: 4,
  borderDash: [5, 5]
}, {
  label: 'SPDR Bloomberg Barclays High Yield Bond ETF',
  fill: false,
  data: 5.6,
  backgroundColor: "#FFDFBA",
  borderColor: "#FFDFBA",
  borderWidth: 4,
  borderDash: [5, 5]
}];


const requestParams = markets.flatMap(market => {
  return tokens.map(token => {
    return token === "sai" && market === "dydx"
      ? null
      : {
        market: market,
        token: token
      }
  })
}).filter(item => item !== null);

const timePeriods = [
  {
    id: 0,
    difference: 1000 * 60 * 60 * 24,
    getStartDate: () => moment() - 1000 * 60 * 60 * 24,
    text: "1 Day"
  },
  {
    id: 1,
    difference: 1000 * 60 * 60 * 24 * 7,
    getStartDate: () => moment() - 1000 * 60 * 60 * 24 * 7,
    text: "7 Days"
  },
  {
    id: 2,
    difference: 1000 * 60 * 60 * 24 * 30,
    getStartDate: () => moment() - 1000 * 60 * 60 * 24 * 30,
    text: "1 Month"
  },
  {
    id: 3,
    difference: 1000 * 60 * 60 * 24 * 31 * 3,
    getStartDate: () => moment() - 1000 * 60 * 60 * 24 * 31 * 3,
    text: "3 Month"
  },
  {
    id: 4,
    difference: 1000 * 60 * 60 * 24 * 365,
    getStartDate: () => moment() - 1000 * 60 * 60 * 24 * 365,
    text: "1 Year"
  },
  {
    id: 5,
    difference: 1000 * 60 * 60 * 24 * 365,
    getStartDate: () => moment(0),
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
  return moment(jsTimestamp)

  switch (activePeriodButton) {
    case 0:
      return moment(jsTimestamp).toLocaleTimeString('en-us', { timeStyle: "short" });
    case 1:
      return moment(jsTimestamp).toLocaleDateString('en-us', { dateStyle: "short", timeStyle: "short" });
    case 2:
      return moment(jsTimestamp).toLocaleString('en-us', { day: "2-digit", month: "short" });
    case 3:
      return moment(jsTimestamp).toLocaleString('en-us', { day: "2-digit", month: "short" });
    case 4:
      return moment(jsTimestamp).toLocaleString('en-us', { day: "2-digit", month: "short" });
    default: return moment(jsTimestamp)
  }
}

const onTimeScaleChange = (e) => {
  e.preventDefault();
  var timePeriodId = parseInt(e.currentTarget.dataset.period);
  var startDate = timePeriods.find(period => period.id == timePeriodId).getStartDate();
  GetData(startDate).then(responses => {
    var daiDataset = GetDaiDataset(responses, timePeriodId);
    var saiDataset = GetSaiDataset(responses, timePeriodId);
    var usdcDataset = GetUsdcDataset(responses, timePeriodId);
    var dataX;
    if (daiDataset.data[0].x < usdcDataset.data[0].x && daiDataset.data[0].x < saiDataset.data[0].x) {
      dataX = daiDataset.data.map(item => item.x)
    } else if (saiDataset.data[0].x < usdcDataset.data[0].x && saiDataset.data[0].x < daiDataset.data[0].x) {
      dataX = saiDataset.data.map(item => item.x)

    }
    else {
      dataX = usdcDataset.data.map(item => item.x)

    }

    var staticDatasets = GetConstDatasetsWithTimescale(timePeriodId, dataX.length, dataX[0], dataX[dataX.length - 1]);
    // // window.myChart.data.labels = responses[0].data.chart.map(chartItem => fromTimestampToLabel(chartItem.timestamp, timePeriodId));
    // // window.myChart.data.labels = dataX;
    window.myChart.data.datasets = [daiDataset, saiDataset, usdcDataset].concat(staticDatasets);
    window.myChart.update();
  });
}

const init = () => {
  var ctx = document.getElementById('rate_graphs').getContext('2d');
  document.getElementById('rate_graphs').style.backgroundColor = 'rgb(255,255,255)';

  GetData().then(responses => {
    var daiDataset = GetDaiDataset(responses, 2);
    var saiDataset = GetSaiDataset(responses, 2);
    var usdcDataset = GetUsdcDataset(responses, 2);
    var lendingRates = tokens.map(token => GetLendingRates(responses, token));
    renderLendingRates(lendingRates)
    var labels = responses[0].data.chart.map(chartItem => fromTimestampToLabel(chartItem.timestamp, 2));
    var staticDatasets = GetConstDatasetsWithTimescale(2, labels.length);
    window.myChart = new Chart(ctx, {
      type: 'line',
      data: {
        // labels: labels,
        datasets: [daiDataset, saiDataset, usdcDataset].concat(staticDatasets),
      },
      options: {
        responsive: true,
        legend: {
          display: false
        },
        tooltips: {
          mode: 'nearest',
          intersect: false,
          position: "average",
          backgroundColor: "#292984",
          titleFontColor: "#fff",
          bodyFontColor: "#fff",
          cornerRadius: 0,
          titleFontFamily: "Kanit",
          titleFontStyle: "normal",
          bodyFontFamily: "Kanit",
          bodyFontSize: 16,
          bodyFontStyle: "normal",
          bodySpacing: 5,
          xPadding: 10,
          yPadding: 10,
          callbacks: {
            label: function (tooltipItem, data) {
              return data['datasets'][tooltipItem['datasetIndex']].label + ': ' + tooltipItem.value + '%';
            }
          }
        },
        hover: {
          mode: 'nearest',
          intersect: false
        },
        scales: {
          xAxes: [{
            type: 'time',
            gridLines: {
              display: false
            },
            ticks: {
              maxTicksLimit: 7
            }
          }],
          yAxes: [{
            offset: true,
            gridLines: {
              drawTicks: false,
              drawBorder: false,
              color: "#F3F5F6"
            },
            ticks: {
              padding: 20,
              beginAtZero: true,
              fontSize: 12,
              fontColor: "#8B8BB8",
              fontFamily: "Open Sans",
              callback: function (value, index, values) {
                return value + '%';
              }
            }
          }]
        }
      }
    });

  });
};

const renderLendingRates = (lendingRates) => {
  document.querySelectorAll(".lending-wrapper").forEach((lendingWrapper, index) => {
    var token = lendingWrapper.dataset.token;
    var rates = lendingRates.find(item => item.token === token)
    lendingWrapper.querySelector(".lending-mean").textContent = rates.mean;
    lendingWrapper.querySelectorAll(".list-crypto .item-crypto").forEach((itemCrypto, index) => {
      var market = itemCrypto.querySelector(".list-crypto-name .value").dataset.market;
      var rate = rates.marketRates.find(item => item.market === market);
      if (rate) {
        itemCrypto.querySelector(".list-crypto-today .value").textContent = rate.supply_rate;
        itemCrypto.querySelector(".list-crypto-month .value").textContent = rate.supply_30d_apr;
      }
    });
  });
};

const GetData = (startDate) => {
  document.getElementById("overlay").style.display = "block";
  if (!startDate) {
    startDate = timePeriods.find(item => item.id === 2).getStartDate();
  }
  startDate = parseInt((startDate / 1000).toFixed(0));
  var requests = requestParams.map(param => get(`${api}/markets/${param.market}/${param.token}?start_date=${startDate}`));
  return Promise.all(requests)
    .then(values => {
      document.getElementById("overlay").style.display = "none";
      return response = values.map((value, index) => {
        return {
          market: requestParams[index].market,
          token: requestParams[index].token,
          data: JSON.parse(value)
        }
      });
    });
}

const GetLendingRates = (responses, token) => {
  var data = responses.filter(item => item.token === token);

  var marketRates = markets.flatMap(market =>
    data.filter(item => item.market === market)
      .map(item => {
        return {
          market: market,
          supply_rate: item.data.supply_rate.toFixed(2),
          supply_30d_apr: item.data.supply_30d_apr.toFixed(2),
        }
      })
  )

  return {
    token: token,
    marketRates,
    mean: GetMeanBetweenArrayElements(marketRates.map(market => market.supply_rate)).toFixed(2)
  }

}

const GetDaiDataset = (responses, timePeriodId) => {
  let daiData = responses.filter(item => item.token === "dai");
  var arrayY = GetArraysMean(daiData.map(item => item.data.chart.map(chartItem => chartItem.supply_rate)))
  var arrayX = GetArraysMean(daiData.map(item => item.data.chart.map(chartItem => chartItem.timestamp)))
    .map(item => fromTimestampToLabel(parseInt(item), timePeriodId));
  return {
    label: 'DAI lending',
    data: arrayY.map((item, index) => { return { y: item, x: arrayX[index] } }),
    backgroundColor: "#FF961C",
    fill: false,
    borderColor: "#FF961C",
    borderWidth: 4,
  }
};

const GetSaiDataset = (responses, timePeriodId) => {
  let saiData = responses.filter(item => item.token === "sai");
  var arrayY = GetArraysMean(saiData.map(item => item.data.chart.map(chartItem => chartItem.supply_rate)))
  var arrayX = GetArraysMean(saiData.map(item => item.data.chart.map(chartItem => chartItem.timestamp)))
    .map(item => fromTimestampToLabel(parseInt(item), timePeriodId));

  return {
    label: 'SAI lending',
    data: arrayY.map((item, index) => { return { y: item, x: arrayX[index] } }),
    backgroundColor: "#8F68FC",
    fill: false,
    borderColor: "#8F68FC",
    borderWidth: 4,
  }
};

const GetUsdcDataset = (responses, timePeriodId) => {
  let usdcData = responses.filter(item => item.token === "usdc");
  var arrayY = GetArraysMean(usdcData.map(item => item.data.chart.map(chartItem => chartItem.supply_rate)))
  var arrayX = GetArraysMean(usdcData.map(item => item.data.chart.map(chartItem => chartItem.timestamp)))
    .map(item => fromTimestampToLabel(parseInt(item), timePeriodId));

  return {
    label: 'USDC lending',
    data: arrayY.map((item, index) => { return { y: item, x: arrayX[index] } }),
    backgroundColor: "#05D2DD",
    fill: false,
    borderColor: "#05D2DD",
    borderWidth: 4,
  }
};

const GetArraysMean = (arrays) => {
  let result = [];

  for (var i = 0; i < arrays[0].length; i++) {
    var num = 0;
    //still assuming all arrays have the same amount of numbers
    for (var j = 0; j < arrays.length; j++) {
      num += arrays[j][i];
    }
    result.push((num / arrays.length).toFixed(2));
  }

  return result
}

const GetMeanBetweenArrayElements = (array) => {
  var sum = array.reduce((a, b) => parseFloat(a) + parseFloat(b), 0);
  return (sum / array.length) || 0;
}

window.addEventListener("load", function (e) {
  init();
  document.querySelectorAll(".period-button").forEach(item => item.addEventListener("click", onTimeScaleChange));
});


var liquidity_xhr = new XMLHttpRequest();
liquidity_xhr.open("GET", old_api + "/getMinInterest", true);
liquidity_xhr.onreadystatechange = function () {
  if (liquidity_xhr.status == 200 && liquidity_xhr.readyState == 4) {
    var liquidityData = JSON.parse(liquidity_xhr.responseText);
    document.querySelector(".sai-eth .list-liquidity .list-liquidity-value .value").textContent = liquidityData[0].providerDAI;
    document.querySelector(".sai-eth .list-liquidity .list-liquidity-name").href = liquidityData[0].providerLink;
    document.querySelector(".usdc-eth .list-liquidity .list-liquidity-name").href = liquidityData[0].providerLink;
    document.querySelector(".usdc-eth .list-liquidity .list-liquidity-value .value").textContent = liquidityData[0].providerUSDC;
  }
}
liquidity_xhr.send();
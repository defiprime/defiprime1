// Declaration of dynamic properties

function getPercent(value) {
  return Math.round( value * 100 ) + '%';
}

function computeAverage(providersArr, property) {
  var sum = 0;
  for(var i=0;i<providersArr.length; i++) {
    sum += providersArr[i][property];
  }
  var divider = providersArr.length == 0 ? 1 : providersArr.length;
  
  return getPercent(sum/divider);
}

var providersViewModel = function() {
  var self = this;

  self.providersDAI  = ko.observableArray([]);
  self.providersUSDC = ko.observableArray([]);
  self.weekData      = ko.observableArray([]);

  self.averageDAI = ko.computed(function () {
    return computeAverage(self.providersDAI(), "providerDAI")
  })

  self.averageUSDC = ko.computed(function () {
    return computeAverage(self.providersUSDC(), "providerUSDC")
  })
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
    var weekData = JSON.parse(xhr2.responseText);

    console.log(weekData)
  }
}
xhr2.send();
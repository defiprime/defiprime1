document.addEventListener("DOMContentLoaded", function () {
  let tickers = [];

  const getShortAddress = (address) => {
    return address.substring(0, 6) + '...' + address.substring(address.length - 11);
  }
  const numberWithCommas = (number) => {
    const parts = number.toString().split(".");
    parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    return parts.join(".");
  }

  const getAddress = () => {
    const tickersAddress = document.querySelectorAll(".ticker-address");
    const arrayAddress = Array.from(tickersAddress);
    arrayAddress.forEach((item, index) => {
      let address = item.innerHTML;
      tickers[index] = Object({ "address": address });
      item.innerHTML = getShortAddress(address);
    })
  }

  getAddress();

  async function getTickers(address, index) {
    const requestUrl = `https://api.coingecko.com/api/v3/simple/token_price/ethereum?contract_addresses=${address}&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true`;
    const tickersResponse = await fetch(requestUrl);
    const responseJson = await tickersResponse.json();
    if (tickersResponse.status === 200) {
      tickers[index].usd = Object.values(responseJson)[0].usd;
      tickers[index].usd_24h_change = Object.values(responseJson)[0].usd_24h_change;
      tickers[index].usd_24h_vol = Object.values(responseJson)[0].usd_24h_vol;
      tickers[index].usd_market_cap = Object.values(responseJson)[0].usd_market_cap;
    }
    setTickerData();
  }

  tickers.forEach((element, index) => {
    if (element.address.length > 0) {
      getTickers(element.address, index);
    }
  });
  const setTickerData = () => {
    const tickersRow = document.querySelectorAll(".ticker-row");
    const arrayRow = Array.from(tickersRow);
    arrayRow.forEach((item, index) => {
      if (tickers[index].usd) {
        item.querySelector('.ticker-price-value').innerHTML = tickers[index].usd.toFixed(2);
        item.querySelector('.ticker-price').classList.remove("loading");
      }
      if (tickers[index].usd_24h_change) {
        item.querySelector('.ticker-change-value').innerHTML = tickers[index].usd_24h_change.toFixed(2);
        item.querySelector('.ticker-change').classList.remove("loading");
        tickers[index].usd_24h_change > 0 ? item.querySelector('.ticker-change').classList.add("hight") : item.querySelector('.ticker-change').classList.add("low");
      }
      if (tickers[index].usd_24h_vol) {
        item.querySelector('.ticker-vol-value').innerHTML = numberWithCommas(tickers[index].usd_24h_vol.toFixed());
        item.querySelector('.ticker-vol').classList.remove("loading");
      }
      if (tickers[index].usd_market_cap) {
        item.querySelector('.ticker-market-cap-value').innerHTML = numberWithCommas(tickers[index].usd_market_cap.toFixed());
        item.querySelector('.ticker-market-cap').classList.remove("loading");

      }
      const btns = item.querySelectorAll('.btncopy')
      Array.from(btns).forEach(function (item) {

        item.addEventListener('click', function (e) {
          const btn = e.currentTarget;
          const title = btn.closest('.ticker-row').querySelector('.ticker-address').getAttribute("title");

          const tempInput = document.createElement("input");
          tempInput.style = "position: absolute; left: -1000px; top: -1000px";
          tempInput.value = title;
          document.body.appendChild(tempInput);
          tempInput.select();
          document.execCommand("copy");
          document.body.removeChild(tempInput);
        });
      });
    })
  }
});
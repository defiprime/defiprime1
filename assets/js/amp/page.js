var filterButtons = document.getElementsByClassName('filters-button-group')[0].getElementsByTagName("button");


if (window.location.hash) {
  var hash = window.location.hash.replace("#", "");
  filter(hash);
  Array.from(filterButtons).find(button => button.classList.contains("active")).classList.remove("active");
  Array.from(filterButtons).find(button => button.getAttribute("data-filter") === hash).classList.add("active");
}
Array.from(filterButtons).forEach(button => {
  button.addEventListener('click', filterButtonClick);
});

function filterButtonClick(e) {
  Array.from(filterButtons).forEach(node => {
    node.classList.remove('active');
  });
  e.currentTarget.classList.add('active');
  var filterValue = e.currentTarget.getAttribute("data-filter");
  filter(filterValue);
};

function filter(filterValue) {
  var itemSelector = document.getElementById('assets_cards').getElementsByClassName("asset_tool_card");
  Array.from(itemSelector).forEach(item => {
    var itemWrapper = item.parentNode; // item.closest(".article-wrapper");
    if (filterValue === "*") {
      itemWrapper.classList.remove("none");
      return;
    }
    itemWrapper.style.display = item.classList.contains(filterValue) ? itemWrapper.classList.remove("none") : itemWrapper.classList.add("none");
  });
}
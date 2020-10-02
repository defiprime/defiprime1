var filterButtons = document.querySelectorAll('.filters-button-group button');

window.addEventListener('load', () => {


    if (window.location.hash) {
        var hash = window.location.hash.replace("#", "");
        filter(hash);
        Array.from(filterButtons).find(button => button.classList.contains("active")).classList.remove("active");
        Array.from(filterButtons).find(button => button.dataset.filter === hash).classList.add("active");
    }
    filterButtons.forEach(button => {
        button.addEventListener('click', filterButtonClick);
    });


});
function filterButtonClick(e) {
    filterButtons.forEach(node => {
        node.classList.remove('active');
    });
    e.currentTarget.classList.add('active');
    var filterValue = e.currentTarget.dataset.filter;
    if (filterValue !== "*") {
        window.location.hash = "#" + filterValue;
    } else {
        history.pushState("", document.title, window.location.pathname
            + window.location.search)
    }
    filter(filterValue);
};

function filter(filterValue) {
    var itemSelector = document.querySelectorAll('#assets_cards .asset_tool_card');
    itemSelector.forEach(item => {
        var itemWrapper = item.closest(".article-wrapper");
        if (filterValue === "*") {
            itemWrapper.style.display = '';
            return;
        }
        itemWrapper.style.display = item.classList.contains(filterValue) ? '' : 'none';
    });
}
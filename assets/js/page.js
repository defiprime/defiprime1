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
    if (filterValue !== "*") {
        window.location.hash = "#" + filterValue;
    } else {
        history.pushState("", document.title, window.location.pathname
            + window.location.search)
    }
    filter(filterValue);
};

function filter(filterValue) {
    var itemSelector = document.getElementById('assets_cards').getElementsByClassName("asset_tool_card");
    Array.from(itemSelector).forEach(item => {
        var itemWrapper = item.closest(".article-wrapper");
        if (filterValue === "*") {
            itemWrapper.style.display = '';
            return;
        }
        itemWrapper.style.display = item.classList.contains(filterValue) ? '' : 'none';
    });
}
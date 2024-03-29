document.getElementById("price-up").addEventListener("click", ordered);
document.getElementById("price-down").addEventListener("click", ordered);
document.getElementById("rating-up").addEventListener("click", ordered);
document.getElementById("rating-down").addEventListener("click", ordered);
document.getElementById("title-up").addEventListener("click", ordered);
document.getElementById("title-down").addEventListener("click", ordered);
document.getElementById("author-up").addEventListener("click", ordered);
document.getElementById("author-down").addEventListener("click", ordered);
document.getElementById("category-up").addEventListener("click", ordered);
document.getElementById("category-down").addEventListener("click", ordered);
document.getElementById("price-up-xl").addEventListener("click", ordered);
document.getElementById("price-down-xl").addEventListener("click", ordered);
document.getElementById("rating-up-xl").addEventListener("click", ordered);
document.getElementById("rating-down-xl").addEventListener("click", ordered);
document.getElementById("title-up-xl").addEventListener("click", ordered);
document.getElementById("title-down-xl").addEventListener("click", ordered);
document.getElementById("author-up-xl").addEventListener("click", ordered);
document.getElementById("author-down-xl").addEventListener("click", ordered);
document.getElementById("category-up-xl").addEventListener("click", ordered);
document.getElementById("category-down-xl").addEventListener("click", ordered);

function ordered() {
    const selector = $(this);
    const thisUrl = new URL(window.location);
    const order = selector.val();
    if (order != "reset") {
        const sort = order.split("_")[0];
        const dir = order.split("_")[1];
        thisUrl.searchParams.set("sort", sort);
        thisUrl.searchParams.set("dir", dir);
        window.location.replace(thisUrl);
    } else {
        thisUrl.searchParams.delete("sort");
        thisUrl.searchParams.delete("dir");
        window.location.replace(thisUrl);
    }
};

function show() {
    var Slogindex = 0;
showPresidentSlog();

function showPresidentSlog() {
    var i;
    var slog = document.getElementsByClassName('president-slog__slide');
    var dots = document.getElementsByClassName("dot");
    for (i = 0; i < slog.length; i++) {
        slog[i].style.opacity = '0';
    }
    Slogindex++;
    if (Slogindex > slog.length) {Slogindex = 1}
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slog[Slogindex-1].style.opacity = '1';
    slog[Slogindex-1].style.transition = 'opacity 2s ease';
    dots[Slogindex-1].className += " active";
    setTimeout(showPresidentSlog, 5000)
}
}
show()


function searchHide(){
    Slogindex = 0
    var search = document.getElementsByClassName("search-wrapper");
    for (i = 0; i < search.length; i++) {
        search[i].className = search[i].className.replace(" hide", "");
    }
    search[Slogindex-1].className += " hide";
}

function showProgres() {
    var ProgressIndex = 0;
    showProgress();

function showProgress() {
    var i;
    var progress = document.getElementsByClassName('latest-news__item');
    for (i = 0; i < progress.length; i++) {
    }
    ProgressIndex++;
    if (ProgressIndex > progress.length) {ProgressIndex = 1}
    for (i = 0; i < progress.length; i++) {
        progress[i].className = progress[i].className.replace(" active", "");
    }
    progress[ProgressIndex-1].className += " active";
    setTimeout(showProgress, 5000)
}
}
showProgres()


function showNews() {
    var NewsIndex = 0;
    showLatest();

    function showLatest() {
        var i;
        var news = document.getElementsByClassName('latest-news__item-background');
        for (i = 0; i < news.length; i++) {
        }
        NewsIndex++;
        if (NewsIndex > news.length) {NewsIndex = 1}
        for (i = 0; i < news.length; i++) {
            news[i].className = news[i].className.replace(" active", "");
        }
        news[NewsIndex-1].className += " active";
        setTimeout(showLatest, 5000)
    }

var TitleIndex = 0;
showTitle();

function showTitle() {
    var i;
    var title = document.getElementsByClassName('latest-news__title-wrapper');
    for (i = 0; i < title.length; i++) {
    }
    TitleIndex++;
    if (TitleIndex > title.length) {TitleIndex = 1}
    for (i = 0; i < title.length; i++) {
        title[i].className = title[i].className.replace(" active", "");
    }
    title[TitleIndex-1].className += " active";
    setTimeout(showTitle, 5000)
}

}
showNews()

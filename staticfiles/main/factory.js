function showSlider() {
    var slideIndex = 0;
    showSlides();

    function showSlides() {
        var i;
        var slides = document.getElementsByClassName("slider__item");
        for (i = 0; i < slides.length; i++) {
            slides[i].style.opacity = "0";
        }
        slideIndex++;
        if(slides.length < slideIndex){slideIndex=1}
        slides[slideIndex-1].style.opacity = "1";
        slides[slideIndex-1].style.transition = 'opacity 2s ease'
        setTimeout(showSlides, 5000)
    }
}
showSlider()


function showFactory() {
    var FullIndex = 0;
    showFull();

    function showFull() {
        var i;
        var full = document.getElementsByClassName('full-slider__img');
        for (i = 0; i < full.length; i++) {
        }
        FullIndex++;
        if (FullIndex > full.length) {FullIndex = 1}
        for (i = 0; i < full.length; i++) {
            full[i].className = full[i].className.replace(" active", "");
        }
        full[FullIndex-1].className += " active";
        setTimeout(showFull, 5000)
    }
}
showFactory();


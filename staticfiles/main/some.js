const mainWrapper = document.querySelector('.main-wrapper')
const headerWrapper = document.querySelector('.header-wrapper')
const headerWrapperHeight = headerWrapper.clientHeight
const mainWrapperHeight = mainWrapper.clientHeight
const headerTop = document.querySelector('.header-top')
const searchWrapper = document.querySelector('.search-wrapper')

const params = new URLSearchParams(window.location.search)


window.addEventListener('scroll', (e)=>{
    const rect = mainWrapper.getBoundingClientRect()

    if (rect.top - headerWrapperHeight <= 0){
        headerWrapper.style.position = 'fixed';
        headerWrapper.style.top = 0;
        headerWrapper.style.width = '100%';
        headerWrapper.style.left = 0;
        headerWrapper.style.opacity = '.9';
        headerTop.style.paddingBottom = '44px'
        headerTop.style.backgroundColor = '#1275ca';
        searchWrapper.addEventListener('mouseover', function(){
            searchWrapper.style.opacity = '1'
            searchWrapper.style.transition = 'opacity .3s ease'
        })
        searchWrapper.addEventListener('mouseout', function(){
            searchWrapper.style.opacity = '.9'
        })
        headerWrapper.addEventListener('mouseover', function(){
            headerWrapper.style.opacity = '1'
            headerWrapper.style.transition = 'opacity .3s ease'
        })
        headerWrapper.addEventListener('mouseout', function(){
            headerWrapper.style.opacity = '.9'
        })
        
    } else{
        headerTop.style.paddingBottom = '0';
        headerWrapper.style.position = '';
        headerWrapper.style.width = '';
        headerWrapper.style.top = '';
        headerWrapper.style.left = '';
        headerWrapper.style.opacity = '1';
        searchWrapper.addEventListener('mouseover', function(){
            searchWrapper.style.opacity = ''
        })
        searchWrapper.addEventListener('mouseout', function(){
            searchWrapper.style.opacity = ''
        })
        headerWrapper.addEventListener('mouseover', function(){
            headerWrapper.style.opacity = ''
        })
        headerWrapper.addEventListener('mouseout', function(){
            headerWrapper.style.opacity = ''
        })
    }
})



const gallerySlide = document.querySelector('.gallery__container')

const prevBtn = document.querySelector('.gallery__btn-prev')
const nextBtn = document.querySelector('.gallery__btn-next')

let counter = 1


prevBtn.addEventListener('click', function(){
    if (counter <= 0){
        gallerySlide.style.transition = 'transform 0.4s ease-in-out';
        counter = 17;
        gallerySlide.style.transform = 'translateX(' + (-24.6 * counter - counter * 1) + '%)';    
    } else{
        gallerySlide.style.transition = 'transform 0.4s ease-in-out';
        counter--;
        gallerySlide.style.transform = 'translateX(' + (-24.6 * counter - counter * 1) + '%)';
    }
})
nextBtn.addEventListener('click', function(){
    if (counter >= 18){
        counter = 1
        gallerySlide.style.transition = 'transform 0.4s ease-in-out';
        gallerySlide.style.transform = 'translateX(0)'
    } else {
    gallerySlide.style.transition = 'transform 0.4s ease-in-out';
    gallerySlide.style.transform = 'translateX(' + (-24.6 * counter - counter * 1) + '%)';
    counter++;
    }
})
setInterval(() => {
    if(counter >= 18 ){
        counter = 1
        gallerySlide.style.transition = 'transform 0.4s ease-in-out';
        gallerySlide.style.transform = 'translateX(0%)'
    }else {
        gallerySlide.style.transform = 'translateX(' + (-24.6 * counter - counter * 1) + '%)';
        counter++;
    }
}, 5000);                                                  




const factorySlide = document.querySelector('.factory__container')
const factoryItem = document.querySelector('.factory__item.item')

const factoryprevBtn = document.querySelector('.section__factory .gallery__btn-prev')
const factorynextBtn = document.querySelector('.section__factory .gallery__btn-next')

let count = 1

factoryprevBtn.addEventListener('click', function(){
    if (count <= 0){
        factorySlide.style.transition = 'transform 0.4s ease-in-out';
        count = 3;
        factorySlide.style.transform = 'translateX(' + (-24.6 * count - count * 1) + '%)';    
    } else{
        factorySlide.style.transition = 'transform 0.4s ease-in-out';
        count--;
        factorySlide.style.transform = 'translateX(' + (-24.6 * count - count * 1) + '%)';
    }
})
factorynextBtn.addEventListener('click', function(){
    if (count >= 4){
        count = 0
        factorySlide.style.transition = 'transform 0.4s ease-in-out';
        factorySlide.style.transform = 'translateX(0)'
    } else {
        factorySlide.style.transition = 'transform 0.4s ease-in-out';
        factorySlide.style.transform = 'translateX(' + (-24.6 * count - count * 1) + '%)';
        count++;
    }
})

window.addEventListener('DOMContentLoaded', function(){
        setInterval(() => {
            if(count >= 4 ){
                count = 0
                factorySlide.style.transition = 'transform 0.4s ease-in-out';
                factorySlide.style.transform = 'translateX(0%)'
            }else {
                factorySlide.style.transform = 'translateX(' + (-24.6 * count - count * 1) + '%)';
                count++;
            }
        }, 6000);
})


function recaptchaCallback() {
    var sendBtn = document.querySelector('#send-button')
    sendBtn.removeAttribute('disabled');
}

const name = document.getElementById('name')
const error = document.getElementById('error')
const form = document.getElementById('feed-back')

form.addEventListener('submit', (e)=>{
    let messages = []
    if(name.value === '' || name.value === null){
        messages.push('Name is required')
    }

    if(messages.length > 0){
        e.preventDefault()
        error.innerText = messages.join(', ')
    }
})



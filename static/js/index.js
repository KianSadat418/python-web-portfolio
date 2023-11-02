let animationStopper;
window.addEventListener("load", function() {
    const h1 = document.getElementById('header-h1-animated');
    const h3 = document.getElementById('header-h3-animated');
    const btns = document.getElementById('header-btns-animated');
    const socials = document.getElementById('header-socials-animated');

    h1.classList.add("slideUp-animation-1400ms");
    h3.classList.add("slideUp-animation-2000ms");
    btns.classList.add("slideUp-animation-2400ms");
    socials.classList.add("slideUp-animation-2600ms");

    h1.addEventListener("animationend", function() {
        h1.classList.remove("slideUp-animation-1400ms");
    });
    h3.addEventListener("animationend", function() {
        h3.classList.remove("slideUp-animation-2000ms");
    });
    btns.addEventListener("animationend", function() {
        btns.classList.remove("slideUp-animation-2400ms");
    });
    socials.addEventListener("animationend", function() {
        socials.classList.remove("slideUp-animation-2600ms");
    });
});
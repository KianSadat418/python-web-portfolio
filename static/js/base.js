let resizeTimer;
window.addEventListener("resize", () => {
    document.body.classList.add("resize-animation-stopper");
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => {
        document.body.classList.remove("resize-animation-stopper");
    });
});

const primaryNav = document.querySelector('.header__primary-navigation');
const navToggle = document.querySelector('.header__mobile-nav-toggle');

navToggle.addEventListener("click", () => {
    const visibility = primaryNav.getAttribute('data-visible')

    if (visibility === "false") {
        primaryNav.setAttribute('data-visible', true); 
        navToggle.setAttribute('aria-expanded', true);
    } else {
        primaryNav.setAttribute('data-visible', false); 
        navToggle.setAttribute('aria-expanded', false);
    }
});
const navSlider = () => {
    const burger = document.querySelector('.nav__burger');
    const nav = document.querySelector('.nav__links');
    const navLinks = document.querySelectorAll('.nav__link');

    burger.addEventListener('click', () => {
        // toggle side menu 
        nav.classList.toggle('nav__active');
        // nav__burger menu animation
        burger.classList.toggle('nav__responsive');
        // nav link animation
        navLinks.forEach((link, index) => {
            if(link.style.animation){
                link.style.animation = '';
            } else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index/ 15 + 0.5}s`;
            }
        });
    });
}

navSlider();
 const hamburger = document.querySelector(".hamburger")
 const navMenu = document.querySelector(".navbar-menu")
 const header = document.querySelector(".header")

 hamburger.addEventListener('click', () => {
    navMenu.classList.toggle('active');
    header.classList.toggle('header-height')
 })
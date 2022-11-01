const slideContainer = [...document.querySelectorAll(".slider-container")];
const slide = [...document.querySelectorAll(".slide")];

const nextBtn = [...document.querySelectorAll(".next-btn")];
const prevBtn = [...document.querySelectorAll(".prev-btn")];

slideContainer.forEach((item, i) => {
    let containerDimension = item.getBoundingClientRect();
    let containerWidth = containerDimension.width


    nextBtn[i].addEventListener("click", () => {
        item.scrollLeft += containerWidth
    })

    prevBtn[i].addEventListener("click", () => {
        item.scrollLeft -= containerWidth
    })
})

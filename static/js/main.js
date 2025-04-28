
document.addEventListener('DOMContentLoaded', function() {
    const tabButtons = document.querySelectorAll('.tab-button');
    const cityContents = document.querySelectorAll('.city-content');

    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            tabButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');

            const cityId = button.getAttribute('data-city');
            cityContents.forEach(content => {
                content.classList.remove('active');
                if (content.id === `city-${cityId}`) {
                    content.classList.add('active');
                    initSlider(content.querySelector('.attraction-slider'));
                }
            });
        });
    });

    // Slayd-shou funksiyasi
    function initSlider(slider) {
        if (!slider) return;

        const images = slider.querySelectorAll('.slider-image');
        const caption = slider.querySelector('.slider-caption');
        let currentIndex = 0;

        const slideInterval = setInterval(() => {
            images[currentIndex].classList.remove('active');
            currentIndex = (currentIndex + 1) % images.length;
            images[currentIndex].classList.add('active');

            if (caption) {
                caption.textContent = images[currentIndex].alt;
            }
        }, 4000);

        slider.addEventListener('mouseenter', () => {
            clearInterval(slideInterval);
        });

        slider.addEventListener('mouseleave', () => {
            clearInterval(slideInterval);
            slideInterval = setInterval(() => {
                images[currentIndex].classList.remove('active');
                currentIndex = (currentIndex + 1) % images.length;
                images[currentIndex].classList.add('active');

                if (caption) {
                    caption.textContent = images[currentIndex].alt;
                }
            }, 4000);
        });
    }

    // Boshlang'ich slayd-shoularni ishga tushirish
    document.querySelectorAll('.attraction-slider').forEach(slider => {
        initSlider(slider);
    });
});
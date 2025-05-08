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
                }
            });
        });
    });
});


// Diqqatga sazovor joylar uchun yangi funksiya
    document.querySelectorAll('.attraction-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const targetId = this.getAttribute('data-target');

            // Barcha tugmalardan active klassini olib tashlash
            document.querySelectorAll('.attraction-btn').forEach(b => {
                b.classList.remove('active');
            });

            // Bosilgan tugmaga active klassini qo'shish
            this.classList.add('active');

            // Barcha rasmlarni yashirish
            document.querySelectorAll('.slider-image').forEach(img => {
                img.classList.remove('active');
            });

            // Tanlangan rasmni ko'rsatish
            const targetImage = document.querySelector(`.slider-image[data-id="${targetId}"]`);
            if (targetImage) {
                targetImage.classList.add('active');

                // Sarlavhani yangilash
                const caption = targetImage.closest('.attraction-slider').querySelector('.slider-caption');
                if (caption) {
                    caption.textContent = this.textContent.trim();
                }
            }
        });
    });
});
document.addEventListener('DOMContentLoaded', function() {
    // Shahar tablari uchun funksiya
    const tabButtons = document.querySelectorAll('.tab-button');
    const cityContents = document.querySelectorAll('.city-content');

    tabButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Barcha tugmalardan active klassini olib tashlash
            tabButtons.forEach(btn => btn.classList.remove('active'));

            // Bosilgan tugmaga active klassini qo'shish
            this.classList.add('active');

            // Barcha kontentlarni yashirish
            cityContents.forEach(content => content.classList.remove('active'));

            // Tanlangan shahar kontentini ko'rsatish
            const cityId = this.getAttribute('data-city');
            const activeContent = document.getElementById(`city-${cityId}`);
            if (activeContent) {
                activeContent.classList.add('active');
            }
        });
    });

    // Diqqatga sazovor joylar uchun funksiya
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
            const slider = this.closest('.city-content').querySelector('.attraction-slider');
            if (slider) {
                slider.querySelectorAll('.slider-image').forEach(img => {
                    img.classList.remove('active');
                });

                // Tanlangan rasmni ko'rsatish
                const targetImage = slider.querySelector(`.slider-image[data-id="${targetId}"]`);
                if (targetImage) {
                    targetImage.classList.add('active');

                    // Sarlavhani yangilash
                    const caption = slider.querySelector('.slider-caption');
                    if (caption) {
                        caption.textContent = this.textContent.trim();
                    }
                }
            }
        });
    });

    // Boshlang'ich holatda birinchi shaharning birinchi diqqatga sazovor joyini aktiv qilish
    const firstAttractionBtn = document.querySelector('.attraction-btn');
    if (firstAttractionBtn) {
        firstAttractionBtn.classList.add('active');
    }
});
document.addEventListener('DOMContentLoaded', function() {
    // Confirm before delete
    document.querySelectorAll('.deletelink').forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('Ushbu elementni oʻchirishga ishonchingiz komilmi?')) {
                e.preventDefault();
            }
        });
    });

    // Image preview enhancement
    document.querySelectorAll('.field-image_preview img').forEach(img => {
        img.classList.add('image-preview');
    });

    // Video preview enhancement
    document.querySelectorAll('.field-video_embed iframe').forEach(iframe => {
        iframe.parentElement.classList.add('video-preview');
    });

    // Custom tooltips
    document.querySelectorAll('[title]').forEach(el => {
        el.setAttribute('data-toggle', 'tooltip');
        el.setAttribute('data-placement', 'top');
    });

    // Initialize tooltips
    if ($.fn.tooltip) {
        $('[data-toggle="tooltip"]').tooltip();
    }
});
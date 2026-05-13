/**
 * KVB Green Energies - Home Page Logic
 * Handles the hero slideshow and other index-specific functionality
 */

document.addEventListener('DOMContentLoaded', function() {
    // Hero slideshow logic: mixes videos and images sequentially
    const slides = document.querySelectorAll('.hero-slide');
    if (slides.length === 0) return;

    let currentSlide = 0;
    let slideTimeout;

    function playNextSlide() {
        clearTimeout(slideTimeout);

        // Hide all slides
        slides.forEach(slide => slide.classList.remove('visible'));

        // Show current slide
        const currentMedia = slides[currentSlide];
        currentMedia.classList.add('visible');

        // Handle alignment fix for slide 2 image if needed
        if (currentMedia.id === 'heroSlide2') {
            const img = currentMedia.querySelector('img');
            if (img) {
                img.style.objectPosition = 'center';
            }
        }

        if (currentMedia.tagName.toLowerCase() === 'video' || currentMedia.querySelector('video')) {
            const video = currentMedia.tagName.toLowerCase() === 'video' ? currentMedia : currentMedia.querySelector('video');
            if (video) {
                video.currentTime = 0;
                video.play().catch(e => console.log('Autoplay blocked:', e));

                video.onended = () => {
                    currentSlide = (currentSlide + 1) % slides.length;
                    playNextSlide();
                };
            }
        } else {
            // If it's an image, stay for 4 seconds then transition
            slideTimeout = setTimeout(() => {
                currentSlide = (currentSlide + 1) % slides.length;
                playNextSlide();
            }, 4000);
        }
    }

    // Start the sequence
    playNextSlide();
});

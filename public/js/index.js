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
                video.play().catch(e => {
                    console.log('Autoplay blocked or failed:', e);
                    // Fallback: transition after 4 seconds if video fails to play
                    slideTimeout = setTimeout(() => {
                        currentSlide = (currentSlide + 1) % slides.length;
                        playNextSlide();
                    }, 4000);
                });

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

    // Hide intro screen after animation finishes
    if (localStorage.getItem('hasSeenLogoReveal')) {
        // Already seen, just show main site immediately and init AOS
        const introScreen = document.getElementById('introScreen');
        if (introScreen) introScreen.style.display = 'none';
        
        const mainSite = document.getElementById('mainWebsite');
        if (mainSite) {
            mainSite.classList.add('show');
            if (typeof AOS !== 'undefined') {
                AOS.init({ duration: 800, once: true, offset: 50 });
                setTimeout(() => AOS.refresh(), 100);
            }
        }
    } else {
        localStorage.setItem('hasSeenLogoReveal', 'true');
        setTimeout(function() {
            const introScreen = document.getElementById('introScreen');
            if (introScreen) {
                introScreen.classList.add('fade-out');
                setTimeout(() => { introScreen.style.display = 'none'; }, 1200);
            }
            
            const mainSite = document.getElementById('mainWebsite');
            if (mainSite) {
                mainSite.classList.add('show');
                // Initialize AOS (Animate on Scroll)
                if (typeof AOS !== 'undefined') {
                    AOS.init({
                        duration: 800,
                        once: true,
                        offset: 50
                    });
                    setTimeout(() => AOS.refresh(), 100);
                }
            }
        }, 4500); // 4.5s delay allows the logo reveal to finish
    }
});

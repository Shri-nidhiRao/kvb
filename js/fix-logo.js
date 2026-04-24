/**
 * KVB Header Logo Fix
 * 
 * When header.html is loaded via fetch() + innerHTML, its inline <script>
 * tags don't execute. This script sets the logo src using the script's
 * own URL to determine the correct path to the logo image.
 */
(function () {
    // Determine the base path from this script's own src attribute.
    // This script lives at {root}/js/fix-logo.js, so stripping "js/fix-logo.js"
    // gives us the root path regardless of deployment location.
    var scripts = document.getElementsByTagName('script');
    var thisScript = scripts[scripts.length - 1]; // last script = current script
    var scriptSrc = thisScript.getAttribute('src') || '';
    var basePath = scriptSrc.replace(/js\/fix-logo\.js.*$/, '');

    var logoPath = basePath + 'images/products/kvb-logo.png';

    function fixLogo() {
        var logo = document.querySelector('#header .logo img');
        if (!logo) return false;
        if (!logo.src || !logo.src.includes('kvb-logo')) {
            logo.src = logoPath;
        }
        return true;
    }

    function initHeaderScripts() {
        // Mobile Menu Toggle
        const btn = document.getElementById("menuBtn");
        const menu = document.getElementById("navMenu");
        if (btn && menu && !btn.hasAttribute('data-initialized')) {
            btn.onclick = () => {
                menu.classList.toggle("active");
            };
            btn.setAttribute('data-initialized', 'true');
        }

        // Mobile Dropdown Toggle
        document.querySelectorAll("#navMenu .dropdown > a").forEach(el => {
            if (!el.hasAttribute('data-initialized')) {
                el.addEventListener("click", e => {
                    if (window.innerWidth < 900) {
                        e.preventDefault();
                        el.parentElement.classList.toggle("active");
                    }
                });
                el.setAttribute('data-initialized', 'true');
            }
        });

        // Hide top bar and add shadow on scroll
        if (!window.headerScrollInitialized) {
            window.addEventListener('scroll', function() {
                const header = document.querySelector('.header');
                if (header) {
                    if (window.scrollY > 50) {
                        header.classList.add('scrolled');
                    } else {
                        header.classList.remove('scrolled');
                    }
                }
            });
            window.headerScrollInitialized = true;
        }
    }

    // Try immediately, then retry until header has loaded (up to ~3 seconds)
    if (!fixLogo()) {
        var attempts = 0;
        var interval = setInterval(function () {
            attempts++;
            if (fixLogo() || attempts > 20) {
                clearInterval(interval);
                initHeaderScripts();
            }
        }, 150);
    } else {
        initHeaderScripts();
    }
})();

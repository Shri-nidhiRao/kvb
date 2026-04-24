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

    // Try immediately, then retry until header has loaded (up to ~3 seconds)
    if (!fixLogo()) {
        var attempts = 0;
        var interval = setInterval(function () {
            attempts++;
            if (fixLogo() || attempts > 20) {
                clearInterval(interval);
            }
        }, 150);
    }
})();

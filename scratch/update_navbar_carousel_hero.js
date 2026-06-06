const fs = require('fs');
const path = require('path');

const targetFiles = [
    'solar-steam-cooking.html',
    'direct-cooking.html',
    'solar-dryers.html',
    'scheffler-concentrators.html',
    'microgreen-systems.html',
    'thermal-storage.html'
];

const dir = 'd:\\kvb-green-energies-website\\public\\products';

targetFiles.forEach(fileName => {
    const filePath = path.join(dir, fileName);
    if (!fs.existsSync(filePath)) {
        console.error(`File not found: ${filePath}`);
        return;
    }

    let content = fs.readFileSync(filePath, 'utf8');

    // 1. Update #header placeholder style
    const headerRegex = /#header\s*\{[^}]*position:\s*fixed;[\s\S]*?\}/gi;
    if (headerRegex.test(content)) {
        content = content.replace(headerRegex, `#header {
            min-height: 80px;
        }`);
        console.log(`Updated #header style in ${fileName}`);
    } else {
        console.log(`Warning: Could not find #header style in ${fileName}`);
    }

    // 2. Remove padding-top: 80px; from body styling
    const bodyPaddingRegex = /(body\s*\{[\s\S]*?)padding-top:\s*80px;([\s\S]*?\})/gi;
    if (bodyPaddingRegex.test(content)) {
        content = content.replace(bodyPaddingRegex, '$1$2');
        console.log(`Removed padding-top from body in ${fileName}`);
    } else {
        console.log(`Warning: Could not find body padding-top in ${fileName}`);
    }

    // 3. Reduce carousel size: max-width: 1000px -> max-width: 800px
    const carouselWidthRegex = /\.kvb-carousel\s*\{([\s\S]*?)max-width:\s*1000px;([\s\S]*?\})/gi;
    if (carouselWidthRegex.test(content)) {
        content = content.replace(carouselWidthRegex, '.kvb-carousel {$1max-width: 800px;$2}');
        console.log(`Reduced carousel width in ${fileName}`);
    } else {
        console.log(`Warning: Could not find carousel width styling in ${fileName}`);
    }

    // 4. Reduce carousel image height: height: 500px -> height: 400px
    const carouselImgHeightRegex = /(\.kvb-carousel\s+\.carousel-item\s+img\s*\{[\s\S]*?)height:\s*500px;([\s\S]*?\})/gi;
    if (carouselImgHeightRegex.test(content)) {
        content = content.replace(carouselImgHeightRegex, '$1height: 400px;$2');
        console.log(`Reduced carousel image height in ${fileName}`);
    } else {
        console.log(`Warning: Could not find carousel img height styling in ${fileName}`);
    }

    // 5. Remove carousel indicators
    const indicatorsRegex = /<ol class="carousel-indicators">[\s\S]*?<\/ol>/gi;
    if (indicatorsRegex.test(content)) {
        content = content.replace(indicatorsRegex, '');
        console.log(`Removed carousel indicators in ${fileName}`);
    } else {
        console.log(`Warning: Could not find carousel indicators HTML in ${fileName}`);
    }

    // 6. Remove hero breadcrumb links
    const breadcrumbRegex = /<div class="hero-breadcrumb">[\s\S]*?<\/div>/gi;
    if (breadcrumbRegex.test(content)) {
        content = content.replace(breadcrumbRegex, '');
        console.log(`Removed hero breadcrumbs in ${fileName}`);
    } else {
        console.log(`Warning: Could not find hero breadcrumbs HTML in ${fileName}`);
    }

    fs.writeFileSync(filePath, content, 'utf8');
});

console.log('All products updated successfully.');

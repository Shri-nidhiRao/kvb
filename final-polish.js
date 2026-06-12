const fs = require('fs');
const path = require('path');
const sharp = require('sharp');

const publicDir = path.join(__dirname, 'public');

function getAllHtmlFiles(dirPath, arrayOfFiles) {
    const files = fs.readdirSync(dirPath);
    arrayOfFiles = arrayOfFiles || [];
    files.forEach(function(file) {
        if (fs.statSync(dirPath + "/" + file).isDirectory()) {
            if (file !== 'node_modules') {
                arrayOfFiles = getAllHtmlFiles(dirPath + "/" + file, arrayOfFiles);
            }
        } else {
            if (file.endsWith('.html')) {
                arrayOfFiles.push(path.join(dirPath, "/", file));
            }
        }
    });
    return arrayOfFiles;
}

const htmlFiles = getAllHtmlFiles(publicDir);

async function finalLighthousePolish() {
    let imagesFixed = 0;
    
    // Also grab all images in the public dir
    for (const file of htmlFiles) {
        let content = fs.readFileSync(file, 'utf8');
        let modified = false;

        // 1. Defer Google Fonts
        const gfMont = '<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap"\n    rel="stylesheet">';
        const gfMontSingleLine = '<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap" rel="stylesheet">';
        
        const gfDeferred = '<link rel="preload" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap" as="style" onload="this.onload=null;this.rel=\'stylesheet\'"><noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap"></noscript>';
        
        if (content.includes(gfMont)) {
            content = content.replace(gfMont, gfDeferred);
            modified = true;
        } else if (content.includes(gfMontSingleLine)) {
            content = content.replace(gfMontSingleLine, gfDeferred);
            modified = true;
        }

        // 2. Fix images (including those in components)
        const imgRegex = /<img\s+([^>]*?)>/g;
        let match;
        const imgMatches = [];
        while ((match = imgRegex.exec(content)) !== null) {
            imgMatches.push({
                fullTag: match[0]
            });
        }

        for (const img of imgMatches) {
            if (img.fullTag.includes('width=') || img.fullTag.includes('height=')) continue;

            const srcMatch = img.fullTag.match(/src=["'](.*?)["']/);
            if (!srcMatch) continue;
            
            let imgPath = srcMatch[1];
            if (imgPath.startsWith('/')) imgPath = imgPath.substring(1);
            
            const absoluteImgPath = path.join(publicDir, imgPath);
            
            if (fs.existsSync(absoluteImgPath)) {
                try {
                    const metadata = await sharp(absoluteImgPath).metadata();
                    if (metadata.width && metadata.height) {
                        const newTag = img.fullTag.replace('<img ', `<img width="${metadata.width}" height="${metadata.height}" `);
                        content = content.replace(img.fullTag, newTag);
                        modified = true;
                        imagesFixed++;
                    }
                } catch (e) { }
            }
        }

        if (modified) {
            fs.writeFileSync(file, content, 'utf8');
        }
    }

    console.log(`Final Polish! Added dimensions to ${imagesFixed} missed images and deferred Google Fonts.`);
}

finalLighthousePolish();

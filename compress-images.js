const fs = require('fs');
const path = require('path');
const sharp = require('sharp');

const imagesDir = path.join(__dirname, 'public', 'images');

function getAllImages(dirPath, arrayOfFiles) {
    const files = fs.readdirSync(dirPath);
    arrayOfFiles = arrayOfFiles || [];
    files.forEach(function(file) {
        if (fs.statSync(dirPath + "/" + file).isDirectory()) {
            arrayOfFiles = getAllImages(dirPath + "/" + file, arrayOfFiles);
        } else {
            const ext = path.extname(file).toLowerCase();
            if (['.jpg', '.jpeg', '.png'].includes(ext)) {
                arrayOfFiles.push(path.join(dirPath, "/", file));
            }
        }
    });
    return arrayOfFiles;
}

const imageFiles = getAllImages(imagesDir);
const MAX_WIDTH = 1920;
let processedCount = 0;

async function processImages() {
    console.log(`Found ${imageFiles.length} images to check...`);
    
    for (const file of imageFiles) {
        const stats = fs.statSync(file);
        const fileSizeMB = stats.size / (1024 * 1024);
        
        // Process images larger than 500KB
        if (fileSizeMB > 0.5) {
            console.log(`Processing ${path.basename(file)} (${fileSizeMB.toFixed(2)} MB)...`);
            try {
                const tempFile = file + '.tmp';
                
                const metadata = await sharp(file).metadata();
                let pipeline = sharp(file);
                
                if (metadata.width > MAX_WIDTH) {
                    pipeline = pipeline.resize(MAX_WIDTH);
                }
                
                if (file.toLowerCase().endsWith('.png')) {
                    await pipeline.png({ quality: 80, compressionLevel: 9 }).toFile(tempFile);
                } else {
                    await pipeline.jpeg({ quality: 80, mozjpeg: true }).toFile(tempFile);
                }
                
                // Replace original
                fs.renameSync(tempFile, file);
                
                const newStats = fs.statSync(file);
                console.log(` -> Reduced to ${(newStats.size / (1024 * 1024)).toFixed(2)} MB`);
                processedCount++;
            } catch (err) {
                console.error(`Error processing ${file}:`, err);
            }
        }
    }
    
    console.log(`Successfully compressed ${processedCount} large images!`);
}

processImages();

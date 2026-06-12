const fs = require('fs');
const path = require('path');

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
const errors = [];

for (const file of htmlFiles) {
    const content = fs.readFileSync(file, 'utf8');
    
    // Find all src="..." and href="..."
    const regex = /(?:src|href)="([^"]+)"/g;
    let match;
    
    while ((match = regex.exec(content)) !== null) {
        let url = match[1];
        
        // Ignore external URLs and anchors
        if (url.startsWith('http') || url.startsWith('//') || url.startsWith('mailto:') || url.startsWith('tel:') || url.startsWith('#') || url === '') {
            continue;
        }
        
        // Remove query params or hashes
        url = url.split('?')[0].split('#')[0];
        
        // Resolve path relative to the current file OR relative to root if it starts with /
        let targetPath;
        if (url.startsWith('/')) {
            targetPath = path.join(publicDir, url);
        } else {
            targetPath = path.join(path.dirname(file), url);
        }
        
        if (!fs.existsSync(targetPath)) {
            errors.push(`File: ${file.replace(publicDir, '')}\nBroken Link: ${match[1]}\nResolved To: ${targetPath}\n`);
        }
    }
}

if (errors.length > 0) {
    console.log("Found broken links:");
    console.log(errors.join('\n'));
} else {
    console.log("No broken links found!");
}

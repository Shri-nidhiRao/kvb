const fs = require("fs");
const path = require("path");
const sharp = require("sharp");

// Recursive function to find all HTML files
function findHtmlFiles(dir, fileList = []) {
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const filePath = path.join(dir, file);
    if (fs.statSync(filePath).isDirectory()) {
      if (file !== "components") {
        findHtmlFiles(filePath, fileList);
      }
    } else if (file.endsWith(".html")) {
      fileList.push(filePath);
    }
  }
  return fileList;
}

async function build() {
  console.log("Starting build process...");
  const publicDir = path.join(__dirname, "public");
  const htmlFiles = findHtmlFiles(publicDir);

  // 1. Read header and footer components
  const headerContentRaw = fs.readFileSync(
    path.join(publicDir, "components", "header.html"),
    "utf-8"
  );
  const footerContentRaw = fs.readFileSync(
    path.join(publicDir, "components", "footer.html"),
    "utf-8"
  );

  // Extract body and style
  const extractBody = (html) => {
    const bodyMatch = html.match(/<body>([\s\S]*?)<\/body>/i);
    return bodyMatch ? bodyMatch[1] : html;
  };
  const extractStyle = (html) => {
    const styleMatch = html.match(/<style>([\s\S]*?)<\/style>/i);
    return styleMatch ? `<style>${styleMatch[1]}</style>` : "";
  };

  const headerBody = extractBody(headerContentRaw);
  const footerBody = extractBody(footerContentRaw);
  const headerStyle = extractStyle(headerContentRaw);
  const footerStyle = extractStyle(footerContentRaw);

  for (const file of htmlFiles) {
    let content = fs.readFileSync(file, "utf-8");
    let modified = false;

    // A. Inject Header and Footer if missing and remove loadComponent
    if (content.includes('loadComponent("header"')) {
      content = content.replace(
        /<div id="header">[\s\S]*?<\/div>/,
        `${headerStyle}\n<div id="header">\n${headerBody}\n</div>`
      );
      content = content.replace(
        /<div id="footer">[\s\S]*?<\/div>/,
        `${footerStyle}\n<div id="footer">\n${footerBody}\n</div>`
      );

      // Remove the loadComponent function calls
      content = content.replace(/loadComponent\("header",.*?\);/g, "");
      content = content.replace(/loadComponent\("footer",.*?\);/g, "");
      modified = true;
    }

    // B. Optimize Google Fonts (Block to Swap)
    if (content.includes("display=block")) {
      content = content.replace(/display=block/g, "display=swap");
      modified = true;
    }

    // C. Add Explicit Image Dimensions
    const imgRegex = /<img\s+([^>]+)>/g;
    let match;
    const replacements = [];

    while ((match = imgRegex.exec(content)) !== null) {
      const imgTag = match[0];
      const attrs = match[1];

      // Check if width and height already exist
      if (!attrs.includes("width=") && !attrs.includes("height=")) {
        // Find src or data-src
        const srcMatch = attrs.match(/(?:data-)?src="([^"]+)"/);
        if (srcMatch) {
          let src = srcMatch[1];
          let imgPath;

          if (src.startsWith("/")) {
            imgPath = path.join(publicDir, src);
          } else {
            imgPath = path.join(path.dirname(file), src);
          }

          if (fs.existsSync(imgPath)) {
            try {
              const metadata = await sharp(imgPath).metadata();
              if (metadata.width && metadata.height) {
                // Insert width and height just after <img 
                const newImgTag = imgTag.replace(
                  "<img ",
                  `<img width="${metadata.width}" height="${metadata.height}" `
                );
                replacements.push({ old: imgTag, new: newImgTag });
              }
            } catch (err) {
              console.log("Error reading image metadata:", imgPath);
            }
          }
        }
      }
    }

    if (replacements.length > 0) {
      for (const rep of replacements) {
        content = content.replace(rep.old, rep.new);
      }
      modified = true;
    }

    if (modified) {
      fs.writeFileSync(file, content);
      console.log(`Optimized: ${path.relative(publicDir, file)}`);
    }
  }

  console.log("Build complete! All optimizations applied.");
}

build().catch(console.error);

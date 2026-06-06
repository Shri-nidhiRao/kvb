const fs = require('fs');
const path = require('path');

const dir = 'd:\\kvb-green-energies-website\\public\\products';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

const cssToInject = `        /* ===== SYSTEM IN ACTION SECTION ===== */
        .system-action-section {
            padding: 80px 0;
            background: linear-gradient(145deg, #f0f7f0, #e6f0e6);
            position: relative;
            overflow: hidden;
            margin-bottom: 3.5rem;
        }
        .system-action-section::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMCIgaGVpZ2h0PSIyMCI+CgkJPGNpcmNsZSBjeD0iMiIgY3k9IjIiIHI9IjIiIGZpbGw9IiMzYWI1NGEiIGZpbGwtb3BhY2l0eT0iMC4wNSIvPgoJPC9zdmc+') repeat;
            z-index: 1;
        }
        .system-action-section .section-header {
            text-align: center; margin-bottom: 48px; position: relative; z-index: 2;
        }`;

files.forEach(file => {
    if (file === 'solar-steam-cooking.html') return; // Already fixed

    const filePath = path.join(dir, file);
    let content = fs.readFileSync(filePath, 'utf8');

    // 1. Fix display: inline-block !important; in STANDARD SECTION TITLE override
    content = content.replace(
        /display:\s*inline-block\s*!important;/g,
        'display: block !important;\n            position: relative !important;\n            width: 100% !important;'
    );

    // 2. For the 5 newer pages, wrap the System in Action gallery in the green section
    // Check if it lacks .system-action-section CSS but has a System in Action h2
    if (!content.includes('.system-action-section {') && content.includes('>System in Action</h2>')) {
        // Inject CSS right before /* ===== KVB CAROUSEL ===== */ or before </style>
        if (content.includes('/* ===== KVB CAROUSEL ===== */')) {
            content = content.replace('/* ===== KVB CAROUSEL ===== */', cssToInject + '\n        /* ===== KVB CAROUSEL ===== */');
        } else {
            content = content.replace('</style>', cssToInject + '\n    </style>');
        }

        // Replace the HTML structure
        // Look for: <div class="reveal"> \s* <div class="section-title"> \s* <h2>System in Action</h2> \s* </div> \s* <div id="..." class="carousel slide kvb-carousel" ...>
        // and replace with the section wrapper.
        // Or it might be <h2 class="section-title">System in Action</h2>
        const regex1 = /<div class="reveal(\s*system-action-section)?">\s*(?:<div class="section-title">\s*)?<h2[^>]*>System in Action<\/h2>(?:\s*<\/div>)?\s*(<div id="[^"]+" class="carousel slide kvb-carousel"[^>]*>)/;
        
        content = content.replace(regex1, (match, p1, carouselTag) => {
            return `<section class="system-action-section">
            <div class="container">
                <div class="section-header reveal">
                    <h2 class="section-title">System in Action</h2>
                    <p class="section-subtitle">See our technology deployed and working in real-world environments.</p>
                </div>
                ${carouselTag}`;
        });

        // We also need to add the closing tags: </div></section> after the carousel's closing </div>
        // But finding the closing </div> of the carousel via regex is hard.
        // Wait, the carousel has a specific structure: 
        // </div>
        // <a class="carousel-control-prev"...>...</a>
        // <a class="carousel-control-next"...>...</a>
        // </div>
        // We can match the end of the carousel:
        const regexEnd = /(<span class="sr-only">Next<\/span>\s*<\/a>\s*<\/div>)/;
        content = content.replace(regexEnd, '$1\n            </div>\n        </section>');
    }

    fs.writeFileSync(filePath, content, 'utf8');
    console.log('Processed', file);
});

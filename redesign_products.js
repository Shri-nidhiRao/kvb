const fs = require('fs');
const path = require('path');

const imgMap = {
    'agrosensse.html': 'agrosense1.jpeg',
    'ai-crop-detection.html': 'advanced-research.png',
    'box-type-solar-dryer.html': 'solar-cabinet-dryer-1625050337-5878433.webp',
    'dehydrator.html': 'dehydrator.jpeg',
    'direct-cooking.html': 'solar-scheffler-dish-direct-cooking-system-1000x1000.webp',
    'fish-dryer.html': 'fish1.jpeg',
    'microgreen-systems.html': 'advanced-research.png',
    'scheffler-concentrators.html': 'scheffler-dish1.jpg',
    'solar-dryers.html': 'solar-dryer.jpeg',
    'solar-steam-cooking.html': 'parabolic-cooker.png',
    'solar.html': 'solar-dryer.jpeg',
    'thermal-storage.html': 'ptc.jpg'
};

const cssToAdd = `
        /* ----- HERO SPLIT REDESIGN ----- */
        .hero-split {
            position: relative;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 4rem;
            padding: 120px 0 60px;
            background: linear-gradient(135deg, #FFFFFF 0%, #F8F9FC 100%);
            min-height: auto;
        }
        .hero-split-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 4rem;
            width: 100%;
        }
        .hero-split-text {
            flex: 1;
            text-align: left;
        }
        .hero-split-text h1 {
            text-align: left;
            margin-bottom: 1.5rem;
        }
        .hero-split-text p {
            font-size: 1.15rem;
            margin-bottom: 2rem;
            color: var(--text-secondary);
        }
        .hero-split-image {
            flex: 1;
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .hero-split-image img {
            width: 100%;
            max-width: 600px;
            border-radius: var(--radius-lg);
            box-shadow: var(--shadow-lg);
            transition: transform 0.4s ease, box-shadow 0.4s ease;
            object-fit: cover;
        }
        .hero-split-image img:hover {
            transform: translateY(-5px);
            box-shadow: 0 30px 50px rgba(0, 0, 0, 0.1);
        }
        @media (max-width: 992px) {
            .hero-split-container {
                flex-direction: column;
                text-align: center;
            }
            .hero-split-text, .hero-split-text h1 {
                text-align: center;
            }
            .hero-split-image {
                width: 100%;
            }
        }
`;

const dir = 'd:\\kvb-green-energies-website\\public\\products';

fs.readdirSync(dir).forEach(file => {
    if (!file.endsWith('.html')) return;
    let content = fs.readFileSync(path.join(dir, file), 'utf8');

    // Add CSS
    if (!content.includes('hero-split')) {
        content = content.replace('</style>', cssToAdd + '\n    </style>');
    }

    // Extract original title and optional description if possible
    const titleMatch = content.match(/<h1>(.*?)<\/h1>/s);
    const title = titleMatch ? titleMatch[1].trim() : 'KVB Green Energies Product';

    // Replace hero-light section
    const imgFile = imgMap[file] || 'parabolic-cooker.png';
    const newHero = `
    <!-- HERO -->
    <section class="hero-split">
        <div class="container hero-split-container">
            <div class="hero-split-text reveal active">
                <h1>${title}</h1>
                <p>Clean, efficient, and highly sustainable professional solutions designed by KVB Green Energies to meet the demands of modern industry.</p>
                <div class="hero-tags" style="justify-content: flex-start;">
                   <span class="tag"><i class="fas fa-leaf"></i> Eco-Friendly</span>
                   <span class="tag"><i class="fas fa-bolt"></i> High Efficiency</span>
                   <span class="tag"><i class="fas fa-shield-alt"></i> Reliable</span>
                </div>
            </div>
            <div class="hero-split-image reveal active" style="transition-delay: 0.2s;">
                <img src="../images/products/${imgFile}" alt="${title}">
            </div>
        </div>
    </section>
`;
    
    const sectionRegex = /<section class="hero-light">[\s\S]*?<\/section>/;
    if (sectionRegex.test(content)) {
        content = content.replace(sectionRegex, newHero.trim());
        fs.writeFileSync(path.join(dir, file), content, 'utf8');
        console.log('Updated', file);
    } else {
        console.log('Could not find hero-light in', file);
    }
});

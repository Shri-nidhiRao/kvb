import os
import re
import glob

products_dir = r'd:\kvb-green-energies-website\public\products'
html_files = glob.glob(os.path.join(products_dir, '*.html'))

def remove_emojis(match):
    text = match.group(0)
    # Remove icon spans first
    text = re.sub(r'<span class="section-icon">.*?</span>', '', text, flags=re.DOTALL)
    # Remove common emojis
    text = re.sub(r'[\U00010000-\U0010ffff]', '', text)
    text = re.sub(r'[⚡📐☀️🌱🐟🌡️⚙️🔒📊🔥💡💧🌬️🚀🥗📍🛠️🔧🐛🦠🌤️🌾🏗️📱👉]', '', text)
    # Clean up multiple spaces
    text = re.sub(r'\s+', ' ', text)
    # Remove space right after > or before <
    text = text.replace('> <', '><').replace('> ', '>').replace(' <', '<')
    return text

carousel_css = '''
        /* ===== KVB CAROUSEL ===== */
        .kvb-carousel {
            max-width: 800px; margin: 0 auto 2rem auto;
            background: #fff; border-radius: var(--radius-md);
            overflow: hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.15);
        }
        .kvb-carousel .carousel-item img {
            width: 100%; aspect-ratio: 16/9; height: auto; object-fit: contain; border-radius: 0;
        }
        .kvb-carousel .carousel-control-prev,
        .kvb-carousel .carousel-control-next {
            width: 50px; height: 50px; background: rgba(0,0,0,0.5);
            border-radius: 50%; top: 50%; transform: translateY(-50%);
            opacity: 0.8; transition: all 0.3s ease;
        }
        .kvb-carousel .carousel-control-prev:hover,
        .kvb-carousel .carousel-control-next:hover {
            background: var(--primary); opacity: 1;
        }
        .kvb-carousel .carousel-control-prev { left: 10px; }
        .kvb-carousel .carousel-control-next { right: 10px; }
        .kvb-carousel .carousel-control-prev-icon,
        .kvb-carousel .carousel-control-next-icon {
            width: 20px; height: 20px;
        }
        .kvb-carousel .carousel-indicators li {
            width: 10px; height: 10px; border-radius: 50%;
            background-color: rgba(255,255,255,0.5); border: none;
            margin: 0 5px;
        }
        .kvb-carousel .carousel-indicators li.active {
            background-color: var(--primary); transform: scale(1.2);
        }
'''

override_style = '''
        /* STANDARD SECTION TITLE & SUBTITLE OVERRIDE */
        h2.section-title, .section-title h2, div.section-title h2 {
            font-size: 2.5rem !important;
            color: #0B3D91 !important;
            text-align: center !important;
            margin-bottom: 25px !important;
            display: inline-block !important;
        }
        h2.section-title:after, .section-title h2:after, div.section-title h2:after {
            content: '' !important;
            position: absolute !important;
            bottom: -10px !important;
            left: 50% !important;
            transform: translateX(-50%) !important;
            width: 80px !important;
            height: 4px !important;
            background: #FDB813 !important;
            border-radius: 2px !important;
        }
        p.section-subtitle, .section-subtitle {
            font-size: 1.15rem !important;
            color: var(--text-secondary) !important;
            text-align: center !important;
            max-width: 800px !important;
            margin: 0 auto 2rem auto !important;
        }
'''

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Remove emojis from h1, h2, h3
    content = re.sub(r'<h[1-6][^>]*>.*?</h[1-6]>', remove_emojis, content, flags=re.DOTALL)
    
    # 2. Add Standardized Styles
    if '/* STANDARD SECTION TITLE & SUBTITLE OVERRIDE */' not in content:
        content = content.replace('</style>', override_style + '\n    </style>')
    if '/* ===== KVB CAROUSEL ===== */' not in content:
        content = content.replace('</style>', carousel_css + '\n    </style>')
        
    # 3. Add Bootstrap CSS if not present
    if 'bootstrap.min.css' not in content:
        content = content.replace('</head>', '    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">\n</head>')
        
    # 4. Add Bootstrap JS if not present
    if 'bootstrap.min.js' not in content:
        js_inject = """
    <!-- jQuery and Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
"""
        content = content.replace('</body>', js_inject + '\n</body>')

    # 5. Convert gallery-grid to carousel for "System in Action"
    # Find the System in Action block
    if 'System in Action' in content and 'class="gallery-grid"' in content:
        # Extract images from gallery-grid
        # We look for <div class="gallery-item">...<img src="...">...</div>
        gallery_match = re.search(r'<div class="gallery-grid">(.*?)</div>\s*</div>\s*</main>', content, flags=re.DOTALL)
        if not gallery_match:
            gallery_match = re.search(r'<div class="gallery-grid">(.*?)</div>\s*</div>\s*</div>', content, flags=re.DOTALL)
            
        if gallery_match:
            inner_html = gallery_match.group(1)
            img_srcs = re.findall(r'<img\s+src="(.*?)"', inner_html)
            
            if img_srcs:
                carousel_id = "kvbCarousel_" + os.path.basename(file_path).replace('.html', '')
                
                carousel_html = f'''<div id="{carousel_id}" class="carousel slide kvb-carousel" data-ride="carousel" data-interval="3000">
                    <ol class="carousel-indicators">'''
                for i in range(len(img_srcs)):
                    active_cls = ' class="active"' if i == 0 else ''
                    carousel_html += f'\n                        <li data-target="#{carousel_id}" data-slide-to="{i}"{active_cls}></li>'
                carousel_html += '\n                    </ol>\n                    <div class="carousel-inner">'
                
                for i, src in enumerate(img_srcs):
                    active_cls = ' active' if i == 0 else ''
                    carousel_html += f'''
                        <div class="carousel-item{active_cls}">
                            <img src="{src}" class="d-block w-100" alt="System in Action">
                        </div>'''
                
                carousel_html += f'''
                    </div>
                    <a class="carousel-control-prev" href="#{carousel_id}" role="button" data-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="sr-only">Previous</span>
                    </a>
                    <a class="carousel-control-next" href="#{carousel_id}" role="button" data-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="sr-only">Next</span>
                    </a>
                </div>'''
                
                content = content.replace(gallery_match.group(0), carousel_html)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print('Done updating files!')

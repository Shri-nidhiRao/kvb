import os
import re

solutions_dir = r"d:\kvb-green-energies-website\solutions"

def ultra_wrap(inner):
    common_defs = """
    <linearGradient id="gP" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#4A8B4A" />
        <stop offset="50%" stop-color="#4a8b4a" />
        <stop offset="100%" stop-color="#2F5E2F" />
    </linearGradient>
    <linearGradient id="gA" x1="100%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" stop-color="#fff" stop-opacity="0.8" />
        <stop offset="100%" stop-color="#4A8B4A" stop-opacity="0.4" />
    </linearGradient>
    <linearGradient id="gB" x1="0%" y1="100%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#4A8B4A" />
        <stop offset="100%" stop-color="#8fd18f" /> 
    </linearGradient>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stop-color="#4A8B4A" stop-opacity="0.7"/>
        <stop offset="100%" stop-color="#4A8B4A" stop-opacity="0"/>
    </radialGradient>
    """
    return f"""<svg class="pro-icon-ultra" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
    <defs>{common_defs}</defs>
    <path class="ultra-background" fill="url(#gP)" opacity="0.15" d="M150.2,42.4 C175.1,64.2 189.6,98.6 181.3,128.8 C172.9,159 141.6,185.1 108.3,188.7 C74.9,192.4 39.5,173.5 19.8,142.3 C0.1,111.1 -3.9,67.6 14.9,40.3 C33.7,13 75.3,1.9 110.8,4.6 C146.4,7.3 125.3,20.6 150.2,42.4 Z" />
    <circle class="ultra-pulse" cx="100" cy="100" r="80" fill="url(#glow)" />
    {inner}
    <circle cx="30" cy="40" r="4" fill="#E9F3EA" class="ultra-float" />
    <circle cx="160" cy="150" r="6" fill="#4A8B4A" class="ultra-float-delay" />
    <circle cx="180" cy="60" r="3" fill="#2F5E2F" class="ultra-float-delay-2" />
</svg>"""

# Full 21 definitions
U_HEAT = ultra_wrap("""
    <g class="ultra-spin-fast" transform-origin="100 100">
        <path fill="url(#gA)" d="M100,20 L110,40 L100,30 L90,40 Z M180,100 L160,110 L170,100 L160,90 Z M100,180 L90,160 L100,170 L110,160 Z M20,100 L40,90 L30,100 L40,110 Z" />
    </g>
    <circle class="ultra-float" cx="100" cy="100" r="45" fill="url(#gP)" stroke="#fff" stroke-width="4" />
    <path class="ultra-pulse" fill="none" stroke="url(#gB)" stroke-width="6" stroke-linecap="round" d="M100,130 L100,80 M100,80 C100,70 110,70 110,80 L110,100 M110,80 C110,60 130,60 130,80 L130,120 M130,80 C130,50 150,50 150,80 L150,140" transform="translate(-25, -20) scale(0.8)"/>
""")
U_TIME = ultra_wrap("""
    <circle class="ultra-float" cx="100" cy="100" r="60" fill="url(#gP)" stroke="#fff" stroke-width="6" />
    <circle class="ultra-pulse" cx="100" cy="100" r="40" fill="url(#gB)" />
    <g class="ultra-spin-fast" transform-origin="100 100">
        <rect x="96" y="50" width="8" height="50" rx="4" fill="#fff" />
    </g>
    <rect x="96" y="100" width="30" height="8" rx="4" fill="#2F5E2F" class="ultra-float-delay" />
""")
U_SIZE = ultra_wrap("""
    <g class="ultra-float">
        <rect x="40" y="40" width="120" height="120" rx="10" fill="url(#gP)" stroke="#fff" stroke-width="4" stroke-dasharray="10 10"/>
        <line x1="20" y1="100" x2="180" y2="100" stroke="url(#gB)" stroke-width="6" stroke-linecap="round"/>
        <polygon points="20,100 40,90 40,110" fill="url(#gB)" />
        <polygon points="180,100 160,90 160,110" fill="url(#gB)" />
    </g>
    <rect x="80" y="80" width="40" height="40" rx="5" fill="url(#gA)" class="ultra-pulse" />
""")
U_CAPACITY = ultra_wrap("""
    <g class="ultra-float">
        <path fill="url(#gP)" stroke="#fff" stroke-width="4" d="M50,60 C50,40 150,40 150,60 L150,140 C150,160 50,160 50,140 Z" />
        <ellipse cx="100" cy="60" rx="50" ry="15" fill="url(#gA)" stroke="#fff" stroke-width="4"/>
    </g>
    <path class="ultra-pulse" fill="url(#gB)" d="M50,100 L150,100 L150,140 C150,160 50,160 50,140 Z" opacity="0.8"/>
""")
U_EFFICIENCY = ultra_wrap("""
    <g class="ultra-spin-fast" transform-origin="100 100">
        <path fill="none" stroke="url(#gB)" stroke-width="12" stroke-linecap="round" stroke-dasharray="80 40" d="M100,30 A70,70 0 1,1 99,30" />
        <polygon points="90,20 120,30 90,40" fill="url(#gB)" />
    </g>
    <path class="ultra-float" fill="#fff" d="M105,60 L85,110 L110,110 L95,140 L125,90 L100,90 Z" />
""")
U_STERILIZE = ultra_wrap("""
    <path class="ultra-float" fill="url(#gP)" d="M100,40 C140,40 160,80 160,120 C160,160 140,180 100,180 C60,180 40,160 40,120 C40,80 60,40 100,40 Z" />
    <g class="ultra-pulse" stroke="#fff" stroke-width="8" stroke-linecap="round">
        <line x1="70" y1="150" x2="130" y2="150" />
        <line x1="80" y1="130" x2="120" y2="130" />
        <line x1="90" y1="110" x2="110" y2="110" />
    </g>
    <circle cx="100" cy="100" r="25" fill="none" stroke="url(#gB)" stroke-width="6" class="ultra-float-delay" />
""")
U_INDUSTRY = ultra_wrap("""
    <g class="ultra-float">
        <path fill="url(#gP)" stroke="#fff" stroke-width="4" d="M30,160 L30,100 L60,70 L60,100 L100,60 L100,100 L140,50 L140,160 Z" />
        <rect x="50" y="50" width="10" height="20" fill="url(#gB)" />
        <rect x="90" y="40" width="10" height="20" fill="url(#gB)" />
        <rect x="130" y="30" width="10" height="20" fill="url(#gB)" />
    </g>
    <circle class="ultra-pulse" cx="130" cy="110" r="20" fill="url(#gB)" />
    <path class="ultra-pulse" fill="none" d="M120,110 L140,110 M130,100 L130,120" stroke="#fff" stroke-width="4" />
""")
U_COMMUNITY = ultra_wrap("""
    <circle class="ultra-pulse" cx="100" cy="100" r="40" fill="url(#gP)" stroke="#fff" stroke-width="4"/>
    <g class="ultra-spin">
        <circle cx="100" cy="30" r="15" fill="url(#gB)" />
        <circle cx="160" cy="140" r="15" fill="url(#gB)" />
        <circle cx="40" cy="140" r="15" fill="url(#gB)" />
        <path fill="none" stroke="url(#gB)" stroke-width="4" d="M100,45 L100,60 M145,130 L130,115 M55,130 L70,115" />
    </g>
""")
U_TRACKING = ultra_wrap("""
    <path class="ultra-float" fill="none" stroke="url(#gP)" stroke-width="12" stroke-linecap="round" d="M30,70 Q100,160 170,70" />
    <path class="ultra-pulse" fill="#E9F3EA" d="M100,140 L120,60 L80,60 Z" />
    <circle cx="100" cy="50" r="20" fill="url(#gB)" class="ultra-float-delay" />
    <line x1="100" y1="140" x2="100" y2="180" stroke="url(#gP)" stroke-width="8" stroke-linecap="round" class="ultra-float" />
""")
U_FRUITS = ultra_wrap("""
    <g class="ultra-float">
        <path fill="url(#gP)" stroke="#fff" stroke-width="4" d="M100,170 C40,170 30,100 50,70 C70,40 130,40 150,70 C170,100 160,170 100,170 Z" />
        <path fill="url(#gB)" d="M100,40 Q120,20 140,30 Q110,50 100,40" />
    </g>
    <circle cx="120" cy="90" r="10" fill="#fff" opacity="0.6" class="ultra-pulse" />
""")
U_VEGETABLES = ultra_wrap("""
    <g class="ultra-float">
        <path fill="url(#gP)" stroke="#fff" stroke-width="4" d="M100,180 L70,100 Q100,80 130,100 Z" />
        <path fill="url(#gB)" d="M90,90 Q50,40 70,20 Q100,60 100,90 M110,90 Q150,40 130,20 Q100,60 100,90" />
    </g>
""")
U_SPICES = ultra_wrap("""
    <g class="ultra-float">
        <path fill="url(#gP)" stroke="#fff" stroke-width="4" d="M50,100 L150,100 L130,160 L70,160 Z" />
        <ellipse cx="100" cy="100" rx="50" ry="15" fill="url(#gA)" />
    </g>
    <path class="ultra-pulse" fill="url(#gB)" d="M100,20 L115,80 L85,80 Z" />
    <circle cx="70" cy="60" r="4" fill="url(#gB)" class="ultra-float-delay" />
    <circle cx="130" cy="50" r="3" fill="url(#gB)" class="ultra-float-delay-2" />
""")
U_GRAINS = ultra_wrap("""
    <g class="ultra-float">
        <path fill="none" stroke="url(#gP)" stroke-width="6" d="M100,180 Q120,100 100,40" />
        <ellipse cx="90" cy="140" rx="15" ry="8" fill="url(#gB)" transform="rotate(30 90 140)" />
        <ellipse cx="115" cy="120" rx="15" ry="8" fill="url(#gA)" transform="rotate(-30 115 120)" />
        <ellipse cx="85" cy="90" rx="15" ry="8" fill="url(#gB)" transform="rotate(40 85 90)" />
        <ellipse cx="115" cy="70" rx="15" ry="8" fill="url(#gA)" transform="rotate(-40 115 70)" />
    </g>
""")
U_GRID = ultra_wrap("""
    <g class="ultra-float">
        <path fill="none" stroke="url(#gP)" stroke-width="8" stroke-linecap="round" d="M50,170 L80,60 L120,60 L150,170" />
        <path fill="none" stroke="url(#gP)" stroke-width="6" d="M65,110 L135,110 M75,80 L125,80 M100,60 L100,30" />
        <circle cx="100" cy="30" r="8" fill="url(#gB)" class="ultra-pulse" />
    </g>
    <path class="ultra-pulse" fill="none" stroke="url(#gA)" stroke-width="4" stroke-dasharray="10 5" d="M20,60 L80,60 M120,60 L180,60" />
""")
U_TECH = ultra_wrap("""
    <g class="ultra-float">
        <rect x="60" y="30" width="80" height="140" rx="15" fill="url(#gP)" stroke="#fff" stroke-width="4" />
        <rect x="70" y="45" width="60" height="100" rx="5" fill="#fff" />
        <circle cx="100" cy="160" r="6" fill="#fff" opacity="0.6" />
    </g>
    <g class="ultra-pulse">
        <rect x="75" y="100" width="10" height="35" rx="3" fill="url(#gA)" />
        <rect x="95" y="75" width="10" height="60" rx="3" fill="url(#gB)" />
        <rect x="115" y="115" width="10" height="20" rx="3" fill="url(#gP)" />
    </g>
""")
U_HARDWARE = ultra_wrap("""
    <g class="ultra-spin-fast" transform-origin="100 100">
        <circle cx="100" cy="100" r="50" fill="none" stroke="url(#gP)" stroke-width="16" stroke-dasharray="30 15" />
        <circle cx="100" cy="100" r="30" fill="url(#gB)" />
        <circle cx="100" cy="100" r="15" fill="#fff" />
    </g>
    <path class="ultra-float" fill="url(#gA)" d="M50,100 L20,120 L20,80 Z M150,100 L180,120 L180,80 Z" />
""")
U_DOCS = ultra_wrap("""
    <g class="ultra-float">
        <rect x="50" y="40" width="100" height="130" rx="10" fill="url(#gP)" stroke="#fff" stroke-width="4" />
        <path fill="url(#gB)" d="M50,40 L100,40 L100,90 Z" />
        <line x1="70" y1="100" x2="130" y2="100" stroke="#fff" stroke-width="6" stroke-linecap="round" />
        <line x1="70" y1="120" x2="110" y2="120" stroke="#fff" stroke-width="6" stroke-linecap="round" class="ultra-pulse" />
        <line x1="70" y1="140" x2="130" y2="140" stroke="#fff" stroke-width="6" stroke-linecap="round" />
    </g>
    <circle cx="150" cy="140" r="20" fill="url(#gB)" class="ultra-float-delay" />
    <path fill="none" d="M140,140 L145,145 L155,135" stroke="#fff" stroke-width="3" class="ultra-float-delay" />
""")
U_LIGHTING = ultra_wrap("""
    <g class="ultra-float">
        <path fill="url(#gP)" stroke="#fff" stroke-width="4" d="M80,160 L120,160 L115,180 L85,180 Z" />
        <circle cx="100" cy="100" r="50" fill="url(#gB)" />
    </g>
    <g class="ultra-pulse" stroke="url(#gA)" stroke-width="6" stroke-linecap="round">
        <line x1="100" y1="20" x2="100" y2="40" />
        <line x1="40" y1="100" x2="20" y2="100" />
        <line x1="160" y1="100" x2="180" y2="100" />
        <line x1="50" y1="50" x2="65" y2="65" />
        <line x1="150" y1="50" x2="135" y2="65" />
    </g>
""")
U_WATER = ultra_wrap("""
    <g class="ultra-pulse">
        <ellipse cx="100" cy="160" rx="60" ry="15" fill="none" stroke="url(#gP)" stroke-width="8" opacity="0.5" />
        <ellipse cx="100" cy="160" rx="40" ry="10" fill="none" stroke="url(#gP)" stroke-width="6" opacity="0.8" />
    </g>
    <path class="ultra-float" fill="url(#gB)" stroke="#fff" stroke-width="5" d="M100,40 C100,40 40,90 40,130 C40,165 65,190 100,190 C135,190 160,165 160,130 C160,90 100,40 100,40 Z" />
    <path class="ultra-float" fill="rgba(255,255,255,0.4)" d="M70,130 A30,30 0 0,1 100,100 A30,30 0 0,0 70,130 Z" />
""")
U_STRUCTURE = ultra_wrap("""
    <g class="ultra-float">
        <polygon fill="url(#gP)" stroke="#fff" stroke-width="3" points="100,20 170,50 100,80 30,50" />
    </g>
    <g class="ultra-float-delay">
        <polygon fill="url(#gB)" stroke="#fff" stroke-width="3" points="100,60 170,90 100,120 30,90" />
    </g>
    <g class="ultra-float-delay-2">
        <polygon fill="url(#gA)" stroke="#fff" stroke-width="3" points="100,100 170,130 100,160 30,130" />
    </g>
""")
U_PLANT = ultra_wrap("""
    <path class="ultra-float" fill="none" stroke="url(#gP)" stroke-width="12" stroke-linecap="round" d="M100,180 Q80,120 120,80 T100,20" />
    <path class="ultra-float-delay" fill="url(#gB)" stroke="#fff" stroke-width="4" d="M110,100 C150,70 180,90 190,140 C150,150 120,130 110,100 Z" />
    <path class="ultra-float-delay-2" fill="url(#gP)" stroke="#fff" stroke-width="4" d="M90,130 C50,100 20,120 10,170 C50,180 80,160 90,130 Z" />
    <path class="ultra-pulse" fill="url(#gA)" d="M100,20 C120,0 140,20 100,60 C60,20 80,0 100,20 Z" />
""")

word_map = {
    "temperature": U_HEAT, "heat": U_HEAT, "thermal": U_HEAT, "cooking": U_HEAT, "peak temp": U_HEAT,
    "time": U_TIME, "duration": U_TIME,
    "size": U_SIZE, "area": U_SIZE, "footprint": U_SIZE, "aperture": U_SIZE,
    "capacity": U_CAPACITY, "yield": U_CAPACITY, "production": U_CAPACITY, "output": U_CAPACITY,
    "efficiency": U_EFFICIENCY,
    "pasteurization": U_STERILIZE, "sterilization": U_STERILIZE, "clean": U_STERILIZE,
    "process": U_INDUSTRY, "industrial": U_INDUSTRY, "factory": U_INDUSTRY, "district": U_INDUSTRY, 
    "community": U_COMMUNITY,
    "tracking": U_TRACKING, "concentration": U_TRACKING, "dish": U_TRACKING, "farm integration": U_TRACKING,
    "fruits": U_FRUITS,
    "vegetable": U_VEGETABLES,
    "spice": U_SPICES, 
    "grain": U_GRAINS, "pulse": U_GRAINS,
    "grid": U_GRID,
    "smart": U_TECH, "control": U_TECH, "app": U_TECH, "monitoring": U_TECH,
    "broccoli": U_PLANT, "radish": U_PLANT, "sunflower": U_PLANT, "pea": U_PLANT, "seed": U_PLANT, "harvest": U_PLANT, "agritech": U_PLANT, "agriculture": U_PLANT,
    "prototype": U_HARDWARE, "modular": U_HARDWARE, "array": U_HARDWARE, "parabolic": U_HARDWARE, "fresnel": U_HARDWARE, "biomass": U_HARDWARE, "rack": U_HARDWARE, "cooker": U_HARDWARE,
    "library": U_DOCS, "roi": U_DOCS, "video": U_DOCS, "model": U_DOCS, "report": U_DOCS, "study": U_DOCS, "call": U_DOCS, "data": U_DOCS,
    "light": U_LIGHTING,
    "water": U_WATER, "irrigation": U_WATER, "steam": U_WATER,
    "layer": U_STRUCTURE, "storage": U_STRUCTURE
}

ultra_css_animation = """
    /* ===== ENHANCED AOS ZIG-ZAG OVERRIDE ===== */
    .product-row[data-aos] {
        opacity: 0 !important;
        transition: opacity 1s cubic-bezier(0.16, 1, 0.3, 1), transform 1s cubic-bezier(0.16, 1, 0.3, 1) !important;
    }
    .product-row:nth-child(odd)[data-aos] { transform: translateX(-60px) !important; }
    .product-row:nth-child(even)[data-aos] { transform: translateX(60px) !important; }
    .product-row.aos-animate[data-aos] {
        opacity: 1 !important;
        transform: translateX(0) !important;
    }

    /* Override standard media to house massive SVGs */
    .product-media {
        background: linear-gradient(145deg, var(--background, #fff), #f3f3f5) !important;
        border-radius: 32px !important;
        border: 1px solid #e8e8ed !important;
        box-shadow: 0 30px 60px rgba(0,0,0,0.04) !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        padding: 4rem 2rem !important;
        margin: 0 !important;
        min-height: 400px !important; 
        transition: all 0.4s ease !important;
        overflow: visible !important;
    }

    .product-row:hover .product-media {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 40px 80px rgba(74, 139, 74, 0.12) !important;
        border-color: #d1ead1 !important;
    }
    
    .product-media .pro-icon-ultra {
        width: 220px !important;
        height: 220px !important;
    }

    @media (max-width: 768px) {
        .product-row:nth-child(n)[data-aos] { 
            transform: translateY(30px) !important; 
        }
        .product-media {
            min-height: 280px !important;
            padding: 2rem !important;
        }
        .product-media .pro-icon-ultra {
            width: 160px !important;
            height: 160px !important;
        }
    }

    /* ULTR-PREMIUM 3D SVGs */
    .pro-icon-ultra {
        overflow: visible;
        filter: drop-shadow(0 20px 40px rgba(74,139,74,0.3));
    }
    .ultra-background { animation: blobMorph 10s ease-in-out infinite alternate; transform-origin: center; }
    .ultra-float { animation: ultraFloat 6s ease-in-out infinite alternate; }
    .ultra-float-delay { animation: ultraFloat 6s ease-in-out 1.5s infinite alternate; }
    .ultra-float-delay-2 { animation: ultraFloat 6s ease-in-out 3s infinite alternate; }
    .ultra-pulse { animation: ultraPulse 3s ease-in-out infinite alternate; }
    .ultra-spin { animation: ultraSpin 24s linear infinite; transform-origin: center; }
    .ultra-spin-fast { animation: ultraSpin 8s linear infinite; transform-origin: center; }
    .ultra-orbit { animation: ultraOrbit 8s linear infinite; transform-origin: center; }

    @keyframes blobMorph {
        0% { transform: scale(0.85) translate(-5px, 5px); opacity: 0.15; }
        50% { transform: scale(1.1) translate(10px, -10px); opacity: 0.25; }
        100% { transform: scale(0.95) translate(-10px, 0); opacity: 0.1; }
    }
    @keyframes ultraFloat { 0% { transform: translateY(12px); } 100% { transform: translateY(-12px); } }
    @keyframes ultraPulse { 0% { transform: scale(0.92); opacity: 0.8; } 100% { transform: scale(1.08); opacity: 1; } }
    @keyframes ultraSpin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
"""

def extract_and_inject():
    for fname in os.listdir(solutions_dir):
        if not fname.endswith('.html'): continue
        filepath = os.path.join(solutions_dir, fname)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Step 1: Inject the massive CSS overwrite block into <style>
        if "/* ===== ENHANCED AOS ZIG-ZAG OVERRIDE ===== */" not in content:
            content = content.replace('</style>', ultra_css_animation + '\n  </style>')

        # Step 2: Use regex to replace .product-media placeholder text with the bespoke SVG
        # We need to map based on the <h2> closest to the product-media.
        # Find combination: <h2>TITLE</h2> followed by <div class="product-media">...</div>
        
        # We find <div class="product-row" ...> to </div> that ends it, but it's hard.
        # simpler: find <h2>(.*?)</h2> and the next matching <div class="product-media">...</div>
        
        # Find all <h2> matching
        pattern = re.compile(
            r'(<h2[^>]*>\s*(.*?)\s*</h2>.*?<div class="product-media"[^>]*>)\s*<div class="placeholder-text"[^>]*>.*?</div>\s*(</div>)',
            re.IGNORECASE | re.DOTALL
        )
        
        def contextual_swap(match):
            prefix = match.group(1) # up to <div class="product-media">
            title_text = match.group(2).lower()
            suffix = match.group(3) # </div>

            selected_svg = U_HARDWARE
            for word, svg in word_map.items():
                if word in title_text:
                    selected_svg = svg
                    break
                    
            return f'{prefix}\n{selected_svg}\n{suffix}'
            
        content = pattern.sub(contextual_swap, content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
extract_and_inject()
print("Zig-Zag SVGs successfully injected into all solutions pages!")

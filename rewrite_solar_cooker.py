import os

filepath = r"d:\kvb-green-energies-website\products\solar-steam-cooking.html"

def ultra_wrap(inner):
    common_defs = """
    <linearGradient id="gP" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="var(--primary-light)" />
        <stop offset="50%" stop-color="var(--primary)" />
        <stop offset="100%" stop-color="var(--primary-dark)" />
    </linearGradient>
    <linearGradient id="gA" x1="100%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" stop-color="#fff" stop-opacity="0.8" />
        <stop offset="100%" stop-color="var(--primary)" stop-opacity="0.4" />
    </linearGradient>
    <linearGradient id="gB" x1="0%" y1="100%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="var(--primary)" />
        <stop offset="100%" stop-color="#8fd18f" /> 
    </linearGradient>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stop-color="var(--primary)" stop-opacity="0.7"/>
        <stop offset="100%" stop-color="var(--primary)" stop-opacity="0"/>
    </radialGradient>
    """
    return f"""<svg class="pro-icon-ultra" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
    <defs>{common_defs}</defs>
    <path class="ultra-background" fill="url(#gP)" opacity="0.15" d="M150.2,42.4 C175.1,64.2 189.6,98.6 181.3,128.8 C172.9,159 141.6,185.1 108.3,188.7 C74.9,192.4 39.5,173.5 19.8,142.3 C0.1,111.1 -3.9,67.6 14.9,40.3 C33.7,13 75.3,1.9 110.8,4.6 C146.4,7.3 125.3,20.6 150.2,42.4 Z" />
    <circle class="ultra-pulse" cx="100" cy="100" r="80" fill="url(#glow)" />
    {inner}
    <circle cx="30" cy="40" r="4" fill="var(--primary-light)" class="ultra-float" />
    <circle cx="160" cy="150" r="6" fill="var(--primary)" class="ultra-float-delay" />
    <circle cx="180" cy="60" r="3" fill="var(--primary-dark)" class="ultra-float-delay-2" />
</svg>"""

U_HARDWARE = ultra_wrap("""
    <g class="ultra-spin-fast" transform-origin="100 100">
        <circle cx="100" cy="100" r="50" fill="none" stroke="url(#gP)" stroke-width="16" stroke-dasharray="30 15" />
        <circle cx="100" cy="100" r="30" fill="url(#gB)" />
        <circle cx="100" cy="100" r="15" fill="#fff" />
    </g>
    <path class="ultra-float" fill="url(#gA)" d="M50,100 L20,120 L20,80 Z M150,100 L180,120 L180,80 Z" />
""")
U_HEAT = ultra_wrap("""
    <g class="ultra-spin-fast" transform-origin="100 100">
        <path fill="url(#gA)" d="M100,20 L110,40 L100,30 L90,40 Z M180,100 L160,110 L170,100 L160,90 Z M100,180 L90,160 L100,170 L110,160 Z M20,100 L40,90 L30,100 L40,110 Z" />
    </g>
    <circle class="ultra-float" cx="100" cy="100" r="45" fill="url(#gP)" stroke="#fff" stroke-width="4" />
    <path class="ultra-pulse" fill="none" stroke="url(#gB)" stroke-width="6" stroke-linecap="round" d="M100,130 L100,80 M100,80 C100,70 110,70 110,80 L110,100 M110,80 C110,60 130,60 130,80 L130,120 M130,80 C130,50 150,50 150,80 L150,140" transform="translate(-25, -20) scale(0.8)"/>
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
U_STERILIZE = ultra_wrap("""
    <path class="ultra-float" fill="url(#gP)" d="M100,40 C140,40 160,80 160,120 C160,160 140,180 100,180 C60,180 40,160 40,120 C40,80 60,40 100,40 Z" />
    <g class="ultra-pulse" stroke="#fff" stroke-width="8" stroke-linecap="round">
        <line x1="70" y1="150" x2="130" y2="150" />
        <line x1="80" y1="130" x2="120" y2="130" />
        <line x1="90" y1="110" x2="110" y2="110" />
    </g>
    <circle cx="100" cy="100" r="25" fill="none" stroke="url(#gB)" stroke-width="6" class="ultra-float-delay" />
""")
U_EFFICIENCY = ultra_wrap("""
    <g class="ultra-spin-fast" transform-origin="100 100">
        <path fill="none" stroke="url(#gB)" stroke-width="12" stroke-linecap="round" stroke-dasharray="80 40" d="M100,30 A70,70 0 1,1 99,30" />
        <polygon points="90,20 120,30 90,40" fill="url(#gB)" />
    </g>
    <path class="ultra-float" fill="#fff" d="M105,60 L85,110 L110,110 L95,140 L125,90 L100,90 Z" />
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
U_COMMUNITY = ultra_wrap("""
    <circle class="ultra-pulse" cx="100" cy="100" r="40" fill="url(#gP)" stroke="#fff" stroke-width="4"/>
    <g class="ultra-spin">
        <circle cx="100" cy="30" r="15" fill="url(#gB)" />
        <circle cx="160" cy="140" r="15" fill="url(#gB)" />
        <circle cx="40" cy="140" r="15" fill="url(#gB)" />
        <path fill="none" stroke="url(#gB)" stroke-width="4" d="M100,45 L100,60 M145,130 L130,115 M55,130 L70,115" />
    </g>
""")

css_block = """
        /* ===== ULTIMATE PREMIUM ZIG-ZAG LAYOUT OVERRIDE ===== */
        .specs-grid, .applications-grid {
            display: flex !important;
            flex-direction: column !important;
            gap: 6rem !important;
            margin: 6rem 0 !important;
        }

        .spec-card, .app-card, .application-card, .spec-highlight-card {
            animation: none !important;
            display: grid !important;
            grid-template-rows: auto auto !important;
            gap: 3rem !important;
            background: transparent !important;
            border: none !important;
            padding: 0 !important;
            align-items: center !important;
            will-change: transform, opacity;
            transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .spec-card:nth-child(odd), .app-card:nth-child(odd) {
            grid-template-columns: 1.1fr 1fr !important;
            grid-template-areas: "title visual" "desc visual" !important;
            transform: translateX(-60px); opacity: 0;
        }

        .spec-card:nth-child(even), .app-card:nth-child(even) {
            grid-template-columns: 1fr 1.1fr !important;
            grid-template-areas: "visual title" "visual desc" !important;
            transform: translateX(60px); opacity: 0;
        }

        .spec-card.visible, .app-card.visible { transform: translateX(0) !important; opacity: 1 !important; }

        .spec-card h3, .app-card h3 {
            grid-area: title !important;
            font-size: 2.2rem !important; margin-bottom: 1rem !important;
            color: var(--text-primary) !important; align-self: end !important;
        }

        .spec-card p, .app-card p {
            grid-area: desc !important;
            font-size: 1.15rem !important; color: var(--text-secondary) !important;
            line-height: 1.7 !important; max-width: 90% !important;
            margin-bottom: 0 !important; align-self: start !important;
        }

        .pro-icon-ultra {
            grid-area: visual !important;
            width: 100% !important; min-height: 380px !important;
            background: linear-gradient(145deg, var(--background), #f3f3f5) !important;
            border-radius: 32px !important; border: 1px solid var(--border) !important;
            box-shadow: 0 30px 60px rgba(0,0,0,0.04) !important;
            display: flex !important; align-items: center !important; justify-content: center !important;
            padding: 3rem !important; margin: 0 !important; transition: all 0.4s ease !important;
        }

        .spec-card:hover .pro-icon-ultra, .app-card:hover .pro-icon-ultra {
            transform: translateY(-10px) scale(1.02) !important;
            box-shadow: 0 40px 80px rgba(74, 139, 74, 0.12) !important; border-color: var(--primary-light) !important;
        }

        @media (max-width: 992px) {
            .spec-card:nth-child(n), .app-card:nth-child(n) {
                grid-template-columns: 1fr !important; grid-template-areas: "visual" "title" "desc" !important;
                transform: translateY(40px) !important; text-align: center !important;
            }
            .pro-icon-ultra { min-height: 300px !important; }
            .spec-card h3, .app-card h3 { font-size: 1.8rem !important; align-self: center !important; }
            .spec-card p, .app-card p { align-self: center !important; margin: 0 auto !important; }
        }
"""

with open(filepath, 'r', encoding='utf-8') as f:
    original = f.read()

# Isolate the top (up to </style>)
header_part = original.split("</head>")[0]
if "/* ===== ULTIMATE PREMIUM ZIG-ZAG LAYOUT OVERRIDE ===== */" not in header_part:
    header_part = header_part.replace("</style>", css_block + "\n</style>")

# Replace the specific animations natively just in case
header_part = header_part.replace("animation: fadeUp 0.6s forwards;", "/* animation disabled */")

# Build the body
body_new = f"""</head>
<body>
    <div id="header"></div>

    <!-- ===== HERO SECTION ===== -->
    <section class="product-hero">
        <div class="container">
            <div class="hero-grid">
                <!-- left: text -->
                <div class="hero-left">
                    <h1>Solar Parabolic Cooker</h1>
                    <p>Efficient Solar Cooking Solutions for All Scales. High-efficiency cooking system that uses sunlight as its primary energy source, available in 1.5 m² & 4 m².</p>
                    <div class="product-tags">
                        <span class="tag"><i class="fas fa-temperature-high"></i> 150°C to 350°C</span>
                        <span class="tag"><i class="fas fa-sun"></i> Zero Fuel Cost</span>
                        <span class="tag"><i class="fas fa-leaf"></i> Carbon Neutral</span>
                        <span class="tag"><i class="fas fa-rupee-sign"></i> 1‑2 Year ROI</span>
                        <span class="tag"><i class="fas fa-cogs"></i> Manual Tracking</span>
                        <span class="tag"><i class="fas fa-users"></i> 10-30 Persons Capacity</span>
                    </div>
                </div>
                <!-- right: product video -->
                <div class="hero-right">
                    <div class="shine"></div>
                    <iframe
                        src="https://www.youtube.com/embed/wCM_D2bMMRY?autoplay=1&mute=1&loop=1&playlist=wCM_D2bMMRY&controls=0&rel=0&modestbranding=1"
                        title="Parabolic Solar Cooker Demo"
                        frameborder="0"
                        allow="autoplay; fullscreen; picture-in-picture"
                        allowfullscreen>
                    </iframe>
                </div>
            </div>
        </div>
    </section>

    <!-- ===== PRODUCT CONTENT ===== -->
    <section class="product-content">
        <div class="container">
            <h2 class="section-title">Core System</h2>
            <div class="specs-grid">
                <div class="spec-card">
                    {U_HARDWARE}
                    <h3>General Description</h3>
                    <p>The Solar Parabolic Cooker is a high-efficiency cooking system that uses sunlight as its primary energy source. KVB Green Energies offers this system in two sizes — 1.5 Sq. Meter and 4 Sq. Meter, making it suitable for both small-scale and community-level cooking applications. The 1.5 m² model is suitable for small kitchens, while the 4 m² model is designed for larger applications such as temples, hostels, and canteens.</p>
                </div>
                <div class="spec-card">
                    {U_HEAT}
                    <h3>Cooking Performance</h3>
                    <p>Suitable for a wide range of cooking applications including <strong>Boiling, Frying, Steaming, and Roasting</strong>. Typical cooking times are remarkably fast: Rice in 30–45 minutes, Dal in 40–60 minutes, and Vegetables in 20–30 minutes directly using concentrated solar energy.</p>
                </div>
                <div class="spec-card">
                    {U_STRUCTURE}
                    <h3>System Components</h3>
                    <p>The entire setup includes a high-reflectivity Parabolic Dish, a robust Support Structure with Base Frame, a Manual Tracking Mechanism, Receiver / Cooking Vessel Stand, Safety Locking System, and an Optional High-Temperature Cooking Vessel.</p>
                </div>
                <div class="spec-card">
                    {U_STERILIZE}
                    <h3>Safety Features</h3>
                    <p>Designed for absolute operator confidence, featuring a wind locking mechanism for extreme weather, highly stable structural design, heat-resistant receiver materials, and safely controlled manual operation protocols.</p>
                </div>
                <div class="spec-card">
                    {U_EFFICIENCY}
                    <h3>Key Benefits</h3>
                    <p>Eliminates dependency on conventional fuels and drastically reduces carbon emissions. It provides a highly attractive payback period of just 1–2 years, boasts a system life of 15–20 years, and requires purely minimal maintenance.</p>
                </div>
                <div class="spec-card">
                    {U_TECH}
                    <h3>Installation & Maintenance</h3>
                    <p>Initial installation time is rapid, taking only 1–2 days. Long term maintenance is minimal, requiring only periodic cleaning of the reflector surface and basic lubrication of the moving parts to ensure optimal tracking.</p>
                </div>
                <div class="spec-card">
                    {U_COMMUNITY}
                    <h3>Applications</h3>
                    <p>Perfectly integrated into Temples & Ashrams, Residential Schools & Hostels, diverse Community Kitchens, Rural & Tribal Areas, and Small-scale Catering operations requiring massive thermal inputs without the fuel overhead.</p>
                </div>
            </div>

            <!-- Technical Specifications -->
            <div class="tech-table-container">
                <h2 style="color: var(--text-primary); margin-bottom: 2rem;">Technical Details</h2>
                <table class="tech-table">
                    <thead><tr><th>Parameter</th><th>Specification</th></tr></thead>
                    <tbody>
                        <tr><td><strong>Reflector Area</strong></td><td>1.5 m² & 4 m² (Available Options)</td></tr>
                        <tr><td><strong>Type</strong></td><td>Parabolic Dish Concentrator</td></tr>
                        <tr><td><strong>Reflector Material</strong></td><td>High reflectivity aluminum / mirror finish</td></tr>
                        <tr><td><strong>Reflectivity</strong></td><td>≥ 90%</td></tr>
                        <tr><td><strong>Structure Material</strong></td><td>Mild Steel with anti-corrosion coating</td></tr>
                        <tr><td><strong>Tracking System</strong></td><td>Manual (Single Axis)</td></tr>
                        <tr><td><strong>Concentration Ratio</strong></td><td>60:1 to 120:1</td></tr>
                        <tr><td><strong>Focal Length</strong></td><td>~0.8 to 1.5 meters</td></tr>
                        <tr><td><strong>Operating Temperature</strong></td><td>150°C to 350°C</td></tr>
                        <tr><td><strong>Cooking Capacity</strong></td><td>10–30 persons (based on model)</td></tr>
                        <tr><td><strong>Mounting Type</strong></td><td>Ground mounted</td></tr>
                        <tr><td><strong>Wind Resistance</strong></td><td>Up to 120 km/h (with locking mechanism)</td></tr>
                    </tbody>
                </table>
            </div>

            <div class="tech-table-container">
                <h2 style="color: var(--text-primary); margin-bottom: 2rem;">Solar Performance</h2>
                <table class="tech-table">
                    <thead><tr><th>Parameter</th><th>Value</th></tr></thead>
                    <tbody>
                        <tr><td><strong>Thermal Output</strong></td><td>1 kW – 3.5 kW (based on model)</td></tr>
                        <tr><td><strong>Solar Efficiency</strong></td><td>50% – 65%</td></tr>
                        <tr><td><strong>Daily Cooking Hours</strong></td><td>5–7 hours (under clear sky conditions)</td></tr>
                        <tr><td><strong>Fuel Savings</strong></td><td>Significant reduction in LPG usage</td></tr>
                    </tbody>
                </table>
            </div>
        </div>
    </section>
"""

# Extract the Unlock Premium and footer section from the original to preserve logic
footer_part = original.split("<!-- ===== PREMIUM UNLOCK (unchanged) ===== -->")[1]

final_html = header_part + body_new + "\n    <!-- ===== PREMIUM UNLOCK (unchanged) ===== -->\n" + footer_part

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Solar Parabolic Cooker successfully updated and rewritten!")

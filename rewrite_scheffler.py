import os

filepath = r"d:\kvb-green-energies-website\products\scheffler-concentrators.html"

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
            .pro-icon-ultra { min-height: 300px !important; padding: 1.5rem !important; }
            .spec-card h3, .app-card h3 { font-size: 1.8rem !important; align-self: center !important; }
            .spec-card p, .app-card p { align-self: center !important; margin: 0 auto !important; }
        }
"""

with open(filepath, 'r', encoding='utf-8') as f:
    original = f.read()

header_part = original.split("</head>")[0]
if "/* ===== ULTIMATE PREMIUM ZIG-ZAG LAYOUT OVERRIDE ===== */" not in header_part:
    header_part = header_part.replace("</style>", css_block + "\n</style>")

header_part = header_part.replace("animation: fadeUp 0.6s forwards;", "/* animation disabled */")

body_new = f"""</head>
<body>
    <div id="header"></div>

    <!-- ===== HERO SECTION ===== -->
    <section class="product-hero">
        <div class="container">
            <div class="hero-grid">
                <!-- left: text -->
                <div class="hero-left">
                    <h1>16 m² Solar Scheffler Dish</h1>
                    <p>Direct Cooking System – Technical Specifications. High-performance solar thermal system engineered for large-scale direct cooking applications inside the kitchen.</p>
                    <div class="product-tags">
                        <span class="tag"><i class="fas fa-temperature-high"></i> 350°C to 450°C</span>
                        <span class="tag"><i class="fas fa-sun"></i> 8 kW – 10 kW Peak</span>
                        <span class="tag"><i class="fas fa-leaf"></i> 10-12 Tons CO₂ Drop</span>
                        <span class="tag"><i class="fas fa-rupee-sign"></i> 2‑4 Year ROI</span>
                        <span class="tag"><i class="fas fa-cogs"></i> Fixed Focus Tracking</span>
                        <span class="tag"><i class="fas fa-users"></i> 80-100 Persons Batch</span>
                    </div>
                </div>
                <!-- right: product visual -->
                <div class="hero-right">
                    <div class="shine"></div>
                    <img src="https://images.unsplash.com/photo-1508514177221-188b1cf16e9d?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80" alt="Scheffler Concentrator System" style="width:100%; height:100%; object-fit:cover;">
                </div>
            </div>
        </div>
    </section>

    <!-- ===== PRODUCT CONTENT ===== -->
    <section class="product-content">
        <div class="container">
            <h2 class="section-title">System Ecosystem</h2>
            <div class="specs-grid">
                <div class="spec-card">
                    {U_HARDWARE}
                    <h3>General Description</h3>
                    <div>
                        <p style="margin-bottom:1rem;">The 16 m² Solar Scheffler Dish is a high-performance solar thermal system engineered for large-scale direct cooking applications. Unlike conventional solar cookers, this system uses a fixed-focus Scheffler geometry, allowing the reflected solar energy to be directed to a stationary receiver located inside the kitchen.</p>
                        <p>This design ensures continuous, safe, and indoor cooking, while the reflector automatically tracks the sun’s movement. It is an ideal solution for institutions aiming to eliminate fossil fuel dependency and adopt sustainable cooking practices.</p>
                    </div>
                </div>
                
                <div class="spec-card">
                    {U_HEAT}
                    <h3>Cooking Performance</h3>
                    <div>
                        <p style="margin-bottom:1rem;">The system is designed for high-volume cooking with consistent thermal output, making it highly suitable for institutional kitchens.</p>
                        <ul style="list-style:none; padding:0; font-size:1.15rem; color:var(--text-secondary); line-height:1.7;">
                            <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> <strong>Cooking Mode:</strong> Direct cooking at fixed receiver inside kitchen</li>
                            <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> <strong>Batch Capacity:</strong> 80–100 persons per cooking cycle</li>
                            <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> <strong>Typical Output:</strong> Rice: 15–20 kg in 40–60 mins</li>
                            <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> <strong>Typical Output:</strong> Dal / Sambar: 20–25 liters in 45–60 mins</li>
                            <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> <strong>Typical Output:</strong> Vegetables: 25–30 kg in 30–45 mins</li>
                            <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> <strong>Frying / Chapati:</strong> Supported with appropriate cookware</li>
                        </ul>
                    </div>
                </div>
                
                <div class="spec-card">
                    {U_STRUCTURE}
                    <h3>System Components</h3>
                    <div>
                        <p style="margin-bottom:1rem;">The complete system is supplied as an integrated solution consisting of:</p>
                        <ul style="list-style:none; padding:0; font-size:1.15rem; color:var(--text-secondary); line-height:1.7;">
                            <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> 16 m² Scheffler Reflector Assembly</li>
                            <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> Precision Solar Tracking Mechanism</li>
                            <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> Fixed Receiver Unit (installed inside kitchen)</li>
                            <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> Structural Support Frame with Foundation Interface</li>
                            <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> Heat Transfer Interface / Cooking Plate</li>
                            <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> Seasonal Tilt Adjustment System</li>
                            <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> Safety Locking & Stow Arrangement</li>
                        </ul>
                    </div>
                </div>
                
                <div class="spec-card">
                    {U_STERILIZE}
                    <h3>Safety Features</h3>
                    <div>
                        <p style="margin-bottom:1rem;">The system is engineered with multiple safety considerations for long-term and reliable operation:</p>
                        <ul style="list-style:none; padding:0; font-size:1.15rem; color:var(--text-secondary); line-height:1.7;">
                            <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> Fixed focal point eliminates operator exposure to reflected rays</li>
                            <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> Wind stow mechanism for high-speed wind protection</li>
                            <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> Controlled heat delivery at receiver location</li>
                            <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> No glare or open flame in cooking area</li>
                            <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> Heavy-duty structural stability</li>
                        </ul>
                    </div>
                </div>
                
                <div class="spec-card">
                    {U_EFFICIENCY}
                    <h3>Key Benefits</h3>
                    <ul style="list-style:none; padding:0; font-size:1.15rem; color:var(--text-secondary); line-height:1.7;">
                        <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> Eliminates LPG / firewood consumption</li>
                        <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> Reduces CO₂ emissions up to 10–12 tons annually</li>
                        <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> Highly economical with 2–4 years payback</li>
                        <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> Long service life of 20–25 years</li>
                        <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> Suitable for daily, continuous cooking operations</li>
                        <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> Supports carbon credit generation opportunities</li>
                    </ul>
                </div>
                
                <div class="spec-card">
                    {U_TECH}
                    <h3>Installation & Maintenance</h3>
                    <ul style="list-style:none; padding:0; font-size:1.15rem; color:var(--text-secondary); line-height:1.7;">
                        <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> <strong>Installation Requirements:</strong> Civil foundation required</li>
                        <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> <strong>Installation Duration:</strong> 3–5 days</li>
                        <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> <strong>Maintenance:</strong> Routine cleaning of reflector mirrors for optimal efficiency</li>
                        <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> <strong>Maintenance:</strong> Lubrication of tracking joints and bearings</li>
                        <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> <strong>Maintenance:</strong> Periodic inspection of alignment and structure</li>
                    </ul>
                </div>
                
                <div class="spec-card">
                    {U_COMMUNITY}
                    <h3>Applications</h3>
                    <div>
                        <p style="margin-bottom:1rem;">This system is widely deployed across high-demand cooking environments:</p>
                        <ul style="list-style:none; padding:0; font-size:1.15rem; color:var(--text-secondary); line-height:1.7;">
                            <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> Temples & Ashrams (Maths)</li>
                            <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> Residential Schools & Hostels</li>
                            <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> Mid-Day Meal Kitchens</li>
                            <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> Industrial Canteens</li>
                            <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> Defense Kitchens (Army / Police / Paramilitary)</li>
                            <li><i class="fas fa-check-circle" style="color:var(--primary);margin-right:8px;"></i> Large Community Cooking Facilities</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- Technical Specifications -->
            <div class="tech-table-container">
                <h2 style="color: var(--text-primary); margin-bottom: 2rem;">Technical Specifications</h2>
                <table class="tech-table">
                    <thead><tr><th>Parameter</th><th>Specification</th></tr></thead>
                    <tbody>
                        <tr><td><strong>Reflector Area</strong></td><td>16 Square Meter</td></tr>
                        <tr><td><strong>System Type</strong></td><td>Scheffler Fixed Focus Parabolic Dish</td></tr>
                        <tr><td><strong>Reflector Material</strong></td><td>High Reflectivity Glass Mirrors / Anodized Aluminum</td></tr>
                        <tr><td><strong>Reflectivity</strong></td><td>≥ 90%</td></tr>
                        <tr><td><strong>Structure Material</strong></td><td>Mild Steel (Hot Dip Galvanized / Anti-corrosion Coated)</td></tr>
                        <tr><td><strong>Tracking System</strong></td><td>Manual / Semi-Automatic (Single Axis with Seasonal Adjustment)</td></tr>
                        <tr><td><strong>Focal Length</strong></td><td>~2.5 to 3.0 meters</td></tr>
                        <tr><td><strong>Concentration Ratio</strong></td><td>100:1 to 150:1</td></tr>
                        <tr><td><strong>Operating Temperature</strong></td><td>350°C to 450°C</td></tr>
                        <tr><td><strong>Mounting Type</strong></td><td>Ground Mounted with RCC Foundation</td></tr>
                        <tr><td><strong>Wind Resistance</strong></td><td>Up to 140 km/h (with stow mechanism)</td></tr>
                    </tbody>
                </table>
            </div>

            <!-- Solar Thermal Performance -->
            <div class="tech-table-container">
                <h2 style="color: var(--text-primary); margin-bottom: 2rem;">Solar Thermal Performance</h2>
                <table class="tech-table">
                    <thead><tr><th>Parameter</th><th>Value</th></tr></thead>
                    <tbody>
                        <tr><td><strong>Peak Thermal Output</strong></td><td>8 kW – 10 kW</td></tr>
                        <tr><td><strong>System Efficiency</strong></td><td>55% – 70%</td></tr>
                        <tr><td><strong>Effective Cooking Duration</strong></td><td>5–7 hours/day (clear sky conditions)</td></tr>
                        <tr><td><strong>Fuel Savings</strong></td><td>Equivalent to ~3–4 kg LPG/day</td></tr>
                    </tbody>
                </table>
            </div>
        </div>
    </section>
"""

# Preserve the Premium section functionality (it acts as a great lead generator)
parts = original.split("<!-- ===== PREMIUM UNLOCK (unchanged) ===== -->")
if len(parts) > 1:
    footer_part = parts[1]
else:
    # If not found, split by footer
    footer_part = original.split('<div id="footer"></div>')[-1]
    footer_part = '<div id="footer"></div>' + footer_part

final_html = header_part + body_new + "\n    <!-- ===== PREMIUM UNLOCK (unchanged) ===== -->\n" + footer_part

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Scheffler Concentrators page mapped and entirely rebuilt!")

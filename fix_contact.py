import re

def fix_contact():
    with open('d:/kvb-green-energies-website/public/contact.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update fonts
    content = re.sub(
        r'href="https://fonts\.googleapis\.com/css2\?family=Montserrat:wght@400;500;600;700&family=Inter:wght@300;400;500;600&display=swap"',
        r'href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&family=Inter:wght@300;400;500;600;700;800&display=swap"',
        content
    )

    # 2. Update :root CSS
    root_css = """        :root {
            --solar-yellow: #FDB813;
            --deep-blue: #0B3D91;
            --eco-green: #3A7D44;
            --dark-charcoal: #1C1C1C;
            --soft-white: #F9F9F9;
            --accent-orange: #FF6F00;
            --background: #F9F9F9;
            --background-alt: #FFFFFF;
            --text-primary: #1C1C1C;
            --text-secondary: #4a5568;
            --text-tertiary: #A1A1A6;
            --border: #e0e8e0;
            --primary: #3A7D44;
            --primary-dark: #2d5a33;
            --primary-light: #e6f3e6;
            --primary-glow: rgba(58, 125, 68, 0.15);
            --shadow-sm: 0 10px 30px rgba(28,28,28,0.04);
            --shadow-md: 0 20px 40px rgba(58,125,68,0.08);
            --shadow-lg: 0 16px 40px rgba(0,0,0,0.12);
            --radius-sm: 12px;
            --radius-md: 20px;
            --radius-lg: 28px;
            --font-heading: 'Montserrat', sans-serif;
            --font-body: 'Inter', sans-serif;
        }"""
    content = re.sub(r':root\s*\{[^}]+\}', root_css, content, count=1)

    # 3. Update .section-title
    section_title_css = """        .section-title {
            font-size: 2.5rem;
            font-weight: 700;
            font-family: 'Montserrat', sans-serif;
            color: var(--deep-blue);
            text-align: center;
            position: relative;
            display: block;
            margin-bottom: 26px;
        }

        .section-title::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
            width: 80px;
            height: 4px;
            background: var(--solar-yellow);
            border-radius: 2px;
        }"""
    # Regex to match .section-title and .section-title:after
    content = re.sub(r'\.section-title\s*\{[^}]+\}\s*\.section-title:after\s*\{[^}]+\}', section_title_css, content)

    # 4. Update .contact-hero
    hero_css = """        .contact-hero {
            position: relative;
            min-height: 55vh;
            display: flex;
            align-items: center;
            background: linear-gradient(135deg, #09203f 0%, #0f3460 40%, #1a5276 100%);
            overflow: hidden;
            color: white;
            padding: 100px 0 60px;
        }

        .contact-hero::before {
            content: '';
            position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            background:
                radial-gradient(circle at 15% 50%, rgba(0,255,135,0.12) 0%, transparent 55%),
                radial-gradient(circle at 85% 30%, rgba(253,184,19,0.08) 0%, transparent 40%);
            animation: heroPulse 8s infinite alternate;
            z-index: 1;
        }

        .contact-hero::after {
            content: '';
            position: absolute; bottom: -2px; left: 0; width: 100%; height: 80px;
            background: url("data:image/svg+xml,%3Csvg viewBox='0 0 1440 80' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill='%23F9F9F9' d='M0,40 C360,80 1080,0 1440,40 L1440,80 L0,80 Z'/%3E%3C/svg%3E") no-repeat bottom;
            background-size: cover;
            z-index: 2;
        }

        @keyframes heroPulse {
            0% { opacity: 0.9; }
            100% { opacity: 1; }
        }

        .hero-content {
            max-width: 800px;
            margin: 0 auto;
            position: relative;
            z-index: 3;
            text-align: center;
        }

        .hero-content h1 {
            color: white;
            font-size: 3.5rem;
            font-weight: 900;
        }

        .hero-content .hero-subtitle {
            font-size: 1.4rem;
            color: rgba(255, 255, 255, 0.9);
            font-weight: 300;
            margin-bottom: 1.5rem;
        }

        .hero-content .hero-description {
            color: rgba(255, 255, 255, 0.8);
            margin-bottom: 2.5rem;
        }

        .contact-quick-links {
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
            justify-content: center;
            margin-top: 2rem;
        }"""
    
    # regex replace from .contact-hero { to .contact-quick-links { ... }
    content = re.sub(r'\.contact-hero\s*\{.*?\.contact-quick-links\s*\{[^}]+\}', hero_css, content, flags=re.DOTALL)

    # 5. Fix form CTA gradient
    cta_gradient = """        .contact-cta {
            padding: 5rem 0;
            background: linear-gradient(135deg, #09203f 0%, #0f3460 40%, #1a5276 100%);
            color: white;
            text-align: center;
            position: relative;
        }"""
    content = re.sub(r'\.contact-cta\s*\{[^}]+\}', cta_gradient, content, count=1)

    with open('d:/kvb-green-energies-website/public/contact.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    fix_contact()

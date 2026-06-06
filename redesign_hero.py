import os
import glob
import re

app_dir = r"d:\kvb-green-energies-website\public\app"
files = glob.glob(os.path.join(app_dir, "*.html"))

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Remove the badge
    # It looks like: <div class="badge"><i class="fas fa-leaf"></i> Tea processing heat reimagined</div>
    # or similar. It's right above <h1>.
    content = re.sub(r'<div class="badge">.*?</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<span class="badge">.*?</span>', '', content, flags=re.DOTALL)
    
    # 2. Update .hero-section h1 styles
    # Replace existing h1 { ... } inside <style>
    # We will search for h1 { ... } and replace the contents if it's in the CSS.
    # The existing h1 CSS is:
    # h1 {
    #         font-size: 4rem;
    #         font-weight: 900;
    #         line-height: 1.2;
    #         color: white;
    #         margin-bottom: 25px;
    #     }
    new_h1_css = """h1 {
            font-size: 3.8rem;
            margin-bottom: 1.5rem;
            color: #ffffff; /* Match logo theme color for contrast, logo has white/green/yellow */
            font-weight: 800;
            line-height: 1.15;
            letter-spacing: -1px;
            font-family: 'Montserrat', sans-serif;
        }"""
    content = re.sub(r'h1\s*\{[^}]*\}', new_h1_css, content, count=1)
    
    # 3. Update .hero-section background
    # The existing is:
    # .hero-section {
    #     background-color: var(--green-accent);
    #     color: white;
    # }
    new_hero_css = """.hero-section {
            background-color: #2E7D32; /* Eco green */
            color: white;
        }"""
    content = re.sub(r'\.hero-section\s*\{[^}]*\}', new_hero_css, content, count=1)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print(f"Updated {len(files)} files.")

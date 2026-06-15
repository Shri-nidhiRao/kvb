import os
import re

directory = 'd:/kvb-green-energies-website/public'
html_files = []

for root, _, files in os.walk(directory):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

# Regex to find <img> tags
img_pattern = re.compile(r'<img\s+([^>]+)>')

def update_img_tag(match):
    attrs_str = match.group(1)
    
    # Check if it's already processed or is a special image
    is_hero = 'hero' in attrs_str.lower() or 'logo' in attrs_str.lower() or 'kvb-logo' in attrs_str.lower()
    
    # Remove existing loading, decoding, fetchpriority
    attrs_str = re.sub(r'\s+loading=[\'"][^\'"]*[\'"]', '', attrs_str)
    attrs_str = re.sub(r'\s+decoding=[\'"][^\'"]*[\'"]', '', attrs_str)
    attrs_str = re.sub(r'\s+fetchpriority=[\'"][^\'"]*[\'"]', '', attrs_str)
    
    if is_hero:
        return f'<img {attrs_str.strip()} fetchpriority="high" decoding="async">'
    else:
        return f'<img {attrs_str.strip()} loading="lazy" decoding="async">'

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = img_pattern.sub(update_img_tag, content)
        
        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated images in {filepath}")
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

print("Image optimization complete.")

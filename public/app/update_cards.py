import os
import re

directory = "d:/kvb-green-energies-website/public/app"
files = [
    "automobile-industry.html",
    "chemical-industry.html",
    "dairy-industry.html",
    "food-processing-industry.html",
    "leather-footwear.html",
    "paper-pulp-industry.html",
    "tea-processing-industry.html",
    "textile-industry.html"
]

card_pattern = re.compile(
    r'<div class="card" style="text-align: left; padding: 2rem;[^>]*>.*?<h4[^>]*><i class="(.*?)"[^>]*></i> (.*?)</h4>.*?<ul[^>]*>(.*?)</ul>.*?</div>',
    re.DOTALL
)

li_pattern = re.compile(r'<li[^>]*><i class="fas fa-arrow-right"[^>]*></i><span>(.*?)</span></li>', re.DOTALL)
li_pattern_alt = re.compile(r'<li[^>]*><i class="fas fa-arrow-right"[^>]*></i>(.*?)</li>', re.DOTALL)

def replace_card(match):
    icon_class = match.group(1)
    title_text = match.group(2)
    ul_content = match.group(3)
    
    # Process li items
    clean_lis = li_pattern.sub(r'<li>\1</li>', ul_content)
    # Just in case there was no span
    clean_lis = li_pattern_alt.sub(r'<li>\1</li>', clean_lis)
    
    return f'''<div class="impact-card" style="height: 100%;">
                        <div class="impact-header">
                            <h4 style="color: #FF9800; font-size: 1.25rem; margin: 0; display: flex; align-items: center; gap: 10px; font-weight: 800; font-family: 'Montserrat', sans-serif;"><i class="{icon_class}" style="color: #FF9800;"></i> {title_text}</h4>
                        </div>
                        <div class="impact-body">
                            <ul>{clean_lis}</ul>
                        </div>
                    </div>'''

for filename in files:
    filepath = os.path.join(directory, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = card_pattern.sub(replace_card, content)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Updated {filename}")

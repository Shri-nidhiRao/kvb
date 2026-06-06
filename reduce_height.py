import os
import re

app_dir = r"d:\kvb-green-energies-website\public\app"
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

for file in files:
    filepath = os.path.join(app_dir, file)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The regex approach. We know the block starts with /* ===== Premium Smart Solution Redesign ===== */
    # and ends with @media (max-width: 600px) { ... } \n    }
    
    pattern = r'(/\* ===== Premium Smart Solution Redesign ===== \*/\s*\.smart-solution-redesign \{ max-width: 1100px.*?@media \(max-width: 600px\) \{[^}]+\}[^}]+\})'
    
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        print(f"Could not find CSS block in {file}")
        continue
        
    original_block = match.group(1)
    
    # We will compute the indentation based on the first line of the original block
    # Actually, we can just build the new block without capturing indentation and just indent line by line
    
    # Let's get the exact indentation of the first line
    indent_match = re.search(r'^([ \t]+)/\* ===== Premium Smart Solution Redesign ===== \*/', content, re.MULTILINE)
    indent = indent_match.group(1) if indent_match else "    "

    new_css = """/* ===== Premium Smart Solution Redesign ===== */
.smart-solution-redesign { max-width: 1100px; margin: 0 auto; text-align: center; font-family: 'Inter', sans-serif; }

.section-divider { display: flex; align-items: center; justify-content: center; margin: 1.5rem 0 1rem; gap: 15px; }
.divider-line { height: 1px; background: #2c6e49; flex-grow: 1; max-width: 150px; position: relative; }
.divider-line::before { content: ''; position: absolute; width: 6px; height: 6px; background: #2c6e49; border-radius: 50%; top: -2.5px; }
.divider-line.left::before { right: 0; }
.divider-line.right::before { left: 0; }
.divider-text { font-size: 1.4rem; color: #114227; font-weight: 700; margin: 0; }

.solution-grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.25rem; margin-bottom: 1.5rem; }
.solution-card { background: #ffffff; border: 1px solid #eaeaea; border-radius: 12px; padding: 1.5rem 1rem; display: flex; flex-direction: column; align-items: center; box-shadow: 0 4px 15px rgba(0,0,0,0.03); position: relative; overflow: hidden; transition: transform 0.3s ease; }
.solution-card:hover { transform: translateY(-5px); box-shadow: 0 10px 25px rgba(0,0,0,0.06); }
.solution-card::after { content: ''; position: absolute; bottom: 0; left: 0; width: 100%; height: 6px; }
.card-green::after { background: #1f8a70; }
.card-light-green::after { background: #9dcd5a; }
.card-yellow::after { background: #fbc02d; }
.card-blue::after { background: #1565c0; }

.card-icon-circle { width: 50px; height: 50px; background: #eef7f0; color: #2c6e49; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.4rem; margin-bottom: 1rem; }
.card-text { font-size: 0.9rem; color: #515154; line-height: 1.4; }
.card-text strong { color: #1d1d1f; display: block; margin-bottom: 3px; font-size: 1rem; }

.impact-box { background: #f6fcf8; border: 1px solid #e3f2e8; border-radius: 12px; padding: 1.25rem; display: flex; align-items: center; gap: 1.5rem; margin-bottom: 1.5rem; flex-wrap: wrap; }
.impact-left { display: flex; align-items: center; gap: 12px; border-right: 2px solid #e3f2e8; padding-right: 1.5rem; }
.impact-main-icon { font-size: 2.2rem; color: #2c6e49; }
.impact-title { font-size: 1.1rem; font-weight: 700; color: #114227; line-height: 1.2; }

.impact-items { display: flex; gap: 1.5rem; flex-grow: 1; justify-content: space-around; }
.impact-item { display: flex; align-items: center; gap: 12px; text-align: left; }
.impact-icon { width: 36px; height: 36px; background: #2c6e49; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1rem; flex-shrink: 0; }
.impact-item-text { font-size: 0.85rem; color: #1d1d1f; line-height: 1.3; }
.impact-item-text strong { display: block; font-size: 0.95rem; }

.impact-conclusion-bar { background: #0f4b2b; color: white; border-radius: 8px; padding: 0.85rem 1.5rem; display: flex; align-items: center; justify-content: center; gap: 10px; font-size: 1.05rem; font-weight: 500; }
.impact-conclusion-bar .fa-check-circle { color: #ffffff; font-size: 1.2rem; }
.highlight-yellow { color: #ffca28; }

@media (max-width: 1024px) {
    .solution-grid-4 { grid-template-columns: repeat(2, 1fr); }
    .impact-box { flex-direction: column; align-items: flex-start; }
    .impact-left { border-right: none; border-bottom: 2px solid #e3f2e8; padding-right: 0; padding-bottom: 1rem; width: 100%; justify-content: center; }
    .impact-items { flex-direction: column; width: 100%; gap: 1.25rem; }
}
@media (max-width: 600px) {
    .solution-grid-4 { grid-template-columns: 1fr; }
    .impact-conclusion-bar { font-size: 0.9rem; text-align: center; flex-direction: column; }
}"""
    
    indented_css = "\n".join([(indent + line if line.strip() else indent) for line in new_css.split("\n")])
    
    new_content = content.replace(original_block, indented_css)
    
    # Also let's reduce the section padding.
    # We can do this by finding <div class="section section-alt"> and the style="text-align: center;" 
    # and the <div style="margin-bottom: 2.5rem;"> 
    # Let's replace margin-bottom: 3rem; and 2.5rem; with 1.5rem;
    
    new_content = re.sub(r'<div style="margin-bottom: 2\.5rem;">', '<div style="margin-bottom: 1.5rem;">', new_content)
    new_content = re.sub(r'<div style="margin-bottom: 2rem;">', '<div style="margin-bottom: 1rem;">', new_content)
    new_content = re.sub(r'<div style="text-align: center; margin-bottom: 2rem;">', '<div style="text-align: center; margin-bottom: 1rem;">', new_content)
    new_content = re.sub(r'<div class="steps" style="justify-content: center; margin: 3rem 0;">', '<div class="steps" style="justify-content: center; margin: 2rem 0 1.5rem;">', new_content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Updated {file}")

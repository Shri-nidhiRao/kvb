import os
import re

target_files = [
    "solar-steam-cooking.html",
    "direct-cooking.html",
    "solar-dryers.html",
    "scheffler-concentrators.html",
    "microgreen-systems.html",
    "thermal-storage.html"
]

base_dir = r"d:\kvb-green-energies-website\public\products"

def process_file(file_name):
    filepath = os.path.join(base_dir, file_name)
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Hero Split CSS
    # Add display flex column for all container and center text
    css_hero_pattern = r'(\.hero-split-container\s*\{\s*display:\s*flex;\s*align-items:\s*center;\s*)(justify-content:\s*space-between;)'
    content = re.sub(css_hero_pattern, r'\1justify-content: center; flex-direction: column; text-align: center;', content)
    
    css_hero_text_pattern = r'(\.hero-split-text\s*\{\s*flex:\s*1;\s*)(text-align:\s*left;)'
    content = re.sub(css_hero_text_pattern, r'\1text-align: center;', content)

    css_hero_h1_pattern = r'(\.hero-split-text\s*h1\s*\{\s*)(text-align:\s*left;)'
    content = re.sub(css_hero_h1_pattern, r'\1text-align: center;', content)

    css_hero_tags_pattern = r'(<div class="hero-tags" style="display: flex; gap: 1rem; margin-top: 1.5rem;)((">)'
    content = re.sub(css_hero_tags_pattern, r'\1 justify-content: center;\2', content)

    # 2. Extract hero image and remove from hero section
    hero_image_pattern = r'<div class="hero-split-image[^>]*>.*?<img src="([^"]+)"[^>]*>.*?</div>'
    match = re.search(hero_image_pattern, content, re.DOTALL)
    
    hero_img_src = ""
    if match:
        hero_img_src = match.group(1)
        # Remove the hero image block
        content = content.replace(match.group(0), '')
    
    # 3. Find and extract "System in Action" section
    # Some have <div class="reveal system-action-section"> or just <div class="reveal">...<h2>System in Action</h2>
    # We will search for a div containing <h2>System in Action</h2> and extracting it
    # We will then insert it right after <main class="container">

    # A robust way to extract the entire block containing System in Action:
    # First, find the starting index of '<h2>System in Action</h2>'
    h2_idx = content.find('<h2>System in Action</h2>')
    if h2_idx != -1:
        # Find the parent div starting tag before this h2
        div_start_idx = content.rfind('<div class="reveal', 0, h2_idx)
        if div_start_idx == -1:
            div_start_idx = content.rfind('<div class="system-action-section', 0, h2_idx)
            
        if div_start_idx != -1:
            # Find the matching closing div
            # Simple balancing algorithm
            div_count = 0
            idx = div_start_idx
            while idx < len(content):
                if content.startswith('<div', idx):
                    div_count += 1
                    idx += 4
                elif content.startswith('</div', idx):
                    div_count -= 1
                    idx += 5
                    if div_count == 0:
                        break
                else:
                    idx += 1
            
            div_end_idx = idx + 1 # include the > 
            # ensure we got the full closing tag
            close_tag_end = content.find('>', idx)
            if close_tag_end != -1:
                div_end_idx = close_tag_end + 1

            system_action_block = content[div_start_idx:div_end_idx]
            
            # Remove this block from original place
            content = content[:div_start_idx] + content[div_end_idx:]

            # Add Carousel Structure to this block
            # Replace gallery-grid with carousel-container
            system_action_block = system_action_block.replace('class="gallery-grid"', 'class="carousel-container"')
            
            # Prepend hero image to the items
            if hero_img_src:
                new_item = f"""
                <div class="gallery-item">
                    <img src="{hero_img_src}" alt="Hero Image">
                    <div class="gallery-caption"></div>
                </div>"""
                # Insert right after <div class="carousel-container">
                cc_idx = system_action_block.find('class="carousel-container"')
                if cc_idx != -1:
                    bracket_idx = system_action_block.find('>', cc_idx)
                    system_action_block = system_action_block[:bracket_idx+1] + new_item + system_action_block[bracket_idx+1:]
            
            # Add carousel CSS
            carousel_css = """
        /* ===== CAROUSEL STYLES ===== */
        .carousel-container {
            display: flex;
            overflow-x: auto;
            scroll-snap-type: x mandatory;
            gap: 1.5rem;
            padding-bottom: 1rem;
            scroll-behavior: smooth;
        }
        .carousel-container::-webkit-scrollbar {
            height: 10px;
        }
        .carousel-container::-webkit-scrollbar-track {
            background: var(--border-light);
            border-radius: 5px;
        }
        .carousel-container::-webkit-scrollbar-thumb {
            background: var(--primary);
            border-radius: 5px;
        }
        .carousel-container .gallery-item {
            flex: 0 0 85%;
            scroll-snap-align: center;
        }
        @media (min-width: 768px) {
            .carousel-container .gallery-item {
                flex: 0 0 60%;
            }
        }
        @media (min-width: 1024px) {
            .carousel-container .gallery-item {
                flex: 0 0 45%;
            }
        }
"""
            # Inject CSS right before </style>
            content = content.replace('</style>', carousel_css + '</style>')

            # Insert system_action_block right after <main class="container">
            main_idx = content.find('<main class="container">')
            if main_idx != -1:
                bracket_idx = content.find('>', main_idx)
                content = content[:bracket_idx+1] + '\n\n        <!-- Moved System in Action -->\n        ' + system_action_block + content[bracket_idx+1:]
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Processed {file_name}")

for f in target_files:
    process_file(f)

print("Done")

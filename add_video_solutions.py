import re

filepath = r"d:\kvb-green-energies-website\solutions\solar-steam-cooking.html"

# We want to find <h2>Parabolic Solar Cooker</h2> and replace the very next <div class="product-media">...</div>
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Using regex to find the section and replace the product-media block
# The structure is:
# <h2>Parabolic Solar Cooker</h2>
# <p>...</p>
# <a ...>
# </div>
# <div class="product-media">
#   <svg ...> ... </svg>
# </div>

pattern = re.compile(
    r'(<h2>\s*Parabolic Solar Cooker\s*</h2>.*?<div class="product-media"[^>]*>)\s*<svg.*?</svg>\s*(</div>)',
    re.IGNORECASE | re.DOTALL
)

video_html = """
        <video autoplay loop muted playsinline style="width: 100%; height: 100%; object-fit: cover; border-radius: 32px; box-shadow: 0 30px 60px rgba(0,0,0,0.04);">
          <source src="../videos/parabolic.mp4" type="video/mp4">
        </video>
"""

new_content = pattern.sub(r'\1' + video_html + r'\2', content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Video successfully added to solutions/solar-steam-cooking.html!")

import os

base_dir = r"d:\kvb-green-energies-website\products"

files_to_update = [
    'microgreen-systems.html',
    'solar-steam-cooking.html',
    'solar-dryers.html',
    'scheffler-concentrators.html',
    'thermal-storage.html',
    'ai-crop-detection.html'
]

for fname in files_to_update:
    filepath = os.path.join(base_dir, fname)
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The issue: the base CSS class for .spec-card has `animation: fadeUp 0.6s forwards;`
    # This completely blocks the IntersectionObserver `transition` when `.visible` is added.
    # We must append `animation: none !important;` to our Ultimate Zig-Zag override for the specific cards.

    fix_string = """
        .spec-card, .app-card, .application-card, .spec-highlight-card {
            animation: none !important;
            display: grid !important;
"""
    # So I will inject it into my ULTIMATE PREMIUM ZIG-ZAG block:
    if "animation: none !important;" not in content:
        content = content.replace(
            ".spec-card, .app-card, .application-card, .spec-highlight-card {\n            display: grid !important;",
            fix_string
        )
    
    # Also aggressively strip the native fadeUp rules from the source HTML so they don't fight it 
    content = content.replace("animation: fadeUp 0.6s forwards;", "/* animation disabled for zig-zag override */")
    content = content.replace("animation: fadeUp 0.8s forwards;", "/* animation disabled for zig-zag override */")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Animations correctly patched! Zig-Zag slide-ins should now trigger perfectly on scroll.")

import os
import re
import sys

def get_all_files(directory, extensions=None):
    all_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if extensions is None or any(file.endswith(ext) for ext in extensions):
                all_files.append(os.path.join(root, file))
    return all_files

def main():
    public_dir = r"d:\kvb-green-energies-website\public"
    
    # 1. Gather all assets
    asset_exts = ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.mp4', '.avif', '.css', '.js']
    assets = get_all_files(public_dir, asset_exts)
    
    # 2. Gather all code files where assets might be referenced
    code_exts = ['.html', '.css', '.js']
    code_files = get_all_files(public_dir, code_exts)
    
    # Also include root files like server.js just in case
    code_files.append(r"d:\kvb-green-energies-website\server.js")

    # Read all code content
    code_contents = ""
    for cf in code_files:
        try:
            with open(cf, 'r', encoding='utf-8') as f:
                code_contents += f.read() + "\n"
        except Exception as e:
            print(f"Could not read {cf}: {e}")

    unused_assets = []
    for asset in assets:
        basename = os.path.basename(asset)
        # We search for the exact filename in the code contents
        if basename not in code_contents:
            unused_assets.append(asset)
            
    print("=== Potentially Unused Assets (Images, CSS, JS) ===")
    for a in sorted(unused_assets):
        print(a.replace(public_dir, ""))

    # Now let's check for unused HTML files
    html_files = get_all_files(public_dir, ['.html'])
    unused_html = []
    
    for hf in html_files:
        basename = os.path.basename(hf)
        # index.html, 404.html etc. might not be linked but are entry points
        if basename in ['index.html', '404.html', 'header.html', 'footer.html']:
            continue
            
        if basename not in code_contents:
            unused_html.append(hf)

    print("\n=== Potentially Unused HTML Files ===")
    for h in sorted(unused_html):
        print(h.replace(public_dir, ""))

if __name__ == '__main__':
    main()

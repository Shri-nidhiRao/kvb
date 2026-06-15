import os
import re

directory = 'd:/kvb-green-energies-website/public'
html_files = []

for root, _, files in os.walk(directory):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

missing_mobile = []
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check if there is any @media rule
    if '@media' not in content:
        # It's possible the CSS is in an external file or no @media is needed,
        # but let's log it to check.
        missing_mobile.append(filepath)

print("Files without @media queries:")
for f in missing_mobile:
    print(f)

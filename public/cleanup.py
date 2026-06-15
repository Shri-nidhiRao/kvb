import os

directory = 'd:/kvb-green-energies-website/public'
html_files = []

for root, _, files in os.walk(directory):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        cleaned_lines = [line.rstrip() + '\n' for line in lines]
        
        if lines != cleaned_lines:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.writelines(cleaned_lines)
            print(f"Cleaned trailing spaces in {filepath}")
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

print("Code cleanup complete.")

import re

dryer_path = r"d:\kvb-green-energies-website\products\solar-dryers.html"
scheffler_path = r"d:\kvb-green-energies-website\products\scheffler-concentrators.html"

with open(dryer_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Extract the premium block from solar-dryers.html
match = re.search(r'(<div class="container premium-wrapper">.*?)<div id="footer"></div>', text, re.DOTALL)
if match:
    premium_block = match.group(1)
    
    with open(scheffler_path, 'r', encoding='utf-8') as f2:
        s_text = f2.read()
        
    if "premium-wrapper" not in s_text:
        # inject it right before <div id="footer"></div>
        s_text = s_text.replace('<div id="footer"></div>', premium_block + '    <div id="footer"></div>\n')
        
    # Add a safety check around the addEventListener to prevent future bugs if unlockForm is null
    s_text = s_text.replace("unlockForm.addEventListener('submit'", "if(unlockForm) unlockForm.addEventListener('submit'")
    
    # Also add main.js if it somehow got deleted
    if "main.js" not in s_text:
        s_text = s_text.replace("</body>", "    <!-- Custom JS -->\n    <script src=\"../assets/js/main.js\"></script>\n</body>")
        
    with open(scheffler_path, 'w', encoding='utf-8') as f3:
        f3.write(s_text)
        
    print("Successfully patched scheffler-concentrators.html!")
else:
    print("Could not find premium block in solar-dryers.html")

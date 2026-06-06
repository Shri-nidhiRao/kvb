import os
import re

html_dir = r"d:\kvb-green-energies-website\public\app"

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

page_content = {
    "automobile-industry.html": {
        "title": "What This System Does:",
        "subtitle_target": "KVB Green Energies offers Parabolic Trough Solar Thermal Systems (PTC) designed specifically for industrial thermal requirements.",
        "subtitle_replacement": "KVB Green Energies offers <span style=\"color: #2c6e49; font-weight: 600;\">Parabolic Trough Solar Thermal Systems (PTC)</span><br>designed specifically for industrial thermal requirements.",
        "cards": [
            ("fa-temperature-high", "Generates high-temp<br>water/steam", "using solar energy"),
            ("fa-car", "Supports degreasing,<br>washing, and", "paint baking processes"),
            ("fa-plug", "Integrates with<br>existing boiler", "systems"),
            ("fa-sync-alt", "Ensures uninterrupted<br>production", "with hybrid operation")
        ],
        "impact": [
            ("fa-arrow-down", "Up to 40%", "reduction in<br>fuel consumption"),
            ("fa-rupee-sign", "Lower cost", "of production"),
            ("fa-shield-alt", "Long-term", "energy price stability")
        ],
        "conclusion": "This is not just energy saving — it is <span class=\"highlight-yellow\">margin improvement</span> for your factory."
    },
    "chemical-industry.html": {
        "title": "What This System Does:",
        "subtitle_target": "KVB Green Energies offers Parabolic Trough Solar Thermal Systems (PTC) designed specifically for heavy-duty chemical processing.",
        "subtitle_replacement": "KVB Green Energies offers <span style=\"color: #2c6e49; font-weight: 600;\">Parabolic Trough Solar Thermal Systems (PTC)</span><br>designed specifically for heavy-duty chemical processing.",
        "cards": [
            ("fa-temperature-high", "Generates high-temp<br>steam/heat", "using solar energy"),
            ("fa-flask", "Supports reactor heating,<br>distillation, and", "evaporation"),
            ("fa-plug", "Integrates seamlessly<br>with existing", "thermal systems"),
            ("fa-sync-alt", "Operates in<br>hybrid mode", "for continuous heat supply")
        ],
        "impact": [
            ("fa-arrow-down", "Up to 40%", "reduction in<br>fuel consumption"),
            ("fa-rupee-sign", "Lower cost", "of production"),
            ("fa-shield-alt", "Long-term", "energy price stability")
        ],
        "conclusion": "This is not just energy saving — it is <span class=\"highlight-yellow\">margin improvement</span> for your factory."
    },
    "dairy-industry.html": {
        "title": "What This System Does:",
        "subtitle_target": "KVB Green Energies offers Parabolic Trough Solar Thermal Systems (PTC) designed specifically for dairy operations.",
        "subtitle_replacement": "KVB Green Energies offers <span style=\"color: #2c6e49; font-weight: 600;\">Parabolic Trough Solar Thermal Systems (PTC)</span><br>designed specifically for dairy operations.",
        "cards": [
            ("fa-temperature-high", "Generates steam<br>and hot water", "using solar energy"),
            ("fa-glass-whiskey", "Supports pasteurization,<br>sterilization, and", "CIP cleaning"),
            ("fa-plug", "Integrates seamlessly<br>with existing", "boiler systems"),
            ("fa-sync-alt", "Operates in<br>hybrid mode", "for continuous thermal supply")
        ],
        "impact": [
            ("fa-arrow-down", "Up to 40%", "reduction in<br>fuel consumption"),
            ("fa-rupee-sign", "Lower cost", "of production"),
            ("fa-shield-alt", "Long-term", "energy price stability")
        ],
        "conclusion": "This is not just energy saving — it is <span class=\"highlight-yellow\">margin improvement</span> for your factory."
    },
    "food-processing-industry.html": {
        "title": "What This System Does:",
        "subtitle_target": "KVB Green Energies provides Parabolic Trough Solar Thermal Systems (PTC) engineered for food processing applications.",
        "subtitle_replacement": "KVB Green Energies provides <span style=\"color: #2c6e49; font-weight: 600;\">Parabolic Trough Solar Thermal Systems (PTC)</span><br>engineered for food processing applications.",
        "cards": [
            ("fa-temperature-high", "Generates steam<br>and high-temp heat", "using solar energy"),
            ("fa-hand-holding-heart", "Supports cooking,<br>drying, and", "sterilization processes"),
            ("fa-plug", "Integrates with<br>existing boiler", "systems"),
            ("fa-sync-alt", "Ensures uninterrupted<br>production", "with hybrid operation")
        ],
        "impact": [
            ("fa-arrow-down", "Up to 40%", "reduction in<br>fuel consumption"),
            ("fa-rupee-sign", "Lower cost", "of production"),
            ("fa-shield-alt", "Long-term", "energy price stability")
        ],
        "conclusion": "This is not just energy saving — it is <span class=\"highlight-yellow\">margin improvement</span> for your factory."
    },
    "leather-footwear.html": {
        "title": "What This System Does:",
        "subtitle_target": "KVB Green Energies offers Parabolic Trough Solar Thermal Systems (PTC) designed specifically for industrial requirements in leather and footwear plants.",
        "subtitle_replacement": "KVB Green Energies offers <span style=\"color: #2c6e49; font-weight: 600;\">Parabolic Trough Solar Thermal Systems (PTC)</span><br>designed specifically for industrial requirements in leather and footwear plants.",
        "cards": [
            ("fa-temperature-high", "Generates high-temp<br>heat", "using solar energy"),
            ("fa-hand-holding-heart", "Supports tanning,<br>drying, and", "finishing processes"),
            ("fa-plug", "Integrates with<br>existing boiler", "systems"),
            ("fa-sync-alt", "Ensures uninterrupted<br>production", "with hybrid operation")
        ],
        "impact": [
            ("fa-arrow-down", "Up to 40%", "reduction in<br>fuel consumption"),
            ("fa-rupee-sign", "Lower cost", "of production"),
            ("fa-shield-alt", "Long-term", "energy price stability")
        ],
        "conclusion": "This is not just energy saving — it is <span class=\"highlight-yellow\">margin improvement</span> for your factory."
    },
    "paper-pulp-industry.html": {
        "title": "What This System Does:",
        "subtitle_target": "KVB Green Energies offers Parabolic Trough Solar Thermal Systems (PTC) engineered for high-demand paper and pulp operations.",
        "subtitle_replacement": "KVB Green Energies offers <span style=\"color: #2c6e49; font-weight: 600;\">Parabolic Trough Solar Thermal Systems (PTC)</span><br>engineered for high-demand paper and pulp operations.",
        "cards": [
            ("fa-temperature-high", "Generates high-temp<br>steam", "using solar energy"),
            ("fa-chart-line", "Reduces boiler fuel<br>consumption", "significantly"),
            ("fa-plug", "Integrates seamlessly<br>with existing", "steam systems"),
            ("fa-sync-alt", "Operates in<br>hybrid mode", "for uninterrupted production")
        ],
        "impact": [
            ("fa-arrow-down", "Up to 40%", "reduction in<br>fuel consumption"),
            ("fa-rupee-sign", "Lower cost", "per ton of paper produced"),
            ("fa-shield-alt", "Stable long-term", "energy pricing")
        ],
        "conclusion": "This is not just energy saving — this is <span class=\"highlight-yellow\">large-scale cost optimization</span>."
    },
    "tea-processing-industry.html": {
        "title": "What This System Does:",
        "subtitle_target": "KVB Green Energies offers Parabolic Trough Solar Thermal Systems (PTC)\n            designed specifically for tea processing requirements.",
        "subtitle_replacement": "KVB Green Energies offers <span style=\"color: #2c6e49; font-weight: 600;\">Parabolic Trough Solar Thermal Systems (PTC)</span><br>designed specifically for tea processing requirements.",
        "cards": [
            ("fa-temperature-high", "Generates steam<br>and hot air", "using solar energy"),
            ("fa-leaf", "Supports withering,<br>fixation, and drying", "processes"),
            ("fa-plug", "Integrates with<br>existing boiler", "systems"),
            ("fa-sync-alt", "Ensures uninterrupted<br>operation", "with hybrid control")
        ],
        "impact": [
            ("fa-arrow-down", "Up to 40%", "reduction in<br>fuel consumption"),
            ("fa-rupee-sign", "Lower processing", "cost per kg of tea"),
            ("fa-shield-alt", "Stable energy cost", "for long-term operations")
        ],
        "conclusion": "This is not just energy saving — this is <span class=\"highlight-yellow\">cost optimization</span> for your factory."
    },
    "textile-industry.html": {
        "title": "What we deliver",
        "subtitle_target": "High-temperature solar steam that integrates\n                        directly with your existing boiler room.",
        "subtitle_replacement": "<span style=\"color: #2c6e49; font-weight: 600;\">High-temperature solar steam</span> that integrates<br>directly with your existing boiler room.",
        "cards": [
            ("fa-check-circle", "Direct steam generation", "for dyeing & finishing"),
            ("fa-tachometer-alt", "Boiler feedwater<br>preheating", "→ boost efficiency"),
            ("fa-sync-alt", "Hybrid solar + boiler", "(no production stops)"),
            ("fa-database", "Optional thermal storage", "for extended operation")
        ],
        "impact": [
            ("fa-arrow-down", "Up to 40%", "reduction in<br>fuel consumption"),
            ("fa-cogs", "No disruption", "to process lines"),
            ("fa-shield-alt", "Stable energy cost", "for long-term operations")
        ],
        "conclusion": "This is not just energy saving — this is <span class=\"highlight-yellow\">margin improvement</span> for your factory."
    }
}

new_css = """        /* ===== Premium Smart Solution Redesign ===== */
        .smart-solution-redesign { max-width: 1100px; margin: 0 auto; text-align: center; font-family: 'Inter', sans-serif; }
        
        .section-divider { display: flex; align-items: center; justify-content: center; margin: 3rem 0 2rem; gap: 15px; }
        .divider-line { height: 1px; background: #2c6e49; flex-grow: 1; max-width: 150px; position: relative; }
        .divider-line::before { content: ''; position: absolute; width: 6px; height: 6px; background: #2c6e49; border-radius: 50%; top: -2.5px; }
        .divider-line.left::before { right: 0; }
        .divider-line.right::before { left: 0; }
        .divider-text { font-size: 1.4rem; color: #114227; font-weight: 700; margin: 0; }

        .solution-grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.5rem; margin-bottom: 3rem; }
        .solution-card { background: #ffffff; border: 1px solid #eaeaea; border-radius: 12px; padding: 2rem 1.5rem; display: flex; flex-direction: column; align-items: center; box-shadow: 0 4px 15px rgba(0,0,0,0.03); position: relative; overflow: hidden; transition: transform 0.3s ease; }
        .solution-card:hover { transform: translateY(-5px); box-shadow: 0 10px 25px rgba(0,0,0,0.06); }
        .solution-card::after { content: ''; position: absolute; bottom: 0; left: 0; width: 100%; height: 6px; }
        .card-green::after { background: #1f8a70; }
        .card-light-green::after { background: #9dcd5a; }
        .card-yellow::after { background: #fbc02d; }
        .card-blue::after { background: #1565c0; }

        .card-icon-circle { width: 64px; height: 64px; background: #eef7f0; color: #2c6e49; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.8rem; margin-bottom: 1.5rem; }
        .card-text { font-size: 0.95rem; color: #515154; line-height: 1.5; }
        .card-text strong { color: #1d1d1f; display: block; margin-bottom: 5px; font-size: 1.05rem; }

        .impact-box { background: #f6fcf8; border: 1px solid #e3f2e8; border-radius: 12px; padding: 1.5rem; display: flex; align-items: center; gap: 2rem; margin-bottom: 1.5rem; flex-wrap: wrap; }
        .impact-left { display: flex; align-items: center; gap: 15px; border-right: 2px solid #e3f2e8; padding-right: 2rem; }
        .impact-main-icon { font-size: 3rem; color: #2c6e49; }
        .impact-title { font-size: 1.2rem; font-weight: 700; color: #114227; line-height: 1.3; }
        
        .impact-items { display: flex; gap: 2rem; flex-grow: 1; justify-content: space-around; }
        .impact-item { display: flex; align-items: center; gap: 15px; text-align: left; }
        .impact-icon { width: 42px; height: 42px; background: #2c6e49; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.1rem; flex-shrink: 0; }
        .impact-item-text { font-size: 0.9rem; color: #1d1d1f; line-height: 1.4; }
        .impact-item-text strong { display: block; font-size: 1rem; }

        .impact-conclusion-bar { background: #0f4b2b; color: white; border-radius: 8px; padding: 1rem 2rem; display: flex; align-items: center; justify-content: center; gap: 10px; font-size: 1.1rem; font-weight: 500; }
        .impact-conclusion-bar .fa-check-circle { color: #ffffff; font-size: 1.3rem; }
        .highlight-yellow { color: #ffca28; }

        @media (max-width: 1024px) {
            .solution-grid-4 { grid-template-columns: repeat(2, 1fr); }
            .impact-box { flex-direction: column; align-items: flex-start; }
            .impact-left { border-right: none; border-bottom: 2px solid #e3f2e8; padding-right: 0; padding-bottom: 1rem; width: 100%; justify-content: center; }
            .impact-items { flex-direction: column; width: 100%; gap: 1.5rem; }
        }
        @media (max-width: 600px) {
            .solution-grid-4 { grid-template-columns: 1fr; }
            .impact-conclusion-bar { font-size: 0.95rem; text-align: center; flex-direction: column; }
        }"""

html_template = """<div class="smart-solution-redesign">
          <div class="section-divider">
              <span class="divider-line left"></span>
              <h3 class="divider-text">{title}</h3>
              <span class="divider-line right"></span>
          </div>

          <div class="solution-grid-4">
              <div class="solution-card card-green">
                  <div class="card-icon-circle"><i class="fas {c1_icon}"></i></div>
                  <div class="card-text">
                      <strong>{c1_b}</strong>
                      <span>{c1_s}</span>
                  </div>
              </div>
              <div class="solution-card card-light-green">
                  <div class="card-icon-circle"><i class="fas {c2_icon}"></i></div>
                  <div class="card-text">
                      <strong>{c2_b}</strong>
                      <span>{c2_s}</span>
                  </div>
              </div>
              <div class="solution-card card-yellow">
                  <div class="card-icon-circle"><i class="fas {c3_icon}"></i></div>
                  <div class="card-text">
                      <strong>{c3_b}</strong>
                      <span>{c3_s}</span>
                  </div>
              </div>
              <div class="solution-card card-blue">
                  <div class="card-icon-circle"><i class="fas {c4_icon}"></i></div>
                  <div class="card-text">
                      <strong>{c4_b}</strong>
                      <span>{c4_s}</span>
                  </div>
              </div>
          </div>

          <div class="impact-box">
              <div class="impact-left">
                  <i class="fas fa-chart-line impact-main-icon"></i>
                  <span class="impact-title">Immediate<br>Impact:</span>
              </div>
              
              <div class="impact-items">
                  <div class="impact-item">
                      <div class="impact-icon"><i class="fas {i1_icon}"></i></div>
                      <div class="impact-item-text"><strong>{i1_b}</strong>{i1_s}</div>
                  </div>
                  <div class="impact-item">
                      <div class="impact-icon"><i class="fas {i2_icon}"></i></div>
                      <div class="impact-item-text"><strong>{i2_b}</strong>{i2_s}</div>
                  </div>
                  <div class="impact-item">
                      <div class="impact-icon"><i class="fas {i3_icon}"></i></div>
                      <div class="impact-item-text"><strong>{i3_b}</strong>{i3_s}</div>
                  </div>
              </div>
          </div>

          <div class="impact-conclusion-bar">
              <i class="fas fa-check-circle"></i> 
              <span>{conclusion}</span>
          </div>
        </div>"""

for fname in files:
    path = os.path.join(html_dir, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Replace the CSS block
    css_regex = re.compile(r'/\* ===== Smart Solution Redesign ===== \*/.*?} \}', re.DOTALL)
    content = css_regex.sub(new_css, content)
    
    # 2. Replace the HTML block
    html_regex = re.compile(r'<div class="smart-solution-redesign">.*?</div>\s*</div>\s*</div>', re.DOTALL)
    # wait, the closing tags were:
    # </div> <!-- impact conclusion -->
    # </div> <!-- smart solution -->
    
    # let's be more precise:
    html_regex2 = re.compile(r'<div class="smart-solution-redesign">.*?<div class="impact-conclusion">.*?</div>\s*</div>', re.DOTALL)
    
    data = page_content[fname]
    new_html = html_template.format(
        title=data["title"],
        c1_icon=data["cards"][0][0], c1_b=data["cards"][0][1], c1_s=data["cards"][0][2],
        c2_icon=data["cards"][1][0], c2_b=data["cards"][1][1], c2_s=data["cards"][1][2],
        c3_icon=data["cards"][2][0], c3_b=data["cards"][2][1], c3_s=data["cards"][2][2],
        c4_icon=data["cards"][3][0], c4_b=data["cards"][3][1], c4_s=data["cards"][3][2],
        i1_icon=data["impact"][0][0], i1_b=data["impact"][0][1], i1_s=data["impact"][0][2],
        i2_icon=data["impact"][1][0], i2_b=data["impact"][1][1], i2_s=data["impact"][1][2],
        i3_icon=data["impact"][2][0], i3_b=data["impact"][2][1], i3_s=data["impact"][2][2],
        conclusion=data["conclusion"]
    )
    
    content = html_regex2.sub(new_html, content)
    
    # 3. Replace the subtitle
    # Need to normalize spaces for subtitle target matching
    sub_target = data["subtitle_target"]
    sub_replace = data["subtitle_replacement"]
    # We will use string replace if it matches exactly, else regex with space collapsing
    if sub_target in content:
        content = content.replace(sub_target, sub_replace)
    else:
        # try regex with variable whitespace
        regex_target = r'\s+'.join(map(re.escape, sub_target.split()))
        content = re.sub(regex_target, sub_replace, content)
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done updating files!")

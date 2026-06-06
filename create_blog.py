import os

template = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blogs | KVB Green Energies</title>
    <link rel="icon" type="image/png" href="images/products/kvb-logo.png">
    
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <!-- Google Fonts: Montserrat + Inter -->
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    
    <style>
        /* ===== BASE STYLES – KVB Theme ===== */
        :root {
            --solar-yellow: #FDB813;
            --deep-blue: #0B3D91;
            --eco-green: #3A7D44;
            --dark-charcoal: #1C1C1C;
            --soft-white: #F9F9F9;
            --accent-orange: #FF6F00;
            --background: #F9F9F9;
            --background-alt: #FFFFFF;
            --text-primary: #1C1C1C;
            --text-secondary: #4a5568;
            --text-tertiary: #A1A1A6;
            --border: #e0e8e0;
            --primary: #3A7D44;
            --primary-dark: #2d5a33;
            --primary-light: #e6f3e6;
            --primary-glow: rgba(58, 125, 68, 0.15);
            --shadow-sm: 0 10px 30px rgba(28,28,28,0.04);
            --shadow-md: 0 20px 40px rgba(58,125,68,0.08);
            --shadow-lg: 0 16px 40px rgba(0,0,0,0.12);
            --radius-sm: 12px;
            --radius-md: 20px;
            --radius-lg: 28px;
            --font-heading: 'Montserrat', sans-serif;
            --font-body: 'Inter', sans-serif;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            font-family: var(--font-body);
            color: var(--text-primary);
            background: var(--background);
            line-height: 1.6;
            overflow-x: hidden;
            scroll-behavior: smooth;
        }

        .container { max-width: 1280px; margin: 0 auto; padding: 0 32px; }

        h1, h2, h3, h4 { font-family: var(--font-heading); font-weight: 700; letter-spacing: -0.02em; }

        .section-title {
            font-size: 2.5rem; font-weight: 700; font-family: 'Montserrat', sans-serif;
            color: var(--deep-blue); text-align: center; position: relative;
            display: block; margin-bottom: 26px;
        }

        .section-title::after {
            content: ''; position: absolute; bottom: -10px; left: 50%;
            transform: translateX(-50%); width: 80px; height: 4px;
            background: var(--solar-yellow); border-radius: 2px;
        }

        /* ===== HEADER PLACEHOLDER ===== */
        #header { min-height: 80px; }

        /* ===== HERO SECTION ===== */
        .blog-hero {
            position: relative; min-height: 50vh; display: flex; align-items: center;
            background: linear-gradient(135deg, #09203f 0%, #0f3460 40%, #1a5276 100%);
            overflow: hidden; color: white; padding: 100px 0 60px;
        }

        .blog-hero::before {
            content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            background: radial-gradient(circle at 15% 50%, rgba(0,255,135,0.12) 0%, transparent 55%),
                        radial-gradient(circle at 85% 30%, rgba(253,184,19,0.08) 0%, transparent 40%);
            animation: heroPulse 8s infinite alternate; z-index: 1;
        }

        .blog-hero::after {
            content: ''; position: absolute; bottom: -2px; left: 0; width: 100%; height: 80px;
            background: url("data:image/svg+xml,%3Csvg viewBox='0 0 1440 80' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill='%23F9F9F9' d='M0,40 C360,80 1080,0 1440,40 L1440,80 L0,80 Z'/%3E%3C/svg%3E") no-repeat bottom;
            background-size: cover; z-index: 2;
        }

        @keyframes heroPulse { 0% { opacity: 0.9; } 100% { opacity: 1; } }

        .hero-content {
            max-width: 800px; margin: 0 auto; position: relative; z-index: 3; text-align: center;
        }

        .hero-content h1 { color: white; font-size: 3.5rem; font-weight: 900; margin-bottom: 20px; animation: fadeUp 0.9s ease 0.1s both; }
        
        .hero-title-highlight {
            background: linear-gradient(135deg, #00e676, var(--solar-yellow));
            -webkit-background-clip: text; -webkit-text-fill-color: transparent; display: inline;
        }

        .hero-content .hero-subtitle {
            font-size: 1.2rem; color: rgba(255, 255, 255, 0.9); font-weight: 400; margin-bottom: 2rem; max-width: 680px; margin-inline: auto; animation: fadeUp 1s ease 0.2s both;
        }

        @keyframes fadeUp {
            from { opacity: 0; transform: translateY(25px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* ===== BLOG GRID ===== */
        .blogs-section { padding: 4rem 0 6rem; }

        .blogs-grid {
            display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem; margin-top: 3rem;
        }

        .blog-card {
            background: white; border-radius: var(--radius-md); overflow: hidden;
            box-shadow: var(--shadow-sm); border: 1px solid var(--border); transition: all 0.3s ease;
            display: flex; flex-direction: column; height: 100%;
        }

        .blog-card:hover {
            transform: translateY(-8px); box-shadow: var(--shadow-md); border-color: var(--primary);
        }

        .blog-img {
            width: 100%; height: 220px; object-fit: cover; background: var(--primary-light);
            display: flex; align-items: center; justify-content: center;
        }
        
        .blog-img i { font-size: 4rem; color: rgba(58, 125, 68, 0.3); }

        .blog-content { padding: 2rem; flex-grow: 1; display: flex; flex-direction: column; }

        .blog-meta {
            display: flex; align-items: center; gap: 15px; font-size: 0.85rem; color: var(--text-tertiary); margin-bottom: 1rem;
        }

        .blog-meta .tag {
            background: var(--primary-light); color: var(--primary-dark); padding: 4px 12px;
            border-radius: 20px; font-weight: 600; letter-spacing: 0.5px; text-transform: uppercase; font-size: 0.75rem;
        }

        .blog-card h3 {
            font-size: 1.4rem; color: var(--deep-blue); margin-bottom: 1rem; line-height: 1.4;
        }

        .blog-card p {
            color: var(--text-secondary); font-size: 0.95rem; margin-bottom: 1.5rem; flex-grow: 1;
        }

        .blog-read-more {
            display: inline-flex; align-items: center; gap: 8px; font-weight: 600; color: var(--primary);
            text-decoration: none; transition: gap 0.3s; margin-top: auto;
        }

        .blog-read-more:hover { gap: 12px; color: var(--primary-dark); }

        @media (max-width: 768px) {
            .hero-content h1 { font-size: 2.5rem; }
            .blogs-grid { grid-template-columns: 1fr; }
        }
    </style>
</head>

<body>
    <!-- Header injected via script -->
    <div id="header"></div>

    <!-- HERO SECTION -->
    <section class="blog-hero">
        <div class="container">
            <div class="hero-content">
                <h1>Insights & <span class="hero-title-highlight">Innovations</span></h1>
                <p class="hero-subtitle">Explore the latest news, technological breakthroughs, and insights in the world of renewable energy and smart agriculture.</p>
            </div>
        </div>
    </section>

    <!-- BLOGS CONTENT -->
    <section class="blogs-section">
        <div class="container">
            <h2 class="section-title">Latest Articles</h2>
            
            <div class="blogs-grid">
                <!-- Blog Card 1 -->
                <div class="blog-card">
                    <div class="blog-img">
                        <i class="fas fa-solar-panel"></i>
                    </div>
                    <div class="blog-content">
                        <div class="blog-meta">
                            <span class="tag">Solar Energy</span>
                            <span>May 15, 2026</span>
                        </div>
                        <h3>The Future of Parabolic Trough Solar Collectors</h3>
                        <p>How next-generation parabolic trough technology is making industrial process heating more efficient and affordable than ever.</p>
                        <a href="#" class="blog-read-more">Read Article <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>

                <!-- Blog Card 2 -->
                <div class="blog-card">
                    <div class="blog-img">
                        <i class="fas fa-leaf"></i>
                    </div>
                    <div class="blog-content">
                        <div class="blog-meta">
                            <span class="tag">Agriculture</span>
                            <span>April 28, 2026</span>
                        </div>
                        <h3>Revolutionizing Yields with Automated Microgreen Systems</h3>
                        <p>Discover how climate-controlled automated racks are helping farmers maximize their yield per square foot with zero pesticide use.</p>
                        <a href="#" class="blog-read-more">Read Article <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>

                <!-- Blog Card 3 -->
                <div class="blog-card">
                    <div class="blog-img">
                        <i class="fas fa-industry"></i>
                    </div>
                    <div class="blog-content">
                        <div class="blog-meta">
                            <span class="tag">Industrial</span>
                            <span>April 10, 2026</span>
                        </div>
                        <h3>Decarbonizing the Tea Processing Industry</h3>
                        <p>A deep dive into how large-scale solar drying and thermal storage solutions are slashing carbon footprints in traditional tea estates.</p>
                        <a href="#" class="blog-read-more">Read Article <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer injected via script -->
    <div id="footer"></div>

    <!-- Base component injection scripts -->
    <script>
        // Inject Header and Footer
        fetch('components/header.html')
            .then(response => response.text())
            .then(data => {
                document.getElementById('header').innerHTML = data;
                
                // Re-initialize any header scripts
                var script = document.createElement("script");
                script.text = `
                    var menuBtn = document.getElementById('menuBtn');
                    var navMenu = document.getElementById('navMenu');
                    if (menuBtn && navMenu) {
                        menuBtn.addEventListener('click', function () {
                            navMenu.classList.toggle('active');
                            menuBtn.classList.toggle('active');
                        });
                    }
                    var dropdowns = document.querySelectorAll('.dropdown');
                    dropdowns.forEach(function (dd) {
                        dd.addEventListener('click', function (e) {
                            if (window.innerWidth <= 1024) {
                                e.preventDefault();
                                this.classList.toggle('active');
                            }
                        });
                    });
                `;
                document.body.appendChild(script);
            });

        fetch('components/footer.html')
            .then(response => response.text())
            .then(data => {
                document.getElementById('footer').innerHTML = data;
            });
    </script>
</body>
</html>
"""

with open("d:/kvb-green-energies-website/public/blog.html", "w", encoding="utf-8") as f:
    f.write(template)

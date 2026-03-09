import os
import re

nav_dropdown_css = '''
        /* Dropdown */
        .dropdown {
            position: relative;
            display: inline-block;
        }
        .dropdown-content {
            display: none;
            position: absolute;
            top: 100%;
            left: 50%;
            transform: translateX(-50%) translateY(10px);
            background-color: var(--surface);
            min-width: 200px;
            box-shadow: 0px 8px 24px 0px rgba(0,0,0,0.06);
            z-index: 101;
            border-radius: 4px;
            border: 1px solid var(--border);
            opacity: 0;
            transition: opacity 0.3s ease, transform 0.3s ease;
        }
        .dropdown:hover .dropdown-content {
            display: flex;
            flex-direction: column;
            opacity: 1;
            transform: translateX(-50%) translateY(0);
        }
        .dropdown-content a {
            color: var(--text) !important;
            padding: 12px 16px;
            text-decoration: none;
            display: block;
            font-size: 0.75rem;
            transition: background 0.2s, color 0.2s !important;
        }
        .dropdown-content a:hover {
            background-color: var(--card-bg) !important;
            color: var(--accent) !important;
        }
'''

new_nav_html = '''<ul class="nav-links">
            <li><a href="frontend.html">Home</a></li>
            <li class="dropdown">
                <a href="#products">Products ▾</a>
                <div class="dropdown-content">
                    <a href="seafood.html">Sea Food</a>
                    <a href="vegetables-turmeric.html">Vegetables & Turmeric</a>
                    <a href="textile.html">Textiles</a>
                </div>
            </li>
            <li><a href="#about">About Us</a></li>
            <li><a href="#story">Contact Us</a></li>
        </ul>'''

files = ['frontend.html', 'seafood.html', 'vegetables-turmeric.html', 'textile.html']

anim_css_map = {
    'seafood.html': '''        /* Water Splash Animation */
        .card-img-wrap, .feature-img {
            position: relative;
            overflow: hidden;
        }
        .splash-particle {
            position: absolute;
            border: 2px solid rgba(255, 255, 255, 0.8);
            border-radius: 50%;
            pointer-events: none;
            transform: translate(-50%, -50%) scale(0);
            opacity: 0;
            z-index: 20;
        }
        @keyframes splash {
            0% { transform: translate(-50%, -50%) scale(0); opacity: 0.8; border-width: 4px; }
            100% { transform: translate(-50%, -50%) scale(3); opacity: 0; border-width: 1px; }
        }''',
    'vegetables-turmeric.html': '''        /* Turmeric Burst */
        .card-img-wrap, .feature-img {
            position: relative;
            overflow: hidden;
        }
        .burst-particle {
            position: absolute;
            background: rgba(230, 160, 40, 0.7);
            filter: blur(4px);
            border-radius: 50%;
            pointer-events: none;
            transform: translate(-50%, -50%) scale(0);
            mix-blend-mode: multiply;
            z-index: 20;
        }
        @keyframes burst {
            0% { transform: translate(-50%, -50%) scale(0); opacity: 0.8; }
            100% { transform: translate(-50%, -50%) scale(10); opacity: 0; }
        }''',
    'textile.html': '''        /* Thread wave */
        .card-img-wrap, .feature-img {
            position: relative;
            overflow: hidden;
        }
        .thread-line {
            position: absolute;
            background: rgba(255, 255, 255, 0.8);
            pointer-events: none;
            z-index: 20;
        }
        .thread-h { height: 1.5px; width: 0; }
        .thread-v { width: 1.5px; height: 0; }
        
        @keyframes threadShootH {
            0% { width: 0; opacity: 1; left: 0; }
            50% { width: 100%; opacity: 1; left: 0; }
            100% { width: 0; opacity: 0; left: 100%; }
        }
        @keyframes threadShootV {
            0% { height: 0; opacity: 1; top: 0; }
            50% { height: 100%; opacity: 1; top: 0; }
            100% { height: 0; opacity: 0; top: 100%; }
        }'''
}

anim_js_map = {
    'seafood.html': '''        // Splash animation on image hover
        document.querySelectorAll('.card-img-wrap, .feature-img').forEach(el => {
            el.addEventListener('mouseenter', (e) => {
                const rect = el.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                
                const splash = document.createElement('div');
                splash.classList.add('splash-particle');
                splash.style.left = x + 'px';
                splash.style.top = y + 'px';
                splash.style.width = '60px';
                splash.style.height = '60px';
                splash.style.animation = 'splash 0.6s ease-out forwards';
                
                el.appendChild(splash);
                setTimeout(() => splash.remove(), 600);
            });
        });''',
    'vegetables-turmeric.html': '''        // Turmeric burst on image hover
        document.querySelectorAll('.card-img-wrap, .feature-img').forEach(el => {
            el.addEventListener('mouseenter', (e) => {
                const rect = el.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                
                const burst = document.createElement('div');
                burst.classList.add('burst-particle');
                burst.style.left = x + 'px';
                burst.style.top = y + 'px';
                burst.style.width = '40px';
                burst.style.height = '40px';
                burst.style.animation = 'burst 0.7s cubic-bezier(0.1, 0.9, 0.2, 1) forwards';
                
                el.appendChild(burst);
                setTimeout(() => burst.remove(), 700);
            });
        });''',
    'textile.html': '''        // Thread weave on image hover
        document.querySelectorAll('.card-img-wrap, .feature-img').forEach(el => {
            el.addEventListener('mouseenter', (e) => {
                const rect = el.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                
                // create horizontal thread
                const th = document.createElement('div');
                th.className = 'thread-line thread-h';
                th.style.top = y + 'px';
                th.style.animation = 'threadShootH 0.8s ease forwards';
                
                // create vertical thread
                const tv = document.createElement('div');
                tv.className = 'thread-line thread-v';
                tv.style.left = x + 'px';
                tv.style.animation = 'threadShootV 0.8s ease forwards';
                
                el.appendChild(th);
                el.appendChild(tv);
                setTimeout(() => { th.remove(); tv.remove(); }, 800);
            });
        });'''
}

for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update dropdown CSS
    if '/* Dropdown */' not in content:
        content = content.replace('</style>', nav_dropdown_css + '\n    </style>')
    
    # 2. Update Navbar section
    old_nav_regex = r'<ul class=\"nav-links\">.*?</ul>'
    content = re.sub(old_nav_regex, new_nav_html, content, flags=re.DOTALL)
    
    # 3. Add Category Anim CSS & JS (if applicable)
    if fname in anim_css_map and '/* ' + ('Water Splash' if 'seafood' in fname else ('Turmeric Burst' if 'vegetable' in fname else 'Thread wave')) not in content:
         content = content.replace('</style>', anim_css_map[fname] + '\n    </style>')
    
    if fname in anim_js_map and 'document.querySelectorAll(\'.card-img-wrap, .feature-img\').forEach(el => {\n            el.addEventListener(\'mouseenter\'' not in content:
        content = content.replace('</script>', anim_js_map[fname] + '\n    </script>')
        
    # 4. Correct specific backgrounds just to make them more "their own theme" while maintaining the site tone
    target_bgs = {
        'seafood.html': '#eef3f6',   # cooler blue-gray off-white
        'vegetables-turmeric.html': '#f5f7f2', # warmer green-tinted off-white
        'textile.html': '#fcf8f6' # warm rose-tinted off-white
    }
    
    if fname in target_bgs: 
        bg_pattern = r'(--bg:\s*#\w{6};)'
        current_bg_match = re.search(bg_pattern, content)
        if current_bg_match:
            # Check if it isn't already set to the new one
            if target_bgs[fname] not in current_bg_match.group(1):
                 content = re.sub(bg_pattern, f'--bg: {target_bgs[fname]};', content, count=1)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updates applied to all files successfully")

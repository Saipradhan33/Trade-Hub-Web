import os

with open('frontend.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Shared modifications
def generate_page(filename, title, vars_dict, hero_tag, hero_h1, hero_desc, badge_num, badge_label,
                  products_title, products_h2, feature_tag, feature_h2, feature_desc_1, feature_desc_2, feature_desc_3, feature_desc_4):
    content = html
    
    # Title
    content = content.replace('<title>Forma — Product Showcase</title>', f'<title>Forma — {title}</title>')
    
    # CSS Vars
    old_vars = '''        :root {
            --bg: #f7f5f2;
            --surface: #ffffff;
            --text: #1a1814;
            --muted: #9a9589;
            --accent: #c8a96e;
            --border: #e8e4de;
            --card-bg: #fdfcfa;
        }'''
    
    new_vars = f'''        :root {{
            --bg: {vars_dict['bg']};
            --surface: {vars_dict['surface']};
            --text: {vars_dict['text']};
            --muted: {vars_dict['muted']};
            --accent: {vars_dict['accent']};
            --border: {vars_dict['border']};
            --card-bg: {vars_dict['card_bg']};
        }}'''
    content = content.replace(old_vars, new_vars)
    
    # Hero
    content = content.replace('<div class=\"hero-tag\">New Collection 2025</div>', f'<div class=\"hero-tag\">{hero_tag}</div>')
    content = content.replace('<h1>Crafted for<br><em>those who notice</em><br>the details</h1>', hero_h1)
    content = content.replace('<p class=\"hero-desc\">Each piece is designed with intention — where simplicity meets precision. No excess,\n                only what matters.</p>', f'<p class=\"hero-desc\">{hero_desc}</p>')
    
    # Badge
    content = content.replace('<div class=\"badge-num\">240+</div>', f'<div class=\"badge-num\">{badge_num}</div>')
    content = content.replace('<div class=\"badge-label\">Products Crafted</div>', f'<div class=\"badge-label\">{badge_label}</div>')
    
    # Products Header
    content = content.replace('<div class=\"section-tag\">The Collection</div>', f'<div class=\"section-tag\">{products_title}</div>')
    content = content.replace('<h2>Pieces made to<br><em>last a lifetime</em></h2>', products_h2)
    
    # Features
    content = content.replace('<div class=\"section-tag\">Why Forma</div>', f'<div class=\"section-tag\">{feature_tag}</div>')
    content = content.replace('<h2>Every detail<br>is <em>deliberate</em></h2>', feature_h2)
    
    # Feature desc
    content = content.replace('Sourced from certified suppliers with full traceability — from raw\\n                                material to your hands.', feature_desc_1)
    content = content.replace('Each piece passes through at least three artisans before it ever\\n                                reaches packaging.', feature_desc_2)
    content = content.replace('Fully recyclable, minimal packaging. No plastic, no excess. Just\\n                                the product.', feature_desc_3)
    content = content.replace('We stand behind everything we make. If something breaks, we fix or\\n                                replace it. Always.', feature_desc_4)
    
    # Update navigation links
    nav_old = '''<ul class=\"nav-links\">\n            <li><a href=\"#products\">Collection</a></li>\n            <li><a href=\"#about\">About</a></li>\n            <li><a href=\"#story\">Story</a></li>\n        </ul>'''
    nav_new = '''<ul class=\"nav-links\">\n            <li><a href=\"frontend.html\">Home</a></li>\n            <li><a href=\"seafood.html\">Sea Food</a></li>\n            <li><a href=\"vegetables-turmeric.html\">Vegetables</a></li>\n            <li><a href=\"textile.html\">Textile</a></li>\n        </ul>'''
    content = content.replace(nav_old, nav_new)

    # Empty products grid for simplicity to be filled manually or replaced
    products_grid_old = content[content.find('<div class=\"products-grid reveal\">'):content.find('</section>', content.find('<div class=\"products-grid reveal\">'))]
    products_grid_new = f'<div class=\"products-grid reveal\" id=\"{filename.split(".")[0]}-grid\">\\n            <!-- dynamic content -->\\n        </div>\\n    '
    content = content.replace(products_grid_old, products_grid_new)

    with open(filename, 'w', encoding='utf-8') as fw:
        fw.write(content)

# SEAFOOD
generate_page(
    'seafood.html', 'Sea Food',
    {'bg': '#f2f5f7', 'surface': '#ffffff', 'text': '#14181a', 'muted': '#788b99', 'accent': '#4a7c99', 'border': '#dbe4e8', 'card_bg': '#f8fafc'},
    'Ocean Fresh 2025', '<h1>Sustainably sourced<br><em>from the deep</em><br>blue sea</h1>',
    'Premium quality sea food, caught daily and delivered fresh to maintain the highest standards of taste and nutrition.',
    '48h', 'From Ocean to Table',
    'Sea Food Market', '<h2>Fresh catch of<br><em>the day</em></h2>',
    'Why Our Seafood', '<h2>Quality from<br><em>catch to plate</em></h2>',
    'Responsibly sourced from sustainable fisheries protecting marine ecosystems.',
    'Hand-inspected for quality and freshness immediately after docking.',
    'Packed in specialized temperature-controlled, eco-friendly containers.',
    'Guaranteed fresh delivery with full origin traceability on every catch.'
)

# VEGETABLES & TURMERIC
generate_page(
    'vegetables-turmeric.html', 'Vegetables & Turmeric',
    {'bg': '#f4f6f2', 'surface': '#ffffff', 'text': '#161a14', 'muted': '#849679', 'accent': '#6b8e4e', 'border': '#dfe6d8', 'card_bg': '#fafdf8'},
    'Organic Harvest 2025', '<h1>Grown with care<br><em>by local</em><br>farmers</h1>',
    'Fresh, organic vegetables and premium turmeric, cultivated without harmful chemicals to bring nature’s best to your kitchen.',
    '100%', 'Certified Organic',
    'Farm Fresh', '<h2>Rooted in the<br><em>earth</em></h2>',
    'Why Our Produce', '<h2>Nourished by<br><em>nature</em></h2>',
    'Grown in nutrient-rich soil without synthetic pesticides or fertilizers.',
    'Harvested by hand at peak ripeness to ensure maximum flavor.',
    'Delivered fresh in minimal, biodegradable packaging.',
    'Partnering with local farms to support sustainable agricultural communities.'
)

# TEXTILE
generate_page(
    'textile.html', 'Textile Collection',
    {'bg': '#f7f3f2', 'surface': '#ffffff', 'text': '#1a1514', 'muted': '#998078', 'accent': '#c8766e', 'border': '#e8dbd8', 'card_bg': '#fcf9f8'},
    'Artisanal Weaves 2025', '<h1>Woven with<br><em>tradition and</em><br>passion</h1>',
    'Finely crafted textiles made from sustainable fibers. Each thread tells a story of heritage and expert craftsmanship.',
    '500+', 'Artisan Weavers',
    'Textile Gallery', '<h2>Threads of<br><em>elegance</em></h2>',
    'Why Our Textiles', '<h2>Woven to<br><em>perfection</em></h2>',
    'Spun from organic, sustainably harvested cotton, linen, and silk fibers.',
    'Hand-loomed by master artisans preserving generations of technique.',
    'Dyed using natural, plant-based colors that are gentle on the earth.',
    'Crafted to become heirloom pieces that soften and beautify with time.'
)

print('Generated pages.')

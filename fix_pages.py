import os

files_data = {
    'seafood.html': '''
            <a href="#" class="product-card" style="text-decoration: none;">
                <div class="card-img-wrap">
                    <div class="img-placeholder" style="aspect-ratio:1; min-height: 180px; background: #dbe4e8; color: #14181a;">🦐</div>
                    <span class="card-tag">Fresh</span>
                </div>
                <div class="card-body">
                    <div class="card-name">Jumbo King Prawns</div>
                    <div class="card-desc">Wild-caught and delivered fresh daily. Perfect for grilling or scampi.</div>
                </div>
            </a>
            <a href="#" class="product-card" style="text-decoration: none;">
                <div class="card-img-wrap">
                    <div class="img-placeholder" style="aspect-ratio:1; min-height: 180px; background: #dbe4e8; color: #14181a;">🐠</div>
                    <span class="card-tag">Bestseller</span>
                </div>
                <div class="card-body">
                    <div class="card-name">Atlantic Salmon Fillet</div>
                    <div class="card-desc">Responsibly farmed in cold ocean waters. Rich in Omega-3 and flavor.</div>
                </div>
            </a>
            <a href="#" class="product-card" style="text-decoration: none;">
                <div class="card-img-wrap">
                    <div class="img-placeholder" style="aspect-ratio:1; min-height: 180px; background: #dbe4e8; color: #14181a;">🐟</div>
                    <span class="card-tag">Premium</span>
                </div>
                <div class="card-body">
                    <div class="card-name">Yellowfin Tuna Steaks</div>
                    <div class="card-desc">Sustainably line-caught prime cuts, ideal for searing or sashimi.</div>
                </div>
            </a>''',
    'vegetables-turmeric.html': '''
            <a href="#" class="product-card" style="text-decoration: none;">
                <div class="card-img-wrap">
                    <div class="img-placeholder" style="aspect-ratio:1; min-height: 180px; background: #dfe6d8; color: #161a14;">🪴</div>
                    <span class="card-tag">Organic</span>
                </div>
                <div class="card-body">
                    <div class="card-name">Fresh Root Turmeric</div>
                    <div class="card-desc">Earthy, vibrant, and packed with curcumin. Grown in nutrient-rich soil.</div>
                </div>
            </a>
            <a href="#" class="product-card" style="text-decoration: none;">
                <div class="card-img-wrap">
                    <div class="img-placeholder" style="aspect-ratio:1; min-height: 180px; background: #dfe6d8; color: #161a14;">🍅</div>
                    <span class="card-tag">Seasonal</span>
                </div>
                <div class="card-body">
                    <div class="card-name">Heirloom Tomatoes</div>
                    <div class="card-desc">Sun-ripened and hand-picked for maximum sweetness and juiciness.</div>
                </div>
            </a>
            <a href="#" class="product-card" style="text-decoration: none;">
                <div class="card-img-wrap">
                    <div class="img-placeholder" style="aspect-ratio:1; min-height: 180px; background: #dfe6d8; color: #161a14;">🥦</div>
                    <span class="card-tag">Farm Fresh</span>
                </div>
                <div class="card-body">
                    <div class="card-name">Organic Broccoli</div>
                    <div class="card-desc">Crisp, green, and sustainably harvested. Zero synthetic pesticides used.</div>
                </div>
            </a>''',
    'textile.html': '''
            <a href="#" class="product-card" style="text-decoration: none;">
                <div class="card-img-wrap">
                    <div class="img-placeholder" style="aspect-ratio:1; min-height: 180px; background: #e8dbd8; color: #1a1514;">🧺</div>
                    <span class="card-tag">Bestseller</span>
                </div>
                <div class="card-body">
                    <div class="card-name">Woven Linen Throw</div>
                    <div class="card-desc">Portuguese linen, stone-washed for softness and durability.</div>
                </div>
            </a>
            <a href="#" class="product-card" style="text-decoration: none;">
                <div class="card-img-wrap">
                    <div class="img-placeholder" style="aspect-ratio:1; min-height: 180px; background: #e8dbd8; color: #1a1514;">🧶</div>
                    <span class="card-tag">New</span>
                </div>
                <div class="card-body">
                    <div class="card-name">Artisanal Cotton Rug</div>
                    <div class="card-desc">Hand-loomed organic cotton rug, dyed with natural plant extracts.</div>
                </div>
            </a>
            <a href="#" class="product-card" style="text-decoration: none;">
                <div class="card-img-wrap">
                    <div class="img-placeholder" style="aspect-ratio:1; min-height: 180px; background: #e8dbd8; color: #1a1514;">🧣</div>
                    <span class="card-tag">Limited</span>
                </div>
                <div class="card-body">
                    <div class="card-name">Hand-dyed Silk Scarf</div>
                    <div class="card-desc">100% pure silk, woven and dyed by master artisans using ancient techniques.</div>
                </div>
            </a>'''
}

for fname, addition in files_data.items():
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # The string explicitly contains a literal '\n' string instead of a newline, let's fix that
    content = content.replace('\\n', '\n')
    
    # replace the dynamic content comment with actual cards
    grid_id = fname.split('.')[0] + '-grid'
    old_grid = f'<div class="products-grid reveal" id="{grid_id}">\n            <!-- dynamic content -->\n        </div>'
    new_grid = f'<div class="products-grid reveal" id="{grid_id}">\n{addition}\n        </div>'
    
    if old_grid in content:
        content = content.replace(old_grid, new_grid)

    with open(fname, 'w', encoding='utf-8') as fw:
        fw.write(content)

print('Updated files with products.')

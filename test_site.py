from playwright.sync_api import sync_playwright
from pathlib import Path
import http.server, socketserver, threading, functools
p=Path(__file__).resolve().parent
handler=functools.partial(http.server.SimpleHTTPRequestHandler,directory=str(p))
server=socketserver.TCPServer(('127.0.0.1',0),handler)
threading.Thread(target=server.serve_forever,daemon=True).start()
with sync_playwright() as pw:
 b=pw.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage','--disable-background-networking'])
 page=b.new_page(viewport={'width':1440,'height':1100},device_scale_factor=1)
 errs=[]
 page.on('pageerror',lambda e: errs.append(str(e)))
 page.goto(f'http://127.0.0.1:{server.server_address[1]}/index.html',wait_until='domcontentloaded',timeout=20000)
 page.wait_for_timeout(800)
 print('TITLE',page.title())
 print('CARDS',page.locator('.book-card').count(),'CATEGORIES',page.locator('.genre-card').count())
 page.screenshot(path=str(p/'preview.png'),full_page=False)
 page.get_by_role('button',name='View all 12 →').first.click()
 print('CATEGORY CARDS',page.locator('.book-card').count())
 page.get_by_role('button',name='Add The Shining to bag').click()
 page.locator('#cartBtn').click()
 print('CART',page.locator('#subtotal').inner_text(),'BAG',page.locator('#cartCount').inner_text())
 page.locator('.drawer [data-close]').click()
 page.locator('#searchInput').fill('hunger')
 print('SEARCH CARDS',page.locator('.book-card').count())
 print('JS ERRORS',errs)
 b.close()
server.shutdown()

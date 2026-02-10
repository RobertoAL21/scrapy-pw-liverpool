from playwright.sync_api import sync_playwright
import time
import os
from pathlib import Path

BASE_URL = "https://www.liverpool.com.mx/tienda/laptops/catst10075558"
URLS = [
    BASE_URL,
    f"{BASE_URL}/page-2",
]

def fetch_html(output_dir: Path):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        for idx, url in enumerate(URLS, start=1):
            page.goto(url, wait_until="domcontentloaded", timeout=60000)

            page.wait_for_selector("li.m-product__card", timeout=60000)
            page.wait_for_timeout(1500)

            page.evaluate("""
                (() => {
                    const container = document.querySelector('ul.m-product__listing');

                    if (!container) return;

                    const cards = Array.from(container.querySelectorAll('li.m-product__card'));

                    cards.forEach((card, index) => {
                        card.setAttribute('data-visual-order', index);
                    });
                })();
                """)

            html = page.content()
            (output_dir / f"page_{idx}.html").write_text(html, encoding="utf-8")

        browser.close()


if __name__ == "__main__":
    temp_dir = os.environ.get("HTML_TEMP_DIR")
    if not temp_dir:
        raise RuntimeError("HTML_TEMP_DIR no está definido")

    fetch_html(Path(temp_dir))
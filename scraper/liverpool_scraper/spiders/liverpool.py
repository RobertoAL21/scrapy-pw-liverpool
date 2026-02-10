import scrapy
from pathlib import Path
import os


class LiverpoolSpider(scrapy.Spider):
    name = "liverpool"

    def start_requests(self):
        html_dir = Path(os.environ["HTML_TEMP_DIR"])

        for html_file in sorted(html_dir.glob("page_*.html")):
            yield scrapy.Request(
                url=f"file://{html_file.resolve()}",
                callback=self.parse,
                dont_filter=True,
            )

    def parse(self, response):
        ordered_cards = sorted(
            response.css("li.m-product__card"),
            key=lambda c: int(c.attrib.get("data-visual-order", 0))
        )

        cards = ordered_cards[:10]

        for card in cards:
            brand = card.css("h3.a-card-brand::text").get(default="N/A").strip()
            description = card.css("h3.a-card-description::text").get(default="N/A").strip()
            price = self.extract_price(card)

            yield {
                "brand": brand,
                "description": description,
                "price": price,
            }

    def extract_price(self, card):
        price_container = card.css("p.a-card-discount")

        if not price_container:
            return "N/A"

        main_price = price_container.css("::text").get()
        if not main_price:
            return "N/A"

        main_price = (
            main_price
            .replace("$", "")
            .replace("\n", "")
            .replace(" ", "")
            .strip()
        )

        cents = price_container.css("sup::text").get(default="00").strip()

        if not main_price.replace(",", "").isdigit():
            return "N/A"

        return f"${main_price}.{cents}"
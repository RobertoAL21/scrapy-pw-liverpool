# settings.py

BOT_NAME = "liverpool"

SPIDER_MODULES = ["liverpool_scraper.spiders"]
NEWSPIDER_MODULE = "liverpool_scraper.spiders"

ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
    "liverpool_scraper.pipelines.LiverpoolTxtPipeline": 300,
}

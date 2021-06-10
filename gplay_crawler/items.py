# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy_jsonschema.item import JsonSchemaItem


class GplayCrawlerItem(JsonSchemaItem):
    jsonschema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "title": "GplayCrawler",
        "description": "Crawler for Hardware/Peripherals in Gplay",
        "type": "object",
        "properties": {
            "gp_cat": {
                "type": "string",
                },
            "gp_sub_cat": {
                "type": "string",
                },
            "gp_title": {
                    "type": "string",
                },
            "gp_sub_title": {
                    "type": "string",
                },
            "gp_art_num": {
                    "type": "string",
                },
            "pg_price": {
                    "type": "number",
                }
            },
        }

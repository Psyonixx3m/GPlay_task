import scrapy
from gplay_crawler.items import GplayCrawlerItem


class GPlayCrawler(scrapy.Spider):
    name = "gp_items"
    cnt = 0
    start_urls = [
                "https://gplay.bg/%D0%B3%D0%B5%D0%B9%D0%BC%D0%B8%D0%BD%D0%B3-%D1%85%D0%B0%D1%80%D0%B4%D1%83%D0%B5%D1%80",
                "https://gplay.bg/%D0%B3%D0%B5%D0%B9%D0%BC%D0%B8%D0%BD%D0%B3-%D0%BF%D0%B5%D1%80%D0%B8%D1%84%D0%B5%D1%80%D0%B8%D1%8F",
                ]

    def parse(self, resp):
        gp_items_url = resp.xpath("//div[@class='categories-grid']//a//@href").getall()
        for items in gp_items_url:
            yield scrapy.Request(url=items, callback=self.parse_page)

    def parse_page(self, resp):
        gp_items_list = resp.xpath("//div[@class='product-item']//a[@class='product-name']//@href").getall()
        for items in gp_items_list:
            yield scrapy.Request(url=items, callback=self.parse_item)

        next_page = resp.xpath("//a[@rel='next']")
        if next_page:
            next_page_url = next_page.xpath("./@href").get()
            if self.cnt < 1:
                self.cnt += 1
                yield scrapy.Request(url=next_page_url, callback=self.parse_item)

    def parse_item(self, resp):
        gp_cat = resp.xpath("//div[@class='path py-3']//a[2]//text()").get()
        gp_sub_cat = resp.xpath("//div[@class='path py-3']//a[3]//text()").get()
        gp_title = resp.xpath("//h1[@class='large-title']").get()
        gp_sub_title = resp.xpath("//h2[@class='product-subtitle ']").get()
        gp_art_num = resp.xpath("//div[contains(@class,'product-ref-number')]").get()
        pg_price = resp.xpath("//div[@class='normal-price ']").get()
        item = GplayCrawlerItem()
        item["gp_cat"] = gp_cat
        item["gp_sub_cat"] = gp_sub_cat
        item["gp_title"] = gp_title
        item["gp_sub_title"] = gp_sub_title
        item["gp_art_num"] = gp_art_num
        item["pg_price"] = pg_price

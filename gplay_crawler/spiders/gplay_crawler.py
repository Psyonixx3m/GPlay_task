import scrapy
from gplay_crawler.items import GplayCrawlerItem
import sqlite3

conn = sqlite3.connect('gplay.db')
c = conn.cursor()

c.execute('''CREATE TABLE gplaydata(gp_cat TEXT, gp_sub_cat TEXT, gp_title TEXT, gp_sub_title TEXT, gp_art_num TEXT, pg_price REAL)''')


class GPlayCrawler(scrapy.Spider):
    name = "gp_items"
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
            yield scrapy.Request(url=next_page_url, callback=self.parse_item)

    def parse_item(self, resp):
        gp_avail = resp.xpath("//span[@title='наличен']").get()
        gp_lim_avail = resp.xpath("//span[contains(@title,'ограничена')]")
        if gp_avail or gp_lim_avail:

            gp_cat = resp.xpath("//div[@class='path py-3']//a[contains(text(),'')][2]//text()").get()
            gp_sub_cat = resp.xpath("//div[@class='path py-3']//a[contains(text(),'')][3]//text()").get()
            gp_title = resp.xpath("//h1[@class='large-title']//text()").get()
            gp_sub_title = resp.xpath("//h2[@class='product-subtitle ']//text()").get()
            gp_art_num = resp.xpath("//div[@class='col-md-6 product-ref-number']//strong//text()").get()
            pg_price = float(resp.xpath("//div[contains(@class, 'product-price-controls')]//price/@*").get())
            if pg_price < 200:
                item = GplayCrawlerItem()
                item["gp_cat"] = gp_cat
                item["gp_sub_cat"] = gp_sub_cat
                item["gp_title"] = gp_title
                item["gp_sub_title"] = gp_sub_title
                item["gp_art_num"] = gp_art_num
                item["pg_price"] = pg_price
                c.execute(''' INSERT INTO gplaydata(gp_cat, gp_sub_cat, gp_title, gp_sub_title, gp_art_num, pg_price) VALUES(?,?,?,?,?,?)''',(gp_cat, gp_sub_cat, gp_title, gp_sub_title, gp_art_num, pg_price))
                conn.commit()
                yield item


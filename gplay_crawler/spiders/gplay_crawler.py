import scrapy


class GPlayCrawler(scrapy.Spider):
    name = "gp_items"
    start_urls = [
                "https://gplay.bg/%D0%B3%D0%B5%D0%B9%D0%BC%D0%B8%D0%BD%D0%B3-%D1%85%D0%B0%D1%80%D0%B4%D1%83%D0%B5%D1%80",
                "https://gplay.bg/%D0%B3%D0%B5%D0%B9%D0%BC%D0%B8%D0%BD%D0%B3-%D0%BF%D0%B5%D1%80%D0%B8%D1%84%D0%B5%D1%80%D0%B8%D1%8F",
                ]
    
    def parse(self, resp):
        gp_items_url = resp.xpath("//div[@class='categories-grid']//a//@href").getall()
        for items in gp_items_url:
            yield items

    # def parse_cat_list(self, resp):
    #     gp_cat_list = resp.xpath("//div[@class='catalog-grid']//a[@class='product-name']//@href").getall()
    #     for items in gp_cat_list:
    #         yield items
import scrapy


class PwspiderSpider(scrapy.Spider):
    name = 'pwspider'
    page_number = 1

    def start_requests(self):
        # 25 stránek * 20 bytů na stránku = 500 položek
        for strana in range(1, 26):
            yield scrapy.Request('https://www.sreality.cz/hledani/prodej/byty?strana='+str(strana), meta={'playwright': True})

    def parse(self, response):
        for item in response.css('div.property'):
            yield {
                'title': item.css('span.basic h2 a span::text').get(),
                'img_url': item.css('img::attr(src)').get()
            }

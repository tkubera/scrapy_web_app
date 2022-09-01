import scrapy


class PwspiderSpider(scrapy.Spider):
    name = 'pwspider'
    page_number = 2

    def start_requests(self):
        for strana in range(1, 2):
            #yield scrapy.Request('https://www.sreality.cz/hledani/prodej/byty', meta={'playwright': True})
            yield scrapy.Request('https://www.sreality.cz/hledani/prodej/byty?strana='+str(strana), meta={'playwright': True})

    def parse(self, response):
        #unicode(response.body.decode(response.encoding)).encode('utf-8')

        #yield{
        #    'text': response.text
        #}

        for item in response.css('div.property'):
            yield {
        #        #'title': item.css('div.info div.text-wrap span.basic h2 a span::text').get(),
                'title': item.css('span.basic h2 a span::text').get(),
                #'img_url': item.css('preact div div a img::attr(src)').extract(),
                #'img_url_2': item.css('preact div div a img::attr(src)').extract(),
                'img_url_3': item.css('img::attr(src)').get()
            }

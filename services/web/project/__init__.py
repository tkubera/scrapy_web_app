import subprocess
import crochet

crochet.setup()

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from scrapy import signals
from scrapy.crawler import CrawlerProcess, CrawlerRunner

from scrapy.signalmanager import dispatcher
#from .pwdemo.spiders.pwspider import PwspiderSpider


app = Flask(__name__)
app.config.from_object("project.config.Config")
app.debug = True
# instance of SQLAlchemy for DB
db = SQLAlchemy(app)

# crawl_runner = CrawlerRunner(
#     settings={
#             # "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
#             "DOWNLOAD_HANDLERS": {
#                 "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
#                 "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
#             },
#             "CONCURRENT_REQUESTS": 32,
#             "FEED_EXPORT_ENCODING": 'utf-8',
#         }
# )
# output_data = []
# a_output_data = []


class Data(db.Model):
    __tablename__ = "data"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True, nullable=False)
    image_url = db.Column(db.String(), nullable=False)

    def __init__(self, title, image_url):
        self.title = title
        self.image_url = image_url


@app.route('/')
def hello_world():
    """
    Run spider in another process and store items in file. Simply issue command:

    > scrapy crawl dmoz -o "output.json"

    wait for  this command to finish, and read output.json to client.
    """
    spider_name = "pwspider"
    subprocess.check_output(['scrapy', 'crawl', spider_name, "-o", "output.json"])
    with open("output.json") as items_file:
        return items_file.read()


if __name__ == '__main__':
    app.run(debug=True)


# @app.route("/")
# def index():
#     return render_template('index.html', data=get_all_records())
#
#
# @app.route("/scrape")
# def scape():
#     # scrape_with_crochet()
#     # return redirect(url_for('index'))
#     spider_name = "pwspider"
#     subprocess.check_output(['scrapy', 'crawl', spider_name, "-o", "output.json"])
#     with open("output.json") as items_file:
#         return items_file.read()
#     # return render_template('index.html', data=jsonify(output_data))
#     # return render_template('index.html', data=x)


# @crochet.wait_for(timeout=60.0)
# def scrape_with_crochet():
#     # signal fires when single item is processed
#     # and calls _crawler_result to append that item
#     dispatcher.connect(_crawler_result, signal=signals.item_scraped)
#     eventual = crawl_runner.crawl(PwspiderSpider)
#     spider_results()
#     return eventual  # returns a twisted.internet.defer.Deferred
#
#
# def _crawler_result(item, response, spider):
#     """
#     We're using dict() to decode the items.
#     Ideally this should be done using a proper export pipeline.
#     """
#     output_data.append(dict(item))


# def get_all_records():
#     return Data.query.all()
#
#
# # TODO provolat z manage.py
# def create_db():
#     db.drop_all()
#     db.create_all()
#     db.session.commit()
#
#
# @crochet.wait_for(timeout=120.0)
# async def spider_results():
#     results = []
#
#     def crawler_results(signal, sender, item, response, spider):
#         results.append(item)
#
#     dispatcher.connect(crawler_results, signal=signals.item_scraped)
#
#     process = CrawlerProcess(
#         settings={
#             # "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
#             "DOWNLOAD_HANDLERS": {
#                 "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
#                 "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
#             },
#             "CONCURRENT_REQUESTS": 32,
#             "FEED_EXPORT_ENCODING": 'utf-8',
#         })
#     process.crawl(PwspiderSpider)
#     process.start()  # the script will block here until the crawling is finished
#     return results

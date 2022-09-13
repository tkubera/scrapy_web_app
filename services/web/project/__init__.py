import json
import subprocess

from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("project.config.Config")
app.debug = True
# instance of SQLAlchemy for DB
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = "data"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=False, nullable=False)
    image_url = db.Column(db.String(), nullable=False)

    def __init__(self, title, image_url):
        self.title = title
        self.image_url = image_url


@app.route('/')
def home():
    return render_template('index.html', data=get_all_records())


@app.route('/scrape')
def scrape():
    """
    Run spider in another process and store items in file. Simply issue command:

    > scrapy crawl dmoz -o "output.json"

    wait for  this command to finish, and read output.json to client.
    """
    # chyba z původního navrhu, spouštění skenovaní ze špateného adresaře
    # scrapy crawl swspider -o cache.json je potřeba stpustit v adresaři project
    open('project/cache.json', 'w').close()
    p = subprocess.Popen(['scrapy', 'crawl', 'pwspider', "-o", "cache.json"], cwd='project',
                         shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out, err = p.communicate()
    # print('SUBPROCESS ERROR: ' + str(err))
    # print('SUBPROCESS stdout: ' + str(out.decode()))
    data = {"err": str(err), "stdout": str(out.decode())}

    obj = json.load(open("project/cache.json"))
    for i in range(len(obj)):
        title = obj[i]["title"]
        url = obj[i]["img_url"]
        insert_record(title, url)

    return redirect('/')


@app.route('/delete')
def delete_all():
    create_db()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)


def insert_record(title, url):
    db.session.add(Data(title, url))
    db.session.commit()


def get_all_records():
    return Data.query.all()


# # TODO provolat z manage.py
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
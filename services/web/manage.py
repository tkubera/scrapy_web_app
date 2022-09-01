from flask.cli import FlaskGroup

from project import app, db, Data


cli = FlaskGroup(app)


# docker-compose exec web python manage.py create_db
# check db
# docker-compose exec db psql --username=admin --dbname=scrapy_app
# select db - \c scrapy_app


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(Data(title="Test nemovitost2", image_url="http//:.."))
    db.session.commit()


if __name__ == "__main__":
    cli()

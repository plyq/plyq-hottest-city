import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


class City(db.Model):
    __tablename__ = "city"
    index = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    country = db.Column(db.String(32))
    open_weather_id = db.Column(db.Integer)

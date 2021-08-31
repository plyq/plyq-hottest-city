import flask

import hottest.config as hcfg
import hottest.models as hm


def create_app():
    flask_app = flask.Flask(__name__)
    flask_app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = hcfg.get_database_connection_uri()
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    flask_app.app_context().push()
    hm.db.init_app(flask_app)
    hm.db.create_all()
    return flask_app

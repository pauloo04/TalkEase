import os

from flask import Flask, redirect, url_for

from werkzeug.debug import DebuggedApplication
from . import db, home, auth

SECRET_KEY = "jSoNxYNvHIRBsBTp7tBeTMsVd6XWIE8Y"


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.static_folder = "static"
    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        DATABASE=os.path.join(app.instance_path, "talkease.sqlite"),
        TEMPLATES_AUTO_RELOAD=True,
    )

    app.debug = True
    app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(home.bp)
    app.register_blueprint(auth.bp) 
    db.init_app(app)
        
    @app.route("/")
    def index():
        return redirect(url_for("home.home"))

    return app


app = create_app()

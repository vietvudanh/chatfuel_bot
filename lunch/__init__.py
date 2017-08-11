from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('lunch.config.DevConfig')

    from lunch.views.general import general

    app.register_blueprint(general)

    return app

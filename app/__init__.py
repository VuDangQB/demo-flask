from flask import Flask

def create_app(config_name="dev"):
    app = Flask(__name__)

    from app.apis import blueprint
    # from app.views import main_blp
    app.register_blueprint(blueprint)
    return app


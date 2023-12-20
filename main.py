from flask import Flask
from objects.db import db
from blueprints.page_generator_blueprint import page_generator_blueprint


def create_app():
    # создание сервера
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    db.init_app(app)
    app.register_blueprint(page_generator_blueprint)

    with app.app_context():
        db.create_all()

    return app


server = create_app()


if __name__ == '__main__':
    server.run(port=8881)
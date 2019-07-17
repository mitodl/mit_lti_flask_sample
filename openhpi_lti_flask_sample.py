import os
import sys
import logging

from flask import Flask
from orator import (
    DatabaseManager,
    Model
)

import config


def setup_database():
    """ enable database

    """
    from orator import DatabaseManager, Model
    db = DatabaseManager(config.DATABASES)
    Model.set_connection_resolver(db)


def setup_logging(loglevel=logging.DEBUG):
    """ enable debug logging

    :param loglevel: logging level
    """
    logger = logging.getLogger()
    logger.setLevel(loglevel)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(loglevel)
    formatter = logging.Formatter('%(name)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)


def setup_app():
    """ create and setup flask app

    :return: flask app
    """
    # import the individual exercise controller (as blueprints)
    from index import index_blueprint
    from exercises.add import add_blueprint
    from exercises.multiply import multiply_blueprint
    from exercises.divide import divide_blueprint

    # initiiate database
    setup_database()

    app = Flask(__name__)
    app.config.from_object(config)

    # register front controller
    app.register_blueprint(index_blueprint)

    # register exercise controller
    app.register_blueprint(add_blueprint)
    app.register_blueprint(multiply_blueprint)
    app.register_blueprint(divide_blueprint)

    return app


if __name__ == '__main__':
    app = setup_app()
    port = int(os.environ.get("FLASK_LTI_PORT", 5000))
    host = os.environ.get("FLASK_LTI_HOST", '0.0.0.0')
    app.run(debug=True, host=host, port=port)

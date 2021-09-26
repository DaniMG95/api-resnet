from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from resources.predict import PredictImage, PredictURL


def create_app():
    _app = Flask(__name__)
    api = Api(_app, prefix='/api/')
    CORS(_app)
    api.add_resource(PredictImage, '/image/')
    api.add_resource(PredictURL, '/url/')
    return _app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0')

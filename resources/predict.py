from flask_restful import Resource, reqparse
from models.predictUrl import PredictUrlModel

class PredictImage(Resource):
    def get(self):
        return {'hello': 'world'}



class PredictURL(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('url', type=str, help='URl image to charge for this resource')

    @classmethod
    def get(cls):
        url_image = cls.parser.parse_args()['url']
        predictor = PredictUrlModel(url_image)
        return predictor.predict_image()



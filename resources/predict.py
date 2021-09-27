from flask_restful import Resource, reqparse
from models.predictUrl import PredictUrlModel
from models.predictImage import PredictImageModel


class PredictImage(Resource):
    """API resource for the endpoint api/image/"""
    parser = reqparse.RequestParser()
    parser.add_argument('img', type=str, help='img to charge for this resource', required=True)

    @classmethod
    def post(cls):
        """POST which takes care of the base64 image retrieval and calls the functions for its prediction."""
        image_base64 = cls.parser.parse_args()['img']
        predictor = PredictImageModel(image_base64)
        return {"class": predictor.predict_image()}


class PredictURL(Resource):
    """API resource for the endpoint api/url/"""
    parser = reqparse.RequestParser()
    parser.add_argument('url', type=str, help='URl image to charge for this resource', required=True)

    @classmethod
    def post(cls):
        """POST which is in charge of obtaining the ulr of the image and calls the functions for its prediction."""
        url_image = cls.parser.parse_args()['url']
        predictor = PredictUrlModel(url_image)
        return {"class": predictor.predict_image()}

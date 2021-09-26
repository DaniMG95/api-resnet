import base64
import requests
from models.predict import Predict
from flask import abort


class PredictUrlModel(Predict):

    def __init__(self, url):
        self.url = url
        super().__init__()

    def predict_image(self):
        try:
            dl_request = requests.get(self.url, stream=True)
            dl_request.raise_for_status()
        except requests.exceptions.HTTPError:
            abort(401, 'This url not exist')
        # Compose a JSON Predict request (send JPEG image in base64).
        jpeg_bytes = base64.b64encode(dl_request.content).decode('utf-8')
        predict_request = '{"instances" : [{"b64": "%s"}]}' % jpeg_bytes
        return self.predict(predict_request)
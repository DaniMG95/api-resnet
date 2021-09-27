import base64
import requests
from models.predict import Predict
from flask import abort


class PredictUrlModel(Predict):
    """Class that takes the url image, downloads it and launches the call to the class to predict it."""
    def __init__(self, url):
        """Initialiser of the PredictUrlModel class, it is necessary to pass the url of the image."""
        self.url = url
        super().__init__()

    def predict_image(self):
        """Function that downloads the image and formats it for prediction."""
        try:
            dl_request = requests.get(self.url, stream=True)
            dl_request.raise_for_status()
        except requests.exceptions.HTTPError:
            abort(401, 'This url not exist')
        jpeg_bytes = base64.b64encode(dl_request.content).decode('utf-8')
        predict_request = '{"instances" : [{"b64": "%s"}]}' % jpeg_bytes
        return self.predict(predict_request)
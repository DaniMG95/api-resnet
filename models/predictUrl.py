import base64
import requests

class PredictUrlModel():

    def __init__(self, url):
        self.url = url
        self.SERVER_URL = 'http://localhost:8501/v1/models/resnet:predict'

    def predict_image(self):
        dl_request = requests.get(self.url, stream=True)
        dl_request.raise_for_status()

        # Compose a JSON Predict request (send JPEG image in base64).
        jpeg_bytes = base64.b64encode(dl_request.content).decode('utf-8')
        predict_request = '{"instances" : [{"b64": "%s"}]}' % jpeg_bytes
        # Send few requests to warm-up the model.
        for _ in range(3):
            response = requests.post(self.SERVER_URL, data=predict_request)
            response.raise_for_status()

        # Send few actual requests and report average latency.
        total_time = 0
        num_requests = 10
        for _ in range(num_requests):
            response = requests.post(self.SERVER_URL, data=predict_request)
            response.raise_for_status()
            total_time += response.elapsed.total_seconds()
            prediction = response.json()['predictions'][0]

        return {"class Prediction": prediction['classes'], "avg latency": ((total_time*1000)/num_requests)}
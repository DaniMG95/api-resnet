import os
import requests
from flask import abort


class Predict:

    def __init__(self):
        self.SERVER_URL = f"http://{os.getenv('server')}/v1/models/resnet:predict"

    def predict(self, image):
        try:
            response = requests.post(self.SERVER_URL, data=image)
            response.raise_for_status()
        except Exception as e:
            print(e)
            abort(401, "This model not accept this data only accept images")
        prediction = response.json()['predictions'][0]

        # Send few actual requests and report average latency.
        total_time = 0
        num_requests = 10
        for _ in range(num_requests):
            response = requests.post(self.SERVER_URL, data=image)
            response.raise_for_status()
            total_time += response.elapsed.total_seconds()

        return {"class Prediction": prediction['classes'], "avg latency": ((total_time * 1000) / num_requests)}

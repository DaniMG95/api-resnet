from lib.predict import Predict


class PredictImageModel(Predict):

    def __init__(self, image_base64):
        super().__init__()
        self.image_base64 = image_base64

    def predict_image(self):
        predict_request = '{"instances" : [{"b64": "%s"}]}' % self.image_base64
        # Send few requests to warm-up the model.
        return self.predict(predict_request)

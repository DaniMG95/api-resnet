from models.predict import Predict


class PredictImageModel(Predict):
    """Class that takes the image in base64 format and launches the call to the class to predict it."""
    def __init__(self, image_base64):
        """Initialiser of the PredictImageModel class, it is necessary to pass the image in base64 format."""
        super().__init__()
        self.image_base64 = image_base64

    def predict_image(self):
        """Function that performs the encapsulation of the image so that it can be launched into the model."""
        predict_request = '{"instances" : [{"b64": "%s"}]}' % self.image_base64
        return self.predict(predict_request)

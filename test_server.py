import unittest
import base64
import server


class ServerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = server.create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.url_image = {'url': 'https://tensorflow.org/images/blogs/serving/cat.jpg'}
        self.path_image = 'cat.jpg'
        self.url = 'https://tensorflow.org/images/blogs/serving/cat.jpg'

    def test_post_PredictImage(self):
        input_image = open(self.path_image, "rb").read()
        encoded_input_string = base64.b64encode(input_image)
        input_string = encoded_input_string.decode("utf-8")
        body = {'img': input_string}
        response = self.client.post('/api/image/', json=body)
        self.assertEqual(response.status_code, 200)

    def test_post_PredictURL(self):
        response = self.client.post('/api/url/', json=self.url_image)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()

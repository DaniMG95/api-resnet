from flask_restful import Resource

class Predict(Resource):
    def get(self):
        return {'hello': 'world'}
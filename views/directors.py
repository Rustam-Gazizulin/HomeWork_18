from flask_restx import Resource, Namespace

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsViews(Resource):
    def get(self):
        return '', 200


@director_ns.route('/<int:did>')
class DirectorViews(Resource):
    def get(self, did):
        return '', 200
from flask_restx import Resource, Namespace

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresViews(Resource):
    def get(self):
        return '', 200


@genre_ns.route('/<int:gid>')
class GenreViews(Resource):
    def get(self, gid):
        return '', 200

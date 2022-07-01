from flask import request, make_response
from flask_restx import Resource, Namespace

from dao.model.movies import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    schema = MovieSchema(many=True)

    def get(self):
        movies = self.schema.dump(movie_service.get_movies(**request.args))
        return movies, 200

    def post(self):
        new_movie = movie_service.create_movie(request.json)

        resp = make_response('', 201)
        resp.headers['location'] = f"{movie_ns.path}/{new_movie.id}"
        return resp


@movie_ns.route('/<int:movie_id>')
class MovieView(Resource):
    schema = MovieSchema()

    def get(self, movie_id: int):
        return self.schema.dump(movie_service.get_movies(movie_id)), 200

    def patch(self, movie_id: int):
        return self.schema.dump(movie_service.update_movie_partial(movie_id, request.json)), 200

    def put(self, movie_id):
        return self.schema.dump(movie_service.update_movie_full(movie_id, request.json)), 200

    def delete(self, movie_id):
        movie_service.delete(movie_id)
        return '', 204

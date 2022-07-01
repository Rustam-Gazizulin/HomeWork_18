from flask import request, make_response
from flask_restx import Resource, Namespace

from dao.model.movies import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):

    def get(self):
        schema = MovieSchema(many=True)

        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')
        if genre_id:
            return schema.dump(movie_service.filter_by_genre(genre_id)), 200

        movies = schema.dump(movie_service.get_movies())
        return movies, 200

    def post(self):
        new_movie = movie_service.create_movie(request.json)

        resp = make_response('', 201)
        resp.headers['location'] = f"{movie_ns.path}/{new_movie.id}"
        return resp


@movie_ns.route('/<int:movie_id>')
class MovieView(Resource):
    def get(self, movie_id: int):
        schema = MovieSchema()

        return schema.dump(movie_service.get_movies(movie_id))

    def patch(self, movie_id: int):
        return movie_service.update_movie_partial(movie_id, request.json)

    def put(self, movie_id):
        return movie_service.update_movie_full(movie_id, request.json)

    def delete(self, movie_id):
        movie_service.delete(movie_id)
        return '', 204


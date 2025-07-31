# python
from flask import Flask, request
from flask_restx import Api, Resource
from imdbinfo.services import get_movie, get_name, search_title

app = Flask(__name__)
api = Api(app, version="1.0.0", title="qd_imdb_api", doc="/apidoc")


@api.route("/movie/<string:imdb_id>")
@api.param("imdb_id", "The IMDB ID of the movie")
class MovieResource(Resource):
    def get(self, imdb_id: str):
        """Retrieve movie details by IMDB ID."""
        movie_data = get_movie(imdb_id)
        if not movie_data:
            api.abort(404, "Movie not found")
        return movie_data.model_dump()


@api.route("/name/<string:imdb_id>")
@api.param("imdb_id", "The IMDB ID of the name entry")
class NameResource(Resource):
    def get(self, imdb_id: str):
        """Retrieve name details by IMDB ID."""
        name_data = get_name(imdb_id)
        if not name_data:
            api.abort(404, "Name not found")
        return name_data.model_dump()


@api.route("/search")
class SearchResource(Resource):
    @api.doc(params={"q": "The search term for the movie title"})
    def get(self):
        """Search for movie titles by a query term."""
        query = request.args.get("q")
        if not query:
            api.abort(400, "Query parameter is required")

        results = search_title(query)
        if not results:
            api.abort(404, "No results found")

        return results.model_dump()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
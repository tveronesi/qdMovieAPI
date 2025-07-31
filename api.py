# python
from flask import Flask, jsonify, request
from imdbinfo.services import search_title, get_movie, get_name

app = Flask(__name__)

@app.route("/movie/<string:imdb_id>")
def get_imdb_data(imdb_id):
    """
    Retrieve movie details by IMDB ID.

    Args:
        imdb_id (str): The IMDB ID of the movie.

    Returns:
        Response: JSON object with movie details if found,
                  otherwise an error message with HTTP 404.
    """
    movie_data = get_movie(imdb_id)
    if not movie_data:
        return jsonify({"error": "Movie not found"}), 404

    return jsonify(movie_data.model_dump())


@app.route("/name/<string:imdb_id>")
def get_name_data(imdb_id):
    """Retrieve name details by IMDB ID."""
    name_data = get_name(imdb_id)
    if not name_data:
        return jsonify({"error": "Name not found"}), 404

    return jsonify(name_data.model_dump())

@app.route("/search")
def search_imdb():
    """
    Search for movie titles by a query term.

    Query Parameters:
        q (str): The search term for the movie title.

    Returns:
        Response: JSON object with search results if found,
                  otherwise an error message with HTTP 400 or 404.
    """
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    results = search_title(query)
    if not results:
        return jsonify({"error": "No results found"}), 404

    return jsonify(results.model_dump())


@app.route("/apidoc")
def apidoc():
    """Return a minimal OpenAPI specification for the service."""
    spec = {
        "openapi": "3.0.0",
        "info": {"title": "qd_imdb_api", "version": "1.0.0"},
        "paths": {
            "/movie/{imdb_id}": {
                "get": {
                    "summary": "Retrieve movie details by IMDB ID",
                    "parameters": [
                        {
                            "in": "path",
                            "name": "imdb_id",
                            "schema": {"type": "string"},
                            "required": True,
                        }
                    ],
                    "responses": {
                        "200": {"description": "Movie details"},
                        "404": {"description": "Movie not found"},
                    },
                }
            },
            "/search": {
                "get": {
                    "summary": "Search for movie titles by a query term",
                    "parameters": [
                        {
                            "in": "query",
                            "name": "q",
                            "schema": {"type": "string"},
                            "required": True,
                        }
                    ],
                    "responses": {
                        "200": {"description": "Search results"},
                        "400": {"description": "Missing query"},
                        "404": {"description": "No results found"},
                    },
                }
            },
            "/name/{imdb_id}": {
                "get": {
                    "summary": "Retrieve name details by IMDB ID",
                    "parameters": [
                        {
                            "in": "path",
                            "name": "imdb_id",
                            "schema": {"type": "string"},
                            "required": True,
                        }
                    ],
                    "responses": {
                        "200": {"description": "Name details"},
                        "404": {"description": "Name not found"},
                    },
                }
            },
        },
    }
    return jsonify(spec)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
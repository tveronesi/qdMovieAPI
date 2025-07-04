# python
from flask import Flask, jsonify, request
from imdbinfo.services import  search_title, get_movie

app = Flask(__name__)

@app.route("/imdb/<string:imdb_id>")
def get_imdb_data(imdb_id):
    movie_data = get_movie(imdb_id)
    if not movie_data:
        return jsonify({"error": "Movie not found"}), 404

    return jsonify(movie_data.model_dump())

@app.route("/search")
def search_imdb():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    results = search_title(query)
    if not results:
        return jsonify({"error": "No results found"}), 404

    return jsonify(results.model_dump())


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
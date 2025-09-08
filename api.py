"""Simple IMDB API powered by FastAPI.

This module exposes a small set of HTTP endpoints to search for movies and
names on IMDB using the ``imdbinfo`` package.  The API documentation is served
automatically by FastAPI at ``/apidoc``.
"""

from fastapi import FastAPI, HTTPException, Query
from imdbinfo import (
    get_movie,
    get_name,
    search_title,
    get_all_episodes,
    get_episodes,
    get_akas,
    get_reviews,
    get_trivia,
)

app = FastAPI(title="qd_imdb_api", version="1.0.0", docs_url="/apidoc")


@app.get("/movie/{imdb_id}", summary="Retrieve movie details by IMDB ID")
def read_movie(imdb_id: str):
    """Return the details for the movie identified by ``imdb_id``."""
    movie_data = get_movie(imdb_id)
    if not movie_data:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie_data.model_dump()


@app.get("/name/{imdb_id}", summary="Retrieve name details by IMDB ID")
def read_name(imdb_id: str):
    """Return the details for the name entry identified by ``imdb_id``."""
    name_data = get_name(imdb_id)
    if not name_data:
        raise HTTPException(status_code=404, detail="Name not found")
    return name_data.model_dump()


@app.get("/search", summary="Search for movie titles")
def search(q: str = Query(..., description="The search term for the movie title")):
    """Search for movie titles that match ``q``."""
    results = search_title(q)
    if not results:
        raise HTTPException(status_code=404, detail="No results found")
    return results.model_dump()


@app.get(
    "/series/{imdb_id}/season/{season}",
    summary="Retrieve episodes for a season of a series",
)
def read_season_episodes(imdb_id: str, season: int):
    """Return the details for the movie identified by ``imdb_id``."""
    episodes = get_episodes(imdb_id, season)
    if not episodes:
        raise HTTPException(status_code=404, detail="Episodes not found")
    return episodes.model_dump()


@app.get("/series/{imdb_id}/episodes", summary="Retrieve episodes for a series")
def read_series_episodes(imdb_id: str):
    """Return the details for all episodes of a series identified by ``imdb_id``."""
    episodes = get_all_episodes(imdb_id)
    if not episodes:
        raise HTTPException(status_code=404, detail="Episodes not found")
    return episodes


@app.get("/akas/{imdb_id}", summary="Retrieve AKAs for a movie or series")
def read_akas(imdb_id: str):
    """Return the AKAs for the movie or series identified by ``imdb_id``."""
    akas = get_akas(imdb_id)
    if not akas:
        raise HTTPException(status_code=404, detail="AKAs not found")
    return akas


@app.get("/reviews/{imdb_id}", summary="Retrieve reviews for a movie or series")
def read_reviews(imdb_id: str):
    """Return the reviews for the movie or series identified by ``imdb_id``."""
    reviews = get_reviews(imdb_id)
    if not reviews:
        raise HTTPException(status_code=404, detail="Reviews not found")
    return reviews


@app.get("/trivia/{imdb_id}", summary="Retrieve trivia for a movie or series")
def read_trivia(imdb_id: str):
    """Return the trivia for the movie or series identified by ``imdb_id``."""
    trivia = get_trivia(imdb_id)
    if not trivia:
        raise HTTPException(status_code=404, detail="Trivia not found")
    return trivia


# root endpoint for health check
@app.get("/", summary="Health check")
def root():
    """Root endpoint for health check."""
    return {"message": "qd_imdb_api is running", "version": app.version}


if __name__ == "__main__":  # pragma: no cover - convenience for local runs
    import uvicorn

    uvicorn.run("api:app", host="0.0.0.0", port=5000, reload=True)

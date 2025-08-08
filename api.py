"""Simple IMDB API powered by FastAPI.

This module exposes a small set of HTTP endpoints to search for movies and
names on IMDB using the ``imdbinfo`` package.  The API documentation is served
automatically by FastAPI at ``/apidoc``.
"""

from fastapi import FastAPI, HTTPException, Query
from imdbinfo.services import get_movie, get_name, search_title, get_episodes

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

@app.get("/series/{imdb_id}/season/{season}", summary="Retrieve episodes for a season of a series")
def read_season_episodes(imdb_id: str, season: int):
    """Return the details for the movie identified by ``imdb_id``."""
    episodes = get_episodes(imdb_id, season)
    if not episodes:
        raise HTTPException(status_code=404, detail="Episodes not found")
    return episodes.model_dump()



if __name__ == "__main__":  # pragma: no cover - convenience for local runs
    import uvicorn

    uvicorn.run("api:app", host="0.0.0.0", port=5000, reload=True)


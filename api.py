"""Simple IMDB API powered by FastAPI.

This module exposes a small set of HTTP endpoints to search for movies and
names on IMDB using the ``imdbinfo`` package.  The API documentation is served
automatically by FastAPI at ``/apidoc``.
"""
from typing import Dict, List, Optional, Union

from fastapi import FastAPI, HTTPException, Query
from imdbinfo import (
    get_movie,
    get_name,
    search_title,
    get_all_episodes,
    get_season_episodes,
    get_akas,
    get_reviews,
    get_trivia,
    get_filmography,  # aggiunto import
    get_parental_guide,
get_media_gallery, get_quotes,get_awards
)
from imdbinfo.models import ParentalGuideList, MovieDetail, PersonDetail, SearchResult, SeasonEpisodesList, \
    BulkedEpisode, AkasData, MediaGallery,Award,Quote

description = """
This project provides a "quick and dirty" API service to retrieve movie information from IMDB.

It uses the [imdbinfo](https://github.com/tveronesi/imdbinfo) package to fetch movie details based on the IMDB ID or title and is powered by [FastAPI](https://fastapi.tiangolo.com/).

[![PyPI Version](https://img.shields.io/pypi/v/imdbinfo?style=flat-square)](https://pypi.org/project/imdbinfo/)

"""
app = FastAPI(
    title="qd movie api",
    description=description,
    version="1.0.0",
    docs_url="/apidoc"

)

LOCALE_QUERY = Query(
    default=None,
    description="Optional locale forwarded to imdbinfo (for example: en-US or it-IT)."
)


@app.get("/movie/{imdb_id}", summary="Retrieve movie details by IMDB ID", response_model=MovieDetail)
def read_movie(imdb_id: str, locale: Optional[str] = LOCALE_QUERY):
    """Return the details for the movie identified by ``imdb_id``."""
    movie_data = get_movie(imdb_id, locale=locale)
    if not movie_data:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie_data.model_dump()


@app.get("/name/{imdb_id}", summary="Retrieve name details by IMDB ID", response_model=PersonDetail)
def read_name(imdb_id: str, locale: Optional[str] = LOCALE_QUERY):
    """Return the details for the name entry identified by ``imdb_id``."""
    name_data = get_name(imdb_id, locale=locale)
    if not name_data:
        raise HTTPException(status_code=404, detail="Name not found")
    return name_data.model_dump()


@app.get("/search", summary="Search for movie titles", response_model=SearchResult)
def search(
    q: str = Query(..., description="The search term for the movie title"),
    locale: Optional[str] = LOCALE_QUERY,
):
    """Search for movie titles that match ``q``."""
    results = search_title(q, locale=locale)
    if not results:
        raise HTTPException(status_code=404, detail="No results found")
    return results.model_dump()


@app.get(
    "/series/{imdb_id}/season/{season}",
    summary="Retrieve episodes for a season of a series",
    response_model=SeasonEpisodesList
)
def read_season_episodes(imdb_id: str, season: int, locale: Optional[str] = LOCALE_QUERY):
    """Return the details for the movie identified by ``imdb_id``."""
    episodes = get_season_episodes(imdb_id, season, locale=locale)
    if not episodes:
        raise HTTPException(status_code=404, detail="Episodes not found")
    return episodes.model_dump()


@app.get("/series/{imdb_id}/episodes", summary="Retrieve episodes for a series", response_model=List[BulkedEpisode])
def read_series_episodes(imdb_id: str, locale: Optional[str] = LOCALE_QUERY):
    """Return the details for all episodes of a series identified by ``imdb_id``."""
    episodes = get_all_episodes(imdb_id, locale=locale)
    if not episodes:
        raise HTTPException(status_code=404, detail="Episodes not found")
    return episodes


@app.get("/akas/{imdb_id}", summary="Retrieve AKAs for a movie or series", response_model=Union[AkasData, list])
def read_akas(imdb_id: str, locale: Optional[str] = LOCALE_QUERY):
    """Return the AKAs for the movie or series identified by ``imdb_id``."""
    akas = get_akas(imdb_id, locale=locale)
    if not akas:
        raise HTTPException(status_code=404, detail="AKAs not found")
    return akas


@app.get("/reviews/{imdb_id}", summary="Retrieve reviews for a movie or series", response_model=List[Dict])
def read_reviews(imdb_id: str, locale: Optional[str] = LOCALE_QUERY):
    """Return the reviews for the movie or series identified by ``imdb_id``."""
    reviews = get_reviews(imdb_id, locale=locale)
    if not reviews:
        raise HTTPException(status_code=404, detail="Reviews not found")
    return reviews


@app.get("/trivia/{imdb_id}", summary="Retrieve trivia for a movie or series", response_model=List[Dict])
def read_trivia(imdb_id: str, locale: Optional[str] = LOCALE_QUERY):
    """Return the trivia for the movie or series identified by ``imdb_id``."""
    trivia = get_trivia(imdb_id, locale=locale)
    if not trivia:
        raise HTTPException(status_code=404, detail="Trivia not found")
    return trivia


@app.get("/filmography/{imdb_id}", summary="Recupera la filmografia completa per una persona", response_model=dict)
def read_filmography(imdb_id: str, locale: Optional[str] = LOCALE_QUERY):
    """Restituisce la filmografia completa della persona identificata da ``imdb_id`` raggruppata per ruolo/lavoro."""
    filmography = get_filmography(imdb_id, locale=locale)
    if not filmography:
        raise HTTPException(status_code=404, detail="Filmografia non trovata")
    return filmography

@app.get("/parental-guide/{imdb_id}", summary="Retrieve parental guide for a movie or series", response_model=ParentalGuideList)
def read_parental_guide(imdb_id: str, locale: Optional[str] = LOCALE_QUERY):
    """Return the parental guide for the movie or series identified by ``imdb_id``."""
    parental_guide = get_parental_guide(imdb_id, locale=locale)
    if not parental_guide:
        raise HTTPException(status_code=404, detail="Parental guide not found")
    return parental_guide

@app.get("/media-gallery/{imdb_id}", summary="Retrieve media gallery for a movie or series", response_model=MediaGallery)
def read_media_gallery(imdb_id: str, locale: Optional[str] = LOCALE_QUERY):
    """Return the media gallery for the movie or series identified by ``imdb_id``."""
    media_gallery = get_media_gallery(imdb_id, locale=locale)
    if not media_gallery:
        raise HTTPException(status_code=404, detail="Media gallery not found")
    return media_gallery

@app.get("/quotes/{imdb_id}", summary="Retrieve quotes for a movie or series", response_model=List[Quote])
def read_quotes(imdb_id: str, locale: Optional[str] = LOCALE_QUERY):
    """Return the quotes for the movie or series identified by ``imdb_id``."""
    quotes = get_quotes(imdb_id, locale=locale)
    if not quotes:
        raise HTTPException(status_code=404, detail="Quotes not found")
    return quotes

@app.get('/awards/{imdb_id}', summary="Retrieve awards for a movie or series", response_model=List[Award])
def read_awards(imdb_id: str, locale: Optional[str] = LOCALE_QUERY):
    """Return the awards for the movie or series identified by ``imdb_id``."""
    awards = get_awards(imdb_id, locale=locale)
    if not awards:
        raise HTTPException(status_code=404, detail="Awards not found")
    return awards

# root endpoint for health check
@app.get("/", summary="Health check")
def root():
    """Root endpoint for health check."""
    return {"message": "qd_imdb_api is running", "version": app.version}


if __name__ == "__main__":  # pragma: no cover - convenience for local runs
    import uvicorn

    uvicorn.run("api:app", host="0.0.0.0", port=5000, reload=True)

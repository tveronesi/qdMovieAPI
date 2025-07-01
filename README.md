# qd_imdb_api

This project provides a "quick and dirty" API service to retrieve movie information from IMDB.
It uses the qd_imdb_service library to fetch movie details based on the IMDB ID or title.

### example usage:
```python
from qd_imdb_service.services import search_title, get_movie_details
movie_search = search_title("The Matrix")
print(movie_search)
# output:
#[
#   {
#      "imdbId": "tt0133093",
#      "imdb_id": "0133093",
#      "title": "Matrix",
#      "year": 1999
#   },
#   {
#      "imdbId": "tt10838180",
#      "imdb_id": "10838180",
#      "title": "Matrix Resurrections",
#      "year": 2021
#   },
#   {
#      "imdbId": "tt0234215",
#      "imdb_id": "0234215",
#      "title": "Matrix Reloaded",
#      "year": 2003
#   },

movie_details = get_movie_details('0133093')
print(movie_details)
# output:

#{
#   "aspect_ratios": [],
#   "cameras": [],
#   "cast": [],
#   "certificates": [],
#   "country_codes": [],
#   "cover": "https://m.media-amazon.com/images/M/MV5BOWVlOTU2MzktN2Q0Ny00Y2M5LTkzY2QtNjBjOWRhZTQwMmQxXkEyXkFqcGc@._V1_.jpg",
#   "directors": [],
#   "duration": 136,
#   "filming_locations": [],
#   "genres": [],
#   "imdbId": "tt0133093",
#   "imdb_id": 133093,
#   "interests": [],
#   "laboratories": [],
#   "languages": [],
#   "metacritic_rating": 73,
#   "negative_formats": [],
#   "plot": "When a beautiful stranger leads computer hacker Neo to a forbidding underworld, he discovers the shocking truth--the life he knows is the elaborate deception of an evil cyber-intelligence.",
#   "printed_formats": [],
#   "processes": [],
#   "production": [],
#   "production_budget": "63000000 USD",
#   "rating": 8.7,
#   "release_date": "1999-05-07",
#   "sound_mixes": [],
#   "storyline_keywords": [],
#   "summaries": [],
#   "synopses": [],
#   "title": "The Matrix",
#   "trailers": [
#      "https://www.imdb.com/video/vi1032782617",
#      "https://www.imdb.com/video/vi3203793177"
#   ],
#   "url": "https://www.imdb.com/title/tt0133093/",
#   "votes": 2165907,
#   "worldwide_gross": "467841735 USD",
#   "year": 1999
#}
```
## Description

The flask application in `api.py` offers a simple REST API to get movie details via HTTP requests. 
It is designed to be simple and quick to start, ideal for testing or prototyping.
It uses the `qd_imdb_service` library to fetch movie data from IMDB.


## Features
- Fetch movie details from IMDB
- Supports querying by IMDB ID
- Simmle movie search by title 
- Returns movie information

## Requirements

- Docker and Docker Compose installed
- (Optional) Python 3.8+ and pip, if you want to run the app locally without a container

## Starting with Docker Compose

1. Clone the repository and navigate to the project folder.
2. Build and run the service with:

   ```sh
   docker-compose up --build
    ```
   
3. The API will be available at `http://127.0.0.1:5000`.
4. To test the API, you can use tools like `curl`, Postman, or simply your web browser. For example, to get information about a movie with ID `tt0133093` (The Matrix), you can make a GET request using curl:

    ```sh
   curl http://127.0.0.1:5000/search?q=matrix
    curl http://127.0.0.1:5000/imdb/0133093
    ```
   
## Running Locally without Docker

If you prefer to run the application without Docker, you can do so by following these steps:
1. Ensure you have Python 3.8+ installed.
2. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```
3. Run the application:

   ```sh
    python api.py
    ```
4. The API will be available at `http://127.0.0.1:5000`.

## PIP install `qd_imdb_service`
There is not yet been a release of the `qd_imdb_service` library on PyPI, but you can install it directly from the source code:

```sh
pip install git+https://github.com/tveronesi/qdMovieAPI.git
```

## License
Copyright (C)  2025 T.Veronesi

This code is released under the GPL license, version 2 or later.

Read the included [`LICENSE.txt`](LICENSE.txt) file for details.

This project and its authors are not affiliated in any way to Internet Movie Database Inc.; see the  [`DISCLAIMER.txt`](DISCLAIMER.txt) file for details about data licenses.

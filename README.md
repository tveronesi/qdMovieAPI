# qd_imdb_api

This project provides a "quick and dirty" API service to retrieve movie information from IMDB.
It uses the [imdbinfo](https://github.com/tveronesi/imdbinfo) package to fetch movie details based on the IMDB ID or title and is powered by [FastAPI](https://fastapi.tiangolo.com/).

## Usage

1. Clone the repository and navigate to the project folder.
2. Build and run the service with:

   ```sh
   docker compose up --build
   ```
   
3. The API will be available at `http://127.0.0.1:5000`.
4. All `imdbinfo`-backed endpoints accept an optional `locale` query parameter and forward it upstream.
   - example locale values: `en-US`, `it-IT`
   - example usage: `http://127.0.0.1:5000/movie/0234215?locale=it-IT`
5. The API exposes the following endpoints:
   - `/search?q=<searchstring>[&locale=<locale>]`
     - example: `http://127.0.0.1:5000/search?q=matrix&locale=en-US`
   - `/movie/<imdb_id>[?locale=<locale>]`
     - example: `http://127.0.0.1:5000/movie/0234215?locale=it-IT`
   - `/name/<imdb_id>[?locale=<locale>]`
     - example: `http://127.0.0.1:5000/name/nm0000206?locale=en-US`
   - `/series/<imdb_id>/season/<season>[?locale=<locale>]`
     - example: `http://127.0.0.1:5000/series/tt0944947/season/1?locale=en-US`
   - `/series/<imdb_id>/episodes[?locale=<locale>]`
     - example: `http://127.0.0.1:5000/series/tt0944947/episodes?locale=en-US`
   - `/akas/<imdb_id>[?locale=<locale>]`
     - example: `http://127.0.0.1:5000/akas/tt0944947?locale=it-IT`
   - `/trivia/<imdb_id>[?locale=<locale>]`
     - example: `http://127.0.0.1:5000/trivia/tt0944947?locale=en-US`
   - `/reviews/<imdb_id>[?locale=<locale>]`
     - example: `http://127.0.0.1:5000/reviews/tt0944947?locale=en-US`
   - `/filmography/<imdb_id>[?locale=<locale>]`
     - example: `http://127.0.0.1:5000/filmography/nm0000206?locale=it-IT`
     - returns the complete filmography of a person grouped by role
   - `/parental-guide/<imdb_id>[?locale=<locale>]`
     - example: `http://127.0.0.1:5000/parental-guide/tt0944947?locale=en-US`
     - returns the parental guide information for a movie or series
   - `/apidoc`
     - auto-generated Swagger/OpenAPI documentation for the service
   - `/`
     - health check endpoint


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

## Requirements
- Python 3.8 or higher
- `imdbinfo` package for fetching movie details
- FastAPI for creating the API service and automatic API documentation
- Uvicorn for running the ASGI server

## Package imdbinfo

For details on how to use the `imdbinfo` package, please refer to the [imdbinfo](https://github.com/tveronesi/imdbinfo) GitHub repository.

## License
Copyright (C)  2025 T.Veronesi

This code is released under the GPL license, version 2 or later.

Read the included [`LICENSE.txt`](LICENSE.txt) file for details.

This project and its authors are not affiliated in any way to Internet Movie Database Inc.; see the [`DISCLAIMER.txt`](DISCLAIMER.txt) file for details about data licenses.

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
4. The API exposes the following endpoints:
   - `/search?q=<searchstring>`
     - example: http://127.0.0.1:5000/search?q=matrix
   - `/movie/<imdb_id>`
     - example: http://127.0.0.1:5000/movie/0234215
   - `/name/<imdb_id>`
     - example: http://127.0.0.1:5000/name/nm0000206
   - `/series/<imdb_id>/season/<season>`
     - example: http://127.0.0.1:5000/series/tt0944947/season/1
   - `/series/<imdb_id>/episodes`
     - example: http://127.0.0.1:5000/series/tt0944947/episodes
    - `/akas/<imdb_id>
     - example: http://127.0.1:5000/akas/tt0944947`
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
   # or
   uvicorn api:app --host 0.0.0.0 --port 5000 --reload
   ```
4. The API will be available at `http://127.0.0.1:5000`.

## Requirements
- Python 3.8 or higher
- `imdbinfo` package for fetching movie details
- FastAPI for creating the API service and automatic API documentation
- Uvicorn for running the ASGI server

## Package imdbinfo

FOr details on how to use the `imdbinfo` package, please refer to the [imdbinfo](https://github.com/tveronesi/imdbinfo) Github repository.

## License
Copyright (C)  2025 T.Veronesi

This code is released under the GPL license, version 2 or later.

Read the included [`LICENSE.txt`](LICENSE.txt) file for details.

This project and its authors are not affiliated in any way to Internet Movie Database Inc.; see the  [`DISCLAIMER.txt`](DISCLAIMER.txt) file for details about data licenses.

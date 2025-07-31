# qd_imdb_api

This project provides a "quick and dirty" API service to retrieve movie information from IMDB.
It uses the [imdbinfo](https://github.com/tveronesi/imdbinfo) package to fetch movie details based on the IMDB ID or title.

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
   - `/apidoc`
     - auto-generated Swagger/OpenAPI documentation for the service


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
- Flask for creating the API service
- Flask-RESTX for REST utilities and automatic API documentation

## Package imdbinfo

FOr details on how to use the `imdbinfo` package, please refer to the [imdbinfo](https://github.com/tveronesi/imdbinfo) Github repository.

## License
Copyright (C)  2025 T.Veronesi

This code is released under the GPL license, version 2 or later.

Read the included [`LICENSE.txt`](LICENSE.txt) file for details.

This project and its authors are not affiliated in any way to Internet Movie Database Inc.; see the  [`DISCLAIMER.txt`](DISCLAIMER.txt) file for details about data licenses.

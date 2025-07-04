# qd_imdb_api

This project provides a "quick and dirty" API service to retrieve movie information from IMDB.

## Description

The application is written in Python and offers a REST API to get movie details via HTTP requests. It is designed to be simple and quick to start, ideal for testing or prototyping.
This project is intended solely as a starting point for development and testing purposes.  
It is not suitable for production use.

## Features
- Fetch movie details from IMDB
- Supports querying by IMDB ID
- Returns movie information in JSON format

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
    curl http://127.0.0.1:5000/imdb?imdb_id=0133093
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

## Future Improvements

Feel free to fork this project and contribute to its development. Here are some ideas for future improvements:

- Implement more endpoints for additional movie data.
- Add error handling and validation for input parameters.
- Output Format with pydantic models for better structure and validation.
- Add OpenAPI documentation for better API usability.
- Add unit tests for the API endpoints.
- Add caching to improve performance for frequently requested data.

## License
Copyright (C)  2025 T.Veronesi

This code is released under the GPL license, version 2 or later.

Read the included [`LICENSE.txt`](LICENSE.txt) file for details.

This project and its authors are not affiliated in any way to Internet Movie Database Inc.; see the  [`DISCLAIMER.txt`](DISCLAIMER.txt) file for details about data licenses.

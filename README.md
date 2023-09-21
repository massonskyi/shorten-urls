# URL Shortener Service (Python & PHP)

This project contains URL shortener services implemented in both Python and PHP. The primary purpose of this tool is to provide a shorter, easily shareable version of any long URL. The code is straightforward and easy to understand, making it simple to integrate into other projects.

## Python Implementation

The Python implementation is built using FastAPI and does not require any external databases. The shortened URL is generated using the `uuid` library, and a unique 6-digit code is stored in an in-memory dictionary to map the shortened URL to the original URL.

### Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Pydantic

To install required libraries, run the following command:

```bash
$ pip install fastapi uvicorn pydantic
```

### Usage

Run the FastAPI application with Uvicorn using the following command:

```bash
$ uvicorn shorten:app --host 0.0.0.0 --port 8000
```

#### Endpoints

* `POST /url`: Receives the original URL and generates a short URL in response.
* `GET /redirect/{url_id}`: Takes the short URL as input and redirects to the original URL, if it exists. If not, a 404 error is returned.

## PHP Implementation

The PHP implementation is very simple. It consists of two separate files. The first one takes an original URL, generates a unique 6-digit code and appends the short url to a text file. The second file reads the text file, looks for corresponding unique 6-digit code, and handles redirection to the long URL.

### Requirements

- PHP 7.0+
- PHP Webserver (Apache, Nginx, or any other web server with PHP support)

### Usage

Upload the PHP files to your web server directory, then:
1. Send a `POST` request with the parameter `long_url` containing the long URL you'd like to shorten.
2. Access the shortened URL using a `GET` request with the `short_code` as a parameter.

## License

This project is released under the MIT License. Feel free to use, modify, and distribute the code as you wish.

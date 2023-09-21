from pprint import pprint

import requests as req


def post(url: str, data: str) -> dict:
    request: dict = {
        "original_url": data
    }
    return req.post(url, json=request).json()


def create_shorten_url():
    local_url = "http://localhost:8000/url"
    shorting_url = "https://www.example.com/"
    pprint(post(local_url, shorting_url))


create_shorten_url()
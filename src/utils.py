from urllib.parse import quote_plus


def encode_url(url: str) -> str:
    return quote_plus(url)

from urllib.parse import urlparse

def is_valid_url(url, domain):
    parsed = urlparse(url)
    return parsed.scheme in ("http", "https") and domain in parsed.netloc

def normalize_url(url):
    return url.split('#')[0].rstrip('/')
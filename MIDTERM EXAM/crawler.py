import threading
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from utils import is_valid_url, normalize_url

visited = set()
lock = threading.Lock()

MAX_DEPTH = 2
DOMAIN = "books.toscrape.com"

def crawl(url, depth):
    if depth == 0:
        return
    try:
        print(f"Crawling: {url} at depth {depth}")

        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            print(f"Failed to retrieve {url}: Status {response.status_code}")
            return

        soup = BeautifulSoup(response.text, "html.parser")
        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                full_url = normalize_url(urljoin(url, href))
                if is_valid_url(full_url, DOMAIN):
                    with lock:
                        if full_url not in visited:
                            visited.add(full_url)
                            print(f"Found URL: {full_url}")
                            with open("output.txt", "a", encoding="utf-8") as f:
                                f.write(full_url + "\n")
                    threading.Thread(target=crawl, args=(full_url, depth - 1)).start()

    except Exception as e:
        print(f"[Error] Failed to crawl {url}: {e}")

if __name__ == "__main__":
    start_url = f"http://{DOMAIN}"
    crawl(start_url, MAX_DEPTH)

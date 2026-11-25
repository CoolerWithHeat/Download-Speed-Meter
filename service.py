import time
import urllib.request as engine

urls = []

stealth_mode = True

def request_process(url: str) -> tuple[float, int]:
    request = engine.Request(
        url,
        headers = {} if not stealth_mode else {
            "User-Agent": (
                "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) "
                "AppleWebKit/605.1.15 (KHTML, like Gecko) "
                "Version/18.0 Mobile/15E148 Safari/604.1"
            )
        }
    )
    start = time.perf_counter()
    with engine.urlopen(request, timeout=30) as response:
        data = response.read()

    elapsed = time.perf_counter() - start

    return elapsed, len(data)

def main():
    
    copied_urls = [*urls]
    url_index = 0

    while len(copied_urls) > url_index:
        staged_url = copied_urls[url_index]
        time_spent, responses = request_process(staged_url)
        print(time_spent, responses)
        url_index+=1

if __name__ == '__main__':
    main()
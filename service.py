import time
import urllib.request as engine

urls = []

def request_meter(url: str) -> tuple[float, int]:
    request = engine.Request(
        url,
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
        time_spent, responses = request_meter(staged_url)
        print(time_spent, responses)
        url_index+=1

if __name__ == '__main__':
    main()
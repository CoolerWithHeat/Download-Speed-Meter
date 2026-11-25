import os, time
import urllib.request as engine
from ConsoleManagement.errors import FetchFailureError
import Environment.populate

urls = []

failed_urls = []

stealth_mode = False

def clear_terminal():
    print("\033[2J\033[H", end="", flush=True)

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
    try: 
        start = time.perf_counter()

        with engine.urlopen(request, timeout=30) as response:
            data = response.read()

        time_passed = time.perf_counter() - start

        return time_passed, len(data)
    except Exception as error:
        return FetchFailureError(url, error, failed_urls)

def main():

    clear_terminal()

    copied_urls = [*urls]
    url_index = 0
    request_durations = 0
    
    while len(copied_urls) > url_index:
        staged_url = copied_urls[url_index]
        time_passed, responses = request_process(staged_url)
        request_durations += time_passed
        url_index+=1

if __name__ == '__main__':
    main()
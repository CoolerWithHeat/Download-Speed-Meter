import time
import urllib.request as engine
from ConsoleManagement.errors import FetchFailureError
from ConsoleManagement.results import OutputFinalResult

stealth_mode = True

def request_process(url: str) -> tuple[float, int, bool]:
    try:
        request = engine.Request(
            url,
            headers={} if not stealth_mode else {
                "User-Agent": (
                    "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) "
                    "AppleWebKit/605.1.15 (KHTML, like Gecko) "
                    "Version/18.0 Mobile/15E148 Safari/604.1"
                )
            },
        )
        start = time.perf_counter()

        with engine.urlopen(request, timeout=30) as response:
            data = response.read()

        time_passed = time.perf_counter() - start

        return time_passed, len(data), True
    except Exception as error:
        FetchFailureError(url, error)
        return 0.0, 0, False

def meter_service(url, attempts=10, pure=False):
    total_duration = 0.0
    total_size = 0
    successful_attempts = 0
    failed_attempts = 0

    for _ in range(attempts):
        time_passed, size, succeeded = request_process(url)
        if succeeded:
            total_duration += time_passed
            total_size += size
            successful_attempts += 1
        else:
            failed_attempts += 1

    OutputFinalResult(
        total_duration,
        total_size,
        successful_attempts,
        failed_attempts,
        pure,
    )

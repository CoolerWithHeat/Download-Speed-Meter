import time, types
from collections.abc import Callable

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"

def FetchFailureError(url: str, exception_text: str, failure_list: list[str]):
    failure_list.append(url)
    
    print(f'\n{YELLOW}Error occured when fetching url: {url}')
    print(f'\n{RED}Exception details from interpreter:\n    {exception_text}')

    return 0, 0
RED = "\033[91m"
YELLOW = "\033[93m"

def clear_terminal():
    print("\033[2J\033[H", end="", flush=True)

def FetchFailureError(url: str, exception_text: str):
    print(f'\n{YELLOW}Error occured when fetching url: {url}')
    print(f'\n{RED}Exception details from interpreter:\n    {exception_text}')

def DependencyFailureError(text):
    clear_terminal()
    print(f'\n\n{RED}{text}\n')

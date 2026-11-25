from ConsoleManagement.errors import clear_terminal
from Measurements.SpeedMeter import format_download_speed

GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"

def DependencySuccessMessage(text):
    print(f'{GREEN}\n{text}\n')
    print(f'\n{BLUE}Processing...')
    return

def OutputFinalResult(
    total_duration: float,
    total_size: int,
    successful_attempts: int,
    failed_attempts: int,
    pure: bool = False,
):
    clear_terminal()

    total_attempts = successful_attempts + failed_attempts
    if total_attempts <= 0:
        return print(f"{YELLOW}No download attempts to report.")

    print(
        f"{BLUE}Attempts: {total_attempts} "
        f"({successful_attempts} successful, {failed_attempts} failed)"
    )

    if successful_attempts:
        average_time = total_duration / successful_attempts
        print(f"{GREEN}Average download time: {average_time:.2f} seconds")
        average_speed = format_download_speed(total_size, total_duration, pure)
        print(f"{GREEN}Average download speed: {average_speed}")
    else:
        print(f"{YELLOW}No successful downloads; average time is unavailable.")

    if pure:
        print(f"{BLUE}Total downloaded content: {total_size} B")
    else:
        size = float(total_size)
        units = ("B", "KB", "MB", "GB", "TB")
        for unit in units:
            if size < 1024 or unit == units[-1]:
                break
            size /= 1024

        print(f"{BLUE}Total downloaded content: {size:.2f} {unit}")


def format_download_speed(download_size: int, elapsed_seconds: float, pure: bool = False) -> str:
    
    if elapsed_seconds <= 0:
        return "unavailable"

    bytes_per_second = download_size / elapsed_seconds
    if pure:
        return f"{bytes_per_second:.2f} B/s"

    value = bytes_per_second
    
    units = ("B/s", "KB/s", "MB/s", "GB/s", "TB/s")

    for unit in units:
        if value < 1024 or unit == units[-1]:
            return f"{value:.2f} {unit}"
        value /= 1024

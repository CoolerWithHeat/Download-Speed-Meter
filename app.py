import argparse
import importlib.util
import sys
from ConsoleManagement.results import DependencySuccessMessage
from ConsoleManagement.errors import DependencyFailureError

critical_packages = ["urllib", "os", "time"] # These exist in standard python versions already, just as a demonstration for managing dependencies later at runtime.

def get_arguments(argv=None):
    parser = argparse.ArgumentParser(description="Measure download speed for a URL.")
    parser.add_argument("--url", required=True, help="URL of the file to download")
    parser.add_argument(
        "--try",
        dest="attempts",
        type=positive_integer,
        default=10,
        metavar="COUNT",
        help="number of download attempts (default: 10)",
    )
    parser.add_argument(
        "--pure",
        action="store_true",
        help="show byte counts without converting them to larger units",
    )
    return parser.parse_args(argv)

def positive_integer(value):
    try:
        number = int(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError("must be a positive integer") from error
    if number <= 0:
        raise argparse.ArgumentTypeError("must be a positive integer")
    return number

def check_dependencies():
    for dependency in critical_packages:
        failed_packages_list = []
        if importlib.util.find_spec(dependency) is None:
            DependencyFailureError(f'Error: dependency "{dependency}" is not available to proceed.')
            failed_packages_list.append(dependency)
            
        if len(failed_packages_list):
            print('\nScript terminated...')
            sys.exit(1)

    DependencySuccessMessage("Dependency check passed!")
    return True


def start_service(argv=None):
    args = get_arguments(argv)
    proceed = check_dependencies()
    if proceed: 
        from service import meter_service
        meter_service(args.url, args.attempts, pure=args.pure)

if __name__ == "__main__":
    start_service()
